# Generated by Django 4.1.2 on 2022-11-19 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_profile_id_profile'),
        ('profs', '0003_remove_prof_email_remove_prof_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]