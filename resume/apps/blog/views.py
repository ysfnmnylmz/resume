from django.shortcuts import render, get_object_or_404
from .models import BlogPosts, BlogPostCategories
from resume.apps.contact.models import Contact


def blog_posts(request):
    posts = BlogPosts.objects.all()
    trends = BlogPosts.objects.all().order_by('-view')[:4]
    blog_categories = BlogPostCategories.objects.all()
    contact = Contact.objects.first()

    payload = {
        'posts': posts,
        'trends': trends,
        'contact': contact,
        'blog_categories': blog_categories,
    }
    return render(request, 'blog.list.html', payload)


def blog_detail(request, page_id=None, **kwargs):
    blog_post = get_object_or_404(BlogPosts, id=page_id)
    latest = BlogPosts.objects.first()
    posts = BlogPosts.objects.all()
    blog_categories = BlogPostCategories.objects.all()
    contact = Contact.objects.first()
    try:
        prev = get_object_or_404(BlogPosts, id=str(int(page_id) - 1))
    except:
        prev = None

    try:
        next = get_object_or_404(BlogPosts, id=str(int(page_id) + 1))
    except:
        next = None

    payload = {
        'contact': contact,
        'posts': posts,
        'latest': latest,
        'blog_post': blog_post,
        'blog_categories': blog_categories,
        'next': next,
        'prev': prev
    }
    try:
        blog_post.view += 1
        blog_post.save()
    except:
        pass
    return render(request, 'blog.details.html', payload)
