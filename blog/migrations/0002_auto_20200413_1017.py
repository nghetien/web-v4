# Generated by Django 3.0.5 on 2020-04-13 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=200)),
                ('date_comment', models.DateTimeField(auto_now_add=True, verbose_name='date comment')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='date change')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('name_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='imageblog',
            name='date_change',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='date change'),
        ),
        migrations.AddField(
            model_name='imageblog',
            name='date_post',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date post'),
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(max_length=200)),
                ('date_reply', models.DateTimeField(auto_now_add=True, verbose_name='date comment')),
                ('date_change', models.DateTimeField(auto_now=True, verbose_name='date change')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.CommentBlog')),
                ('email_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]