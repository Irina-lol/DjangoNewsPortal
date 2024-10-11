from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
nullfy_quantity.short_description = 'Убрать все посты'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating')
    list_filter = [field.name for field in Author._meta.get_fields()]


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post_type', 'title', 'rating')
    list_filter = [field.name for field in Post._meta.get_fields()]
    search_fields = ('author', 'post_type', 'title', 'category')
    actions = [nullfy_quantity]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'text', 'date_in', 'rating')
    list_filter = [field.name for field in Comment._meta.get_fields()]
    search_fields = ('user', 'text', 'date_in')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
