# Generated by Django 4.2.5 on 2023-10-03 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_rename_comment_discussioncomment_commentbody'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='status',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='submissions',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='type',
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('choices', models.TextField()),
                ('answer', models.CharField(max_length=100)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.assignment')),
            ],
        ),
    ]
