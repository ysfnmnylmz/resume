# Generated by Django 3.0.3 on 2020-03-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Full Name')),
                ('site_title', models.CharField(default='', max_length=255, verbose_name='Site Title')),
                ('site_description', models.TextField(verbose_name='Site Description')),
                ('meta_tags', models.TextField(help_text='Separate the words with a comma.', verbose_name='Site Meta Tags')),
                ('keywords', models.TextField(help_text='Separate the words with a comma.', verbose_name='Site Keywords')),
                ('favicon', models.FileField(blank=True, help_text='Icon size can be max 512x512', null=True, upload_to='', verbose_name='Site favicon')),
                ('site_logo', models.FileField(blank=True, help_text='Logo size max ...', null=True, upload_to='', verbose_name='Site Logo')),
            ],
            options={
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
    ]
