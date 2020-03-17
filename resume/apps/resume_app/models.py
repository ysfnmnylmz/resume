from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Employments(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateField(verbose_name='Start Date')
    finish_date = models.DateField(verbose_name='Finish Date', blank=True, null=True,
                                   help_text='If this field is left blank, it means that you are still working this corporate.')
    co_name = models.CharField(max_length=255, verbose_name='Corporate Name')
    job_title = models.CharField(max_length=255, verbose_name='Job Title')
    job_description = models.CharField(max_length=255, verbose_name='Job Description')

    class Meta:
        verbose_name = 'Employment'
        verbose_name_plural = 'Employments'
        ordering = ['-start_date']

    def __str__(self):
        return "{} --> {}".format(self.co_name, self.job_title)


class Educations(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    start_date = models.DateField(verbose_name='Start Date')
    finish_date = models.DateField(verbose_name='Finish Date', blank=True, null=True,
                                   help_text='If this field is left blank, it means that you are still studying.')
    institute_name = models.CharField(max_length=255, verbose_name='Institute Name')
    institute_stage = models.CharField(max_length=255, verbose_name='Institute Stage')

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ['-start_date']

    def __str__(self):
        return "{} --> {}".format(self.institute_name, self.institute_stage)


class Skills(models.Model):
    name = models.CharField(max_length=255, verbose_name='Skill Title')
    progress = models.PositiveIntegerField(verbose_name='Skill Percent',
                                           validators=[MinValueValidator(1), MaxValueValidator(100)],
                                           help_text='Max Value = 100, Min Value= 1')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name
