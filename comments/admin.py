from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'profile', 'content',  'created_at',  'active')
    list_display_links = ('id', 'post', 'profile',)
    list_filter = ('created_at', 'profile', 'post', 'active')
    search_fields = ('created_at', 'profile', 'post', 'id', 'active')

