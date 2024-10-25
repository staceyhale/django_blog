from django import template
from django.db.models import Count

from blog.models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/sidebar/popular_posts.html')
def get_popular_posts(posts_count=3):
    posts = Post.objects.order_by('-views')[:posts_count]
    return {"posts": posts}


@register.inclusion_tag('blog/sidebar/category_menu.html')
def show_category_menu():
    categories_with_counts = Category.objects.annotate(post_count=Count('posts'))
    return {"categories": categories_with_counts}


@register.inclusion_tag('blog/sidebar/tags_menu.html')
def show_tags_menu():
    tags_with_counts = Tag.objects.annotate(post_count=Count('posts'))
    return {"tags": tags_with_counts}

