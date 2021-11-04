from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns =[
    path('post/list/', views.PostListTV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailTV.as_view(), name='post_detail'),
    path('post/scrap/', views.ScrapListTV.as_view(), name='scrap_list'),

    path('news/list/', views.NewsListTV.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailTV.as_view(), name='news_detail'),
    path('news/scrap/', views.NewsScrapListTV.as_view(), name='news_scrap_list'),
]