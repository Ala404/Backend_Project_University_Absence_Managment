# Generated by Django 4.1.2 on 2022-11-17 18:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id_mod',
            field=models.AutoField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]