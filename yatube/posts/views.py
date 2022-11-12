# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

NUM_OF_POSTED_POSTS: int = 10


def index(request):
    """Возвращает главную страницу"""

    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.select_related('author')[:NUM_OF_POSTED_POSTS]
    context = {
        'title': title,
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Возвращает посты выбранной группы"""

    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = (group.posts.all()
             [:NUM_OF_POSTED_POSTS])
    title = str(group)
    context = {
        'title': title,
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
