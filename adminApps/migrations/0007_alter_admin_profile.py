# Generated by Django 4.1.2 on 2022-11-19 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_id_profile'),
        ('adminApps', '0006_alter_admin_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
