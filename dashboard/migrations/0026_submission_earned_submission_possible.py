# Generated by Django 4.2.5 on 2023-11-27 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_submissionanswer_possible'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='earned',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submission',
            name='possible',
            field=models.IntegerField(default=0),
        ),
    ]
