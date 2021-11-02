from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TagBase, ItemBase


class Topics(TagBase):
    created_dt = models.DateTimeField('Creation date', auto_now_add=True, editable=False)


class PostTag(ItemBase):
    content_object = models.ForeignKey('Post', on_delete=models.CASCADE)
    tag = models.ForeignKey(Topics, related_name="topic_items", on_delete=models.CASCADE)
    created_dt = models.DateTimeField('Creation date', auto_now_add=True, editable=False)


class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50) #title
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.') #요약인데 없어도됨....
    content = models.TextField('CONTENT') #content
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True, through=PostTag)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    scrap = models.ManyToManyField(get_user_model(), related_name='scrap_post', blank=True)
    #news id
    #press
    #url
    #category

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.id,))

    def get_prev(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

