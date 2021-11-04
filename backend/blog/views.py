from django.views.generic import TemplateView




class PostListTV(TemplateView):
    # TemplateView를 상속 받는다면, template_name은 무조건 넣어줘야한다.
    template_name = 'blog/post_list.html'

class PostDetailTV(TemplateView):
    template_name = 'blog/post_detail.html'

class ScrapListTV(TemplateView):
    template_name = 'blog/post_scrap.html'

#NEWS PART
class NewsListTV(TemplateView):
    # TemplateView를 상속 받는다면, template_name은 무조건 넣어줘야한다.
    template_name = 'blog/news_list.html'

class NewsDetailTV(TemplateView):
    template_name = 'blog/news_detail.html'

class NewsScrapListTV(TemplateView):
    template_name = 'blog/news_scrap.html'

