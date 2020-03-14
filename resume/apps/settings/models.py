from django.db import models


class Settings(models.Model):
    title = models.CharField(max_length=255, verbose_name='Full Name', default='')
    site_title = models.CharField(max_length=255, verbose_name='Site Title', default='')
    site_description = models.TextField(verbose_name='Site Description')
    meta_tags = models.TextField(verbose_name='Site Meta Tags', help_text='Separate the words with a comma.')
    keywords = models.TextField(verbose_name='Site Keywords', help_text='Separate the words with a comma.')
    favicon = models.FileField(verbose_name='Site favicon', blank=True, null=True, help_text='Icon size can be max 512x512')
    site_logo = models.FileField(verbose_name='Site Logo', blank=True, null=True, help_text='Logo size max ...')

    class Meta:
        verbose_name = 'Site setting'
        verbose_name_plural = 'Site settings'

    def __str__(self):
        return '{} of {}'.format('Settings', self.title)
