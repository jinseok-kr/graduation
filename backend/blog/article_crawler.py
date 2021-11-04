import os
import sys
import platform
import requests
import re
import time
from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Process
from exceptions import *
from article_parser import ArticleParser
from writer import Writer
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.develop')

import django
django.setup()

from blog.models import News, NewsTopics

class ArticleCrawler(object):
    def __init__(self):
        '''
        self.categories = {'정치': 100, '경제': 101, '사회': 102, '생활문화': 103, '세계': 104, 'IT과학': 105, '오피니언': 110,
                           'politics': 100, 'economy': 101, 'society': 102, 'living_culture': 103, 'world': 104,
                           'IT_science': 105, 'opinion': 110}
        '''
        self.categories = {'정치': 100, '경제': 101, '사회': 102, '생활문화': 103, '세계': 104, 'IT과학': 105, '오피니언': 110}
        self.selected_categories = []
        self.date = {'year': 0, 'month': 0, 'day': 0}
        self.user_operating_system = str(platform.system())

    def set_category(self, *args):
        for key in args:
            if self.categories.get(key) is None:
                raise InvalidCategory(key)
        self.selected_categories = args

    # Crawling할 기사의 URL date를 오늘 날짜로 지정
    def set_date(self):
        cur_time = time.localtime()  # tm_year, tm_mon, tm_mday (int type)
        args = [cur_time.tm_year, cur_time.tm_mon, cur_time.tm_mday]

        for key, date in zip(self.date, args):
            self.date[key] = date
        print(self.date)

    #@staticmethod
    def make_news_page_url(self, category_url):
        made_urls = []

        # year, month, day를 str로 변환
        if len(str(self.date['month'])) == 1:
            month = "0" + str(self.date['month'])
        else:
            month = str(self.date['month'])

        if len(str(self.date['day'])) == 1:
            day = "0" + str(self.date['day'])
        else:
            day = str(self.date['day'])

        year = str(self.date['year'])

        # 오늘 날짜의 url 생성
        url = category_url + year + month + day

        # totalpage는 네이버 페이지 구조를 이용해서 page=10000으로 지정해 totalpage를 알아냄
        # page=10000을 입력할 경우 페이지가 존재하지 않기 때문에 page=totalpage로 이동 됨 (Redirect)
        totalpage = ArticleParser.find_news_totalpage(url + "&page=10000")

        # 전체 page를 적용한 url을 list로 저장
        for page in range(totalpage, 0, -1):
            made_urls.append(url + "&page=" + str(page))

        return made_urls

    @staticmethod
    def get_url_data(url, max_tries=5):
        remaining_tries = int(max_tries)
        while remaining_tries > 0:
            try:
                return requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            except requests.exceptions:
                sleep(1)
            remaining_tries = remaining_tries - 1
        raise ResponseTimeout()

    def crawling(self, category_name):
        # Multi Process PID
        print(category_name + " PID: " + str(os.getpid()))

        self.set_date()

        writer = Writer(category='Article', article_category=category_name, date=self.date)

        ###url_format = f'http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1={self.categories.get(category_name)}&date='
        url_format = f'https://news.naver.com/main/list.naver?mode=LSD&mid=shm&sid1={self.categories.get(category_name)}&date='
        target_urls = self.make_news_page_url(url_format) # URL page list

        print(category_name + " Urls are generated")
        print("The crawler starts")

        cnt = 0
        for url in target_urls:
            request = self.get_url_data(url)
            document = BeautifulSoup(request.content, 'html.parser')

            ### 여기부터 변수 변경

            # html - newsflash_body - type06_headline, type06
            # 각 페이지에 있는 기사들 가져오기
            temp_post = document.select('.newsflash_body .type06_headline li dl')
            temp_post.extend(document.select('.newsflash_body .type06 li dl'))

            # 각 페이지에 있는 기사들의 url 저장
            post_urls = []
            for line in temp_post:
                # 해당되는 page에서 모든 기사들의 URL을 post_urls 리스트에 넣음
                post_urls.append(line.a.get('href'))
            post_urls.reverse()
            del temp_post

            for content_url in post_urls:  # 기사 url
                cnt = cnt + 1

                # 크롤링 대기 시간
                sleep(0.01)

                # 기사 HTML 가져옴
                request_content = self.get_url_data(content_url)

                try:
                    document_content = BeautifulSoup(request_content.content, 'html.parser')
                except:
                    continue

                try:
                    # ID 생성 (sid=분야ID, oid=신문사ID, aid=기사ID 조합)
                    news_id = "'" + str(re.sub(r'[^0-9]', '', content_url)[1:]) # csv 저장시 1의자리 내림이 되어서 우선 '문자 넣어 놓음
                    print(news_id)

                    # 기사 제목 태그 추출
                    tag_title = document_content.find_all('h3', {'id': 'articleTitle'}, {'class': 'tts_head'})

                    # 뉴스 기사 제목 초기화
                    text_title = ''
                    text_title = text_title + ArticleParser.clear_headline(
                        str(tag_title[0].find_all(text=True)))

                    # 공백일 경우 기사 제외 처리
                    if not text_title:
                        continue
                    #print(text_title)

                    # 기사 본문 태그 추출
                    #tag_content = document_content.find_all('div', {'id': 'articleBodyContents'})
                    tag_content = document_content.find_all('div', {'id': 'articleBodyContents'})[0]

                    # 뉴스 기사 본문 초기화
                    text_content = ''
                    #text_content = text_content + ArticleParser.clear_content(str(tag_content[0].find_all(text=True)))
                    text_content = text_content + str(tag_content)
                    #print(text_sentence)

                    # 공백일 경우 기사 제외 처리
                    if not text_content:
                        continue

                    # 기사 언론사 태그 추출
                    tag_press = document_content.find_all('meta', {'property': 'me2:category1'})

                    text_press = ''
                    text_press = text_press + str(tag_press[0].get('content'))

                    #print(text_press)

                    # 공백일 경우 기사 제외 처리
                    if not text_press:
                        print("company vacant")
                        continue

                    # 기사 작성 시간 추출
                    time = re.findall('<span class="t11">(.*)</span>', request_content.text)[0]

                    #print(time)

                    # CSV 작성
                    writer.write_row([news_id, time, category_name, text_press, text_title, text_content, content_url])
                    #News(news_id=news_id, category=category_name, url=content_url, title=text_title, main_contents=text_content, press=text_press, create_data=time).save()
                    News.objects.create(news_id=news_id, category=category_name, url=content_url, title=text_title,
                                      main_contents=text_content, press=text_press, create_date=time)


                    del news_id, time
                    #del text_headline, text_sentence, text_company
                    #del tag_headline, tag_content, tag_company
                    del tag_content
                    del request_content, document_content

                # UnicodeEncodeError
                except Exception as ex:
                    del request_content, document_content
                    pass
                print('{0}번째 크롤링 완료'.format(cnt))
        writer.close()

    def start(self):
        # MultiProcess 크롤링 시작
        for category_name in self.selected_categories:
            proc = Process(target=self.crawling, args=(category_name,))
            proc.start()

        '''
        for category_name in self.selected_categories:
            r_proc = Process(target=self.realtime_crawling, args=(category_name,))
            r_proc.start()
        '''

if __name__ == "__main__":
    before_day = datetime.datetime.now() - datetime.timedelta(days=1)
    NewsTopics.objects.filter(created_dt__lt=before_day).delete()

    Crawler = ArticleCrawler()
    #정치 경제 사회 생활문화 세계 IT과학 오피니언
    Crawler.set_category('오피니언')
    Crawler.start()