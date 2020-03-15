from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from unicode_tr.extras import slugify


class BlogPostCategories(models.Model):
    title = models.CharField(max_length=25, verbose_name='Blog Post Category', default='Uncategorized', unique=True)

    class Meta:
        verbose_name_plural = 'Blog Post Categories'
        verbose_name = 'Blog Post Category'

    def __str__(self):
        return self.title


class BlogPosts(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published Date', blank=True, null=True)
    category = models.ManyToManyField(BlogPostCategories)
    title = models.CharField(max_length=255, verbose_name='Blog Post Title', blank=True, null=True)
    featured_image = models.ImageField(verbose_name='Featured Image', blank=True, null=True)
    blog_keywords = models.CharField(max_length=255, verbose_name='Blog Post Meta Keywords')
    blog_description = RichTextField()
    summary = models.CharField(max_length=200, verbose_name="Blog Post Summary", blank=True, null=True, editable=False)

    class Meta:
        verbose_name_plural = "Blog Posts"
        verbose_name = "Blog Post"
        ordering = ["-created_at", "title"]

    def save(self, *args, **kwargs):
        if self.blog_description:
            self.summary = self.blog_description[:140]
        super(BlogPosts, self).save()

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'page_id': self.id, 'page_slug': slugify(self.title)})

    def __str__(self):
        return '{}'.format(self.title)
