from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

@python_2_unicode_compatible    
class Post(models.Model):
    #文章标题
    title = models.CharField(max_length=70)
    #文章正文
    body = models.TextField()
    #创建时间
    created_time = models.DateTimeField()
    #最后修改时间
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200, blank=True)
    #分类
    category = models.ForeignKey(Category)
    #标签
    tags = models.ManyToManyField(Tag, blank=True)
    #文章作者
    author = models.ForeignKey(User)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    #指定按照时间进行排序
    class Meta:
        ordering = ['-created_time']