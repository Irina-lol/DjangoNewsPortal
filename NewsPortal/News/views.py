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
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'


class ArticlesCreate(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'articles_create.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news.html')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('news.html')