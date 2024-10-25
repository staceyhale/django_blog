from django import template
from django.db.models import Count

from blog.models import Post

register = template.Library()


@register.inclusion_tag('blog/most_commented_posts.html')
def show_most_commented_posts(posts_count=3):
    most_commented_posts = Post.objects.all().annotate(comment_count=Count('comments')).order_by(
        '-comment_count')[:posts_count]
    return {'posts_with_most_comments': most_commented_posts}
