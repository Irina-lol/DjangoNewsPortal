from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, PostCreate, PostDelete


urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='newss'),
   path('search/', PostsSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_edit'),
   path('news/<int:pk>/edit/', PostCreate.as_view(), name='post_edit'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='post_edit'),
   path('articles/<int:pk>/edit/', PostCreate.as_view(), name='post_edit'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
