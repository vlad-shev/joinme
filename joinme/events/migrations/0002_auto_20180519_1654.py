# Generated by Django 2.0.1 on 2018-05-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(null=True, verbose_name='event date published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_location',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FilePathField(null=True, path='static/events/images'),
        ),
        migrations.AlterField(
            model_name='event',
            name='publication_date',
            field=models.DateTimeField(auto_now=True, verbose_name='post date published'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]