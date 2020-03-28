from django.shortcuts import render
from django.http import HttpResponse
from resume.apps.portfolio.models import Portfolio, PortfolioCategories
from resume.apps.resume_app.models import Skills, Educations, Employments
from resume.apps.contact.models import Social, Mails, Contact
from resume.apps.blog.models import BlogPosts
from resume.apps.settings.models import Settings

from django.template.loader import get_template
from resume.utils import render_to_pdf
from django.views.generic import View


def home(request):
    portfolios = Portfolio.objects.all()
    skills = Skills.objects.all()
    educations = Educations.objects.all()
    employments = Employments.objects.all()
    contact = Contact.objects.first()
    portfolio_categories = PortfolioCategories.objects.all()
    latest = BlogPosts.objects.first()
    settings = Settings.objects.first()

    payload = {
        'settings': settings,
        'latest': latest,
        'portfolios': portfolios,
        'portfolio_categories': portfolio_categories,
        'skills': skills,
        'educations': educations,
        'employments': employments,
        'contact': contact,
    }
    return render(request, 'index.index.html', payload)


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('resume.html')
        portfolios = Portfolio.objects.all()
        skills = Skills.objects.all()
        educations = Educations.objects.all()
        employments = Employments.objects.all()
        contact = Contact.objects.first()
        portfolio_categories = PortfolioCategories.objects.all()
        latest = BlogPosts.objects.first()
        settings = Settings.objects.first()
        context = {
            'settings': settings,
            'latest': latest,
            'portfolios': portfolios,
            'portfolio_categories': portfolio_categories,
            'skills': skills,
            'educations': educations,
            'employments': employments,
            'contact': contact,
        }
        html = template.render(context)
        pdf = render_to_pdf('resume.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Yusuf-Numan-YILMAZ_CV.pdf"
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
