# Generated by Django 4.2.5 on 2023-10-03 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_remove_discussionpost_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussioncomment',
            old_name='comment',
            new_name='commentBody',
        ),
    ]
