from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, NewsCreate, ArticlesCreate, NewsDelete, ArticlesDelete


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='newss'),
   path('search/', PostsSearch.as_view(), name='post_search'),
   path('news/create/', NewsCreate.as_view(), name='post_edit'),
   path('news/<int:pk>/edit/',NewsCreate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
   path('articles/create/', ArticlesCreate.as_view(), name='arpost_edit'),
   path('articles/<int:pk>/edit/', ArticlesCreate.as_view(), name='arpost_edit'),
   path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='post_delete'),
]
