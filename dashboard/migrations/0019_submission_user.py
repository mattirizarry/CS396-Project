# Generated by Django 4.2.5 on 2023-10-04 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_submission_created_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
