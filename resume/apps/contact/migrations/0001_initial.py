# Generated by Django 3.0.3 on 2020-03-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.EmailField(max_length=254, verbose_name='mail')),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Social Media Name')),
                ('link', models.URLField(verbose_name='Social Media Profile Link')),
            ],
            options={
                'verbose_name': 'Social Media Account',
                'verbose_name_plural': 'Social Media Accounts',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Your Name', max_length=255, verbose_name='Name')),
                ('picture', models.FileField(upload_to='', verbose_name='Photo')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('location', models.CharField(blank=True, max_length=120, null=True, verbose_name='Location')),
                ('mails', models.ManyToManyField(to='contact.Mails')),
                ('social_media', models.ManyToManyField(to='contact.Social')),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Informations',
            },
        ),
    ]
