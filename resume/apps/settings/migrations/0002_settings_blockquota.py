# Generated by Django 3.0.3 on 2020-03-17 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='blockquota',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Summary Resume'),
        ),
    ]
