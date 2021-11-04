from django.contrib.auth import login, logout, update_session_auth_hash, get_user
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.db.models import Count
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView, BaseUpdateView, BaseDeleteView
from django.views.generic.list import BaseListView
#from taggit.models import Tag
from blog.models import NewsTopics

from blog.models import News
from accounts.forms import MyUserCreationForm
from accounts.views import MyLoginRequiredMixin
from accounts.views import OwnerOnlyMixin
from api.views_util import obj_to_post, prev_next_post, make_tag_cloud


class ApiNewsLV(BaseListView):
    # model = News
    def get_queryset(self):
        keyname = self.request.GET.get('keyname')
        if keyname:
            qs = News.objects.filter(keywords__name=keyname)
        else:
            qs = News.objects.all()
        return qs

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        newsList = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=newsList, safe=False, status=200)

class ApiNewsDV(BaseDetailView):
    model = News

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        news = obj_to_post(obj)
        news['prev'], news['next'] = prev_next_post(obj)
        return JsonResponse(data=news, safe=True, status=200)


class ApikeywordCloudLV(BaseListView):
    # model = Tag
    #queryset = Tag.objects.annotate(count=Count('post'))
    queryset = NewsTopics.objects.annotate(count=Count('news'))

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        keyList = make_key_cloud(qs)
        return JsonResponse(data=keyList, safe=False, status=200)


class ApiNewsScrapLV(MyLoginRequiredMixin, BaseListView):
    def get_queryset(self):
        username = self.request.user.username
        qs = News.objects.filter(scrap__username=username)
        return qs

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        newsList = [obj_to_post(obj) for obj in qs]
        return JsonResponse(data=newsList, safe=False, status=200)

class ApiNewsScrapDView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse(data={'errmsg': 'you should login first!'}, safe=True, status=401)
        else:
            if 'news_id' in kwargs:
                news_id = kwargs['news_id']
                print(news_id)
                news = News.objects.get(pk=news_id)
                print(news)
                user = request.user
                if user in news.scrap.all():
                    news.scrap.remove(user)
                    return JsonResponse(data={'successmsg': 'unscrapped!'}, safe=True, status=200)
                else:
                    return JsonResponse(data={'errmsg': 'Already unscrapped.'}, safe=True, status=401)


class ApiPostScrapAddView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse(data={'errmsg': 'you should login first!'}, safe=True, status=401)
        else:
            if 'news_id' in kwargs:
                news_id = kwargs['news_id']
                print(news_id)
                news = News.objects.get(pk=news_id)
                print(news)
                user = request.user
                if user in news.scrap.all():
                    return JsonResponse(data={'errmsg':'Already scrapped.'}, safe=True, status=401)
                else:
                    news.scrap.add(user)
                    return JsonResponse(data={'successmsg':'scrapped!'}, safe=True, status=200)

