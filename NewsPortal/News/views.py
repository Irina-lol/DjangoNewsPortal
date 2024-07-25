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
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)
        if self.request.path == "/news/create/": post.type = "NV"


class ArticlesCreate(CreateView):
    form_class = ArticlesForm
    model = Post
    template_name = 'arpost_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)
        if self.request.path == "/articles/create/":post.type = "AR"


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
