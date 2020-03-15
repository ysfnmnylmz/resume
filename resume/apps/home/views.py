from django.shortcuts import render
from resume.apps.portfolio.models import Portfolio, PortfolioCategories
from resume.apps.resume_app.models import Skills, Educations, Employments
from resume.apps.contact.models import Social, Mails, Contact
from resume.apps.blog.models import BlogPosts


def home(request):
    portfolios = Portfolio.objects.all()
    skills = Skills.objects.all()
    educations = Educations.objects.all()
    employments = Employments.objects.all()
    contact = Contact.objects.first()
    portfolio_categories = PortfolioCategories.objects.all()
    latest = BlogPosts.objects.first()

    payload = {
        'latest': latest,
        'portfolios': portfolios,
        'portfolio_categories': portfolio_categories,
        'skills': skills,
        'educations': educations,
        'employments': employments,
        'contact': contact,
    }
    return render(request, 'index.index.html', payload)
