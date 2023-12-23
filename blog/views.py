from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request,'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост був створений успішно.')
            return redirect('posts')
        else:
            messages.error(request, 'Будь ласка, виправте помилки:')
            return render(request,'blog/post_form.html',{'form':form})

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')