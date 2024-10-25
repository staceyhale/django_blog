from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Category, Tag
from comments.models import Comment


def get_paginated_posts(request, posts, per_page):
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page')

    try:
        posts_page = paginator.page(page)
    except PageNotAnInteger:
        posts_page = paginator.page(1)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)

    return posts_page


def get_all_posts():
    all_posts = Post.objects.all()
    big_post = all_posts.first()
    other_posts = all_posts.exclude(id=big_post.id)
    return big_post, other_posts


def get_posts_by_category(slug):
    return Post.objects.filter(category__slug=slug)


def get_posts_by_tag(slug):
    return Post.objects.filter(tags__slug=slug)


def get_post_comments(post):
    return {
        'comments': Comment.objects.filter(post=post, active=True, parents=None),
        'comments_total': Comment.objects.filter(post=post, active=True).count()
    }
