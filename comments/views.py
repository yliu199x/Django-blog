from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #检查表单提交数据是否合法
        #数据合法
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        #数据不合法
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
        return render(request, 'blog/detail.html', context=context)
    #不是post请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)