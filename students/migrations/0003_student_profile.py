# Generated by Django 4.1.2 on 2022-11-18 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_profile_profile_type'),
        ('students', '0002_remove_student_email_remove_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
