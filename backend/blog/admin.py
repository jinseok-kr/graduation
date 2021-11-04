from django.contrib import admin

from blog.models import Post, Topics, PostTag, News, NewsTopics, NewsTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'tag_list')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

@admin.register(Topics)
class TopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_dt')

@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'tag', 'created_dt')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'press', 'create_date', 'keyword_list')

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('keywords')

    def keyword_list(self, obj):
        return u", ".join(o.name for o in obj.keywords.all())

@admin.register(NewsTopics)
class NewsTopicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_dt')

@admin.register(NewsTag)
class NewsTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_object', 'tag', 'created_dt')