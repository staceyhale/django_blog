from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post, NetworkModel


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ["title"]}
    save_on_top = True
    save_as = True
    list_display = ('id', 'title', 'category', 'author', 'get_photo', 'views', 'created_at',)
    list_display_links = ('title', 'id')
    list_filter = ('title', 'category', 'created_at')
    fields = ('title', 'slug', 'content', 'photo', 'get_photo', 'views', 'created_at', 'category', 'tags', 'author')
    readonly_fields = ('views', 'created_at', 'get_photo')
    search_fields = ('title', 'content')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="70">')
        return '-'

    get_photo.short_description = 'фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(NetworkModel)
class NetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'icon_class', 'url')
    list_display_links = ('id', 'title', 'icon_class')



