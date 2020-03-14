from django.db import models


class Mails(models.Model):
    title = models.EmailField(verbose_name='mail')

    class Meta:
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'
        ordering = ['title']

    def __str__(self):
        return self.title


class Social(models.Model):
    title = models.CharField(max_length=255, verbose_name='Social Media Name')
    link = models.URLField(verbose_name='Social Media Profile Link')

    class Meta:
        verbose_name = 'Social Media Account'
        verbose_name_plural = 'Social Media Accounts'

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', default='Your Name')
    picture = models.FileField(verbose_name='Photo')
    mails = models.ManyToManyField(Mails)
    phone = models.IntegerField(verbose_name='Phone')
    social_media = models.ManyToManyField(Social)
    location = models.CharField(max_length=120, verbose_name='Location',blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Information'
        verbose_name_plural = 'Contact Informations'

    def __str__(self):
        return self.name
