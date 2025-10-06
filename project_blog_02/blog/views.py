from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.utils import timezone
from django.db.models import Q

from .models import Post, Category

POSTS_LIMIT = 5

def _published_queryset():
    return (Post.objects.select_related('author', 'location', 'category')
            .filter(is_published=True, pub_date__lte=timezone.now())
            .filter(Q(category__isnull=True) | Q(category__is_published=True)))


def index(request):
    template = 'blog/index.html'
    post_list = _published_queryset()[:POSTS_LIMIT]
    return render(request, template, {'post_list': post_list})


def post_detail(request, post_id):

    post = get_object_or_404(_published_queryset(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):

    category = get_object_or_404(Category, slug=category_slug)

    if not category.is_published:
        raise Http404('Категория не опубликована')

    post_list = _published_queryset().filter(category=category)
    return render(
        request, 'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
