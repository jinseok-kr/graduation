from django.urls import path

from api import views

app_name ='api'

urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('tag/cloud/', views.ApiTagCloudLV.as_view(), name='tag_cloud'),

    path('post/scrap/', views.ApiPostScrapLV.as_view(), name='post_scrap'),
    path('post/<int:post_id>/scrap/delete/', views.ApiPostScrapDView.as_view(), name='post_scrap_delete'),
    path('post/<int:post_id>/scrap/add/', views.ApiPostScrapAddView.as_view(), name='post_scrap_add'),

    path('post/create/', views.ApiPostCV.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.ApiPostUV.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.ApiPostDelV.as_view(), name='delete_update'),

    path('news/list/', views.ApiNewsLV.as_view(), name='news_list'),
    path('news/<int:pk>/', views.ApiNewsDV.as_view(), name='news_detail'),
    path('keyword/cloud/', views.ApiKeywordCloudLV.as_view(), name='keyword_cloud'),

    path('news/scrap/', views.ApiNewsScrapLV.as_view(), name='news_scrap'),
    path('news/<int:news_id>/scrap/delete/', views.ApiNewsScrapDView.as_view(), name='news_scrap_delete'),
    path('news/<int:news_id>/scrap/add/', views.ApiNewsScrapAddView.as_view(), name='news_scrap_add'),

    path('login/', views.ApiLoginView.as_view(), name='login'),
    path('register/', views.ApiRegisterView.as_view(), name='register'),
    path('logout/', views.ApiLogoutView.as_view(), name='logout'),
    path('pwdchg/', views.ApiPwdchgView.as_view(), name='pwdchg'),
    path('me/', views.ApimeView.as_view(), name='me'),

]