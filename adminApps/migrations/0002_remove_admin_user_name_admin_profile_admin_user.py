# Generated by Django 4.1.2 on 2022-11-17 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_first_name_remove_profile_last_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminApps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='user_name',
        ),
        migrations.AddField(
            model_name='admin',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
        migrations.AddField(
            model_name='admin',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
