from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=255, verbose_name='Home Full Name', default='')
    job_desc = models.TextField(verbose_name='Job Description', default='')
    home_title_1 = models.TextField(verbose_name='Home Title 1', default='')
    home_title_2 = models.TextField(verbose_name='Home Title 2', default='')
    home_title_3 = models.TextField(verbose_name='Home Title 3', default='')
    home_bg = models.ImageField(verbose_name='Home Backgroud IMG', blank=True, null=True)

    class Meta:
        verbose_name = 'Home Page Setting'
        verbose_name_plural = 'Home page Settings'

    def __str__(self):
        return '{} {}'.format('Home Page Details for', self.name)
