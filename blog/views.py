from django.shortcuts import render, get_object_or_404
import markdown

# Create your views here.
from comments.forms import CommentForm
from .models import Post, Category

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                  ])
    #在顶部导入CommentForm
    form = CommentForm()
    #获取这篇post的全部评论
    comment_list = post.comment_set.all()
    #将文章、表单以及文章下的评论列表作为模板变量传给detail.html模板，以便渲染响应数据
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})