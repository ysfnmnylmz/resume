# Generated by Django 3.0.3 on 2020-03-13 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_app', '0003_auto_20200314_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educations',
            name='finish_date',
            field=models.DateField(blank=True, help_text='If this field is left blank, it means that you are still studying.', null=True, verbose_name='Finish Date'),
        ),
        migrations.AlterField(
            model_name='employments',
            name='finish_date',
            field=models.DateField(blank=True, help_text='If this field is left blank, it means that you are still studying.', null=True, verbose_name='Finish Date'),
        ),
    ]
