import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .filters import PostFilter
from .models import Post, Category, Author
from .forms import NewsForm
from .tasks import inform_about_new_posts


@cache_page(60 * 5)
def my_view(request):
    ...

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

    def get_object(self, *args, **kwargs):
        print(self.request.user.id)
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)

        return obj


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


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('News.add_post')
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        author = Author.objects.get(user=self.request.user)
        form.instance.author = self.request.user.author
        today = datetime.now()
        limit = today - datetime.timedelta(days=1)
        count = Post.objects.filter(author=author, date_published__gte=limit).count()
        if self.request.path == "/articles/create/":
            post.type = "AR"
        if count >= 3:
            return render(self.request, "post_create_limit.html")
        post.save()
        inform_about_new_posts.delay(post.pk)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_title"] = self.get_type()["title"]
        context["get_header"] = self.get_type()["header"]
        return context

    def get_type(self):
        if self.request.path == "/articles/create/":
            return {"title": ("Создать статью"), "header": ("Добавить статью")}
        else:
            return {"title": ("Создать новость"), "header": ("Добавить новость")}


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('News.change_post',)
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('News.delete_post')
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_not_author"] = not self.request.user.groups.filter(name="authors").exists()
        return context


class CategoryListView(PostsList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('-date_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.remove(user)

    message = ("Вы успешно отписались от рассылку категории")
    return render(request, "subscribe.html", {"category": category, "message": message})


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name="authors")
    if not request.user.groups.filter(name="authors").exists():
        authors_group.user_set.add(user)
        Author.objects.create(user=user)
    return redirect("/news/profile/")





