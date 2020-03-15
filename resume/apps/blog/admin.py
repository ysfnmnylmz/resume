from django.contrib import admin
from resume.apps.blog.models import BlogPosts, BlogPostCategories


class BlogPostsAdmin(admin.ModelAdmin):
    class Meta:
        model = BlogPosts


class BlogPostCategoriesAdmin(admin.ModelAdmin):
    class Meta:
        model = BlogPostCategories


admin.site.register(BlogPosts, BlogPostsAdmin)
admin.site.register(BlogPostCategories, BlogPostCategoriesAdmin)
