# Generated by Django 4.2.5 on 2023-11-26 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_alter_discussioncomment_commentbody_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='earned',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='possible',
        ),
        migrations.CreateModel(
            name='SubmissionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='', max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.multiplechoicequestion')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.submission')),
            ],
        ),
    ]
