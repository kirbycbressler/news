# Generated by Django 3.2.6 on 2021-08-27 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Title',
            new_name='title',
        ),
    ]