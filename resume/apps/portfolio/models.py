from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from unicode_tr.extras import slugify


class PortfolioCategories(models.Model):
    title = models.CharField(max_length=25, verbose_name='Portfolio Category', default='Uncategorized', unique=True)

    class Meta:
        verbose_name_plural = 'Protfolio Categories'
        verbose_name = 'Portfolio Category'

    def __str__(self):
        return self.title


class Techs(models.Model):
    title = models.CharField(max_length=25, verbose_name='Technology', default='Uncategorized', unique=True)

    class Meta:
        verbose_name = 'Tech'
        verbose_name_plural = 'Techs'

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    portfolio_type_choices = (
        ('Text', 'text'),
        ('Video', 'video'),
        ('Image', 'image'),
        ('Gallery', 'gallery'),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published Date', blank=True, null=True)
    category = models.ManyToManyField(PortfolioCategories)
    title = models.CharField(max_length=255, verbose_name='Protfolio Title One', blank=True, null=True)
    title_two = models.CharField(max_length=255, verbose_name='Portfolio Title Two', blank=True, null=True)
    portfolio_type = models.CharField(max_length=15, verbose_name='Portfolio Type', choices=portfolio_type_choices)
    featured_image = models.ImageField(verbose_name='Featured Image', blank=True, null=True)
    portfolio_video = models.URLField(verbose_name='Video Link', blank=True, null=True)
    portfolio_keywords = models.CharField(max_length=255, verbose_name='Portfolio Meta Keywords')
    portfolio_description = RichTextField()
    client = models.CharField(max_length=255, verbose_name='Client', blank=True, null='True')
    project_web = models.URLField(verbose_name='Project URL', blank=True, null=True)
    techs = models.ManyToManyField(Techs)
    summary = models.CharField(max_length=200, verbose_name="Duyuru Özet", blank=True, null=True, editable=False)

    class Meta:
        verbose_name_plural = "Portfolios"
        verbose_name = "Portfolio"
        ordering = ["-created_at", "title"]

    def save(self, *args, **kwargs):
        if self.portfolio_description:
            self.summary = self.portfolio_description[:140]
        super(Portfolio, self).save()

    def get_absolute_url(self):
        return reverse('portfolio:portfolio_detail', kwargs={'page_id': self.id, 'page_slug': slugify(self.title)})

    def __str__(self):
        return '{} {}'.format(self.title, self.title_two)

