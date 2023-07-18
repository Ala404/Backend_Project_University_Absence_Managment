# Generated by Django 4.1.2 on 2022-11-23 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0005_alter_section_id_sect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='id_sect',
            new_name='sect_num',
        ),
        migrations.RemoveField(
            model_name='group',
            name='id_grp',
        ),
        migrations.RemoveField(
            model_name='section',
            name='id_sect',
        ),
        migrations.AlterField(
            model_name='group',
            name='grp_num',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='sect_num',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]