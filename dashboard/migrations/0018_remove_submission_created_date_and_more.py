# Generated by Django 4.2.5 on 2023-10-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_multiplechoicequestion_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='description',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='name',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='status',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='student',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='updated_date',
        ),
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