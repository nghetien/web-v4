# Generated by Django 3.0.5 on 2020-04-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200413_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentblog',
            old_name='email',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='replycomment',
            old_name='email_reply',
            new_name='author',
        ),
    ]
