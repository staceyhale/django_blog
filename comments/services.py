from django.shortcuts import get_object_or_404
from blog.models import Post
from comments.models import Comment


def create_comment(form, request):
    comment = form.save(commit=False)
    post = Post.objects.filter(id=form.data['post_id']).first()
    if post is None:
        raise Exception('Post not found')
    comment.post = post
    comment.profile = request.user.userprofile
    comment.save()
    return comment


def delete_comment(comment_id, request):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.profile.user:
        comment.delete()
    return comment
