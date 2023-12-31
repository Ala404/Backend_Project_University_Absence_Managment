# Generated by Django 4.1.2 on 2022-11-23 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_rename_id_sect_group_sect_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='sect_num',
            new_name='id_sect',
        ),
        migrations.AddField(
            model_name='group',
            name='id_grp',
            field=models.AutoField(default=1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='section',
            name='id_sect',
            field=models.AutoField(default=1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='grp_num',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='sect_num',
            field=models.IntegerField(unique=True),
        ),
    ]
