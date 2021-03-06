from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'training/index.html')


class PostList(ListView):
    model = Post
    template_name = 'training/post_list.html'


def post_delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post_list')


class PostDetail(DetailView):
    model = Post
    template_name = 'training/post_detail.html'
