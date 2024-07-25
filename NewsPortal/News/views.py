from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .filters import PostFilter
from .models import Post
from .forms import NewsForm, ArticlesForm

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-date_in'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_count'] = self.get_queryset().count()
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'newss.html'
    context_object_name = 'newss'


class PostsSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qsfrom django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .filters import PostFilter
from .models import Post
from .forms import NewsForm, ArticlesForm

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-date_in'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_count'] = self.get_queryset().count()
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'newss.html'
    context_object_name = 'newss'


class PostsSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qsfrom django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .filters import PostFilter
from .models import Post
from .forms import NewsForm, ArticlesForm

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = '-date_in'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_count'] = self.get_queryset().count()
        return context



class PostDetail(DetailView):
    model = Post
    template_name = 'newss.html'
    context_object_name = 'newss'


class PostsSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
