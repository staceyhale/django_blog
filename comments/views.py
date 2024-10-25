from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from comments.forms import CommentForm
from comments.services import create_comment, delete_comment


@login_required
def create_comment_view(request):
    form = CommentForm(request.POST)
    if form.is_valid():
        create_comment(form, request)

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_comment_view(request):
    comment_id = request.POST.get('comment_id')
    delete_comment(comment_id, request)

    return redirect(request.META.get('HTTP_REFERER'))
