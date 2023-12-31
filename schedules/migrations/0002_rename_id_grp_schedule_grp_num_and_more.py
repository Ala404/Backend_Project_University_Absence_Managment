# Generated by Django 4.1.2 on 2022-11-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profs', '0001_initial'),
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='id_grp',
            new_name='grp_num',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profs.prof'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id_sch',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
