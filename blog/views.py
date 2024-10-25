from django.db.models import F

from django.views.generic import ListView, DetailView

from blog.models import Post, Category, Tag, NetworkModel
from blog.services import get_paginated_posts, get_all_posts, get_posts_by_category, get_posts_by_tag, get_post_comments

from comments.forms import CommentForm


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lifeleck'

        big_post, other_posts = get_all_posts()
        other_posts_page = get_paginated_posts(self.request, other_posts, self.paginate_by)

        context['big_post'] = big_post
        context['other_posts'] = other_posts_page
        context['all_posts'] = Post.objects.all()
        return context


class GetByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'other_posts'
    paginate_by = 8

    def get_queryset(self):
        return get_posts_by_category(self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug']).title
        return context


class GetByTag(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'other_posts'
    paginate_by = 8

    def get_queryset(self):
        return get_posts_by_tag(self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу ::' + str(Tag.objects.get(slug=self.kwargs['slug']).title)
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'
    paginate_by = 8

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        else:
            user_id = -1

        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        post = self.object

        context.update(get_post_comments(post))
        context['comment_form'] = CommentForm()
        context['user_id'] = user_id
        return context


class CategoryMenu(ListView):
    model = Category
    template_name = 'blog/menu/category.html'
    context_object_name = 'categories'


class TagsMenu(ListView):
    model = Tag
    template_name = 'blog/menu/tags.html'
    context_object_name = 'tags'


class SocialNetwork(ListView):
    model = NetworkModel
    template_name = 'blog/menu/networks.html'
    context_object_name = 'networks'


class Search(ListView):
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = f"search={self.request.GET.get('search')}&"
        return context
