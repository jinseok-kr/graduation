# -*- coding: utf-8 -*-
from konlpy.tag import Hannanum
from collections import Counter


class KeyExtraction(object):
    def __init__(self):
        self.hannanum= Hannanum();
        self.stopwords = ["중인", "만큼", "마찬가지", "꼬집었", "연합뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "뉴스1", "뉴시스", "기자"
            , "아", "지난", "이번", "오늘", "이날", "이상", "이하", "이전", "이후", "오전", "오후", "최소", "최대", "직후", "어", "나", "우리"
            , "저희", "따라", "의해", "을", "를", "에", "의", "가", "후보", "대부분", "민간", "결정적", "의혹"]

    def extraction(self, txt):
        wordrank = []
        nouns_list = self.hannanum.nouns(txt)
        count = Counter(nouns_list)

        for tag, counts in count.most_common(50):
            if ((len(str(tag)) > 1) and (tag not in self.stopwords) and (counts >= 2)):
                wordrank.append(tag)
            if len(wordrank) == 15:
                break;

        if len(wordrank) <= 3:
            return []

        return wordrank