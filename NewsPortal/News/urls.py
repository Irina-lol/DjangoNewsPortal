from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, NewsCreate, ArticlesCreate, NewsDelete, ArticlesDelete


urlpatterns = [
   path('<int:pk>', PostsList.as_view(), name='news'),
   path('<int:pk>', PostDetail.as_view(), name='newss'),
   path('search/', PostsSearch.as_view(), name='post_search'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('<int:pk>/news/delete/', NewsDelete.as_view(), name='news_delete'),
   path('<int:pk>/articles/delete/', ArticlesDelete.as_view(), name='articles_delete'),
]