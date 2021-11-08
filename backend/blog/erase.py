import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings.product')
# 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

from blog.models import News, NewsTopics, NewsTag
import datetime

#before_day=datetime.datetime.now()-datetime.timedelta(days=1)
NewsTopics.objects.all().delete()
News.objects.all().delete()
NewsTag.objects.all().delete()
#Topics.objects.filter(created_dt__lt=before_day).delete()
