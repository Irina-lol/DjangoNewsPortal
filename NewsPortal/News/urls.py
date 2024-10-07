from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, PostCreate, PostDelete, CategoryListView, subscribe, unsubscribe, \
   ProfileView, upgrade_me

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='newss'),
   path('search/', PostsSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_edit'),
   path('news/<int:pk>/update/', PostCreate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', PostCreate.as_view(), name='post_edit'),
   path('articles/<int:pk>/update/', PostCreate.as_view(), name='post_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('profile/', ProfileView.as_view(), name='profile'),
   path('profile/upgrade/', upgrade_me, name='upgrade'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe')
]