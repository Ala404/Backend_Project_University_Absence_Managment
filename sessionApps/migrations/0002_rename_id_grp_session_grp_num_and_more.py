# Generated by Django 4.1.2 on 2022-11-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
        ('profs', '0001_initial'),
        ('sessionApps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='id_grp',
            new_name='grp_num',
        ),
        migrations.RenameField(
            model_name='session',
            old_name='type',
            new_name='sess_type',
        ),
        migrations.AddField(
            model_name='session',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classrooms.classroom'),
        ),
        migrations.AlterField(
            model_name='session',
            name='id_prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profs.prof'),
        ),
        migrations.AlterField(
            model_name='session',
            name='id_sess',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='sessiondate',
            name='id_sess',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessionApps.session'),
        ),
    ]
