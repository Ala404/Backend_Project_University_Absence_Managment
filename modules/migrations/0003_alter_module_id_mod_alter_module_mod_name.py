# Generated by Django 4.1.2 on 2022-11-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_alter_module_id_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id_mod',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='mod_name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
