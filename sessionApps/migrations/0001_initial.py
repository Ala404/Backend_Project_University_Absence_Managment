# Generated by Django 4.1.2 on 2022-11-24 21:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('profs', '0001_initial'),
        ('modules', '0001_initial'),
        ('sections', '0001_initial'),
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionDate',
            fields=[
                ('id_date', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id_sess', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('sess_type', models.CharField(choices=[('td', 'td'), ('tp', 'tp'), ('cour', 'cour')], default='cour', max_length=5)),
                ('classroom', models.ForeignKey(default=110, on_delete=django.db.models.deletion.CASCADE, to='classrooms.classroom')),
                ('grp_num', models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='sections.group')),
                ('id_mod', models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='modules.module')),
                ('id_prof', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='profs.prof')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.schedule')),
                ('sect_num', models.ForeignKey(default=100, on_delete=django.db.models.deletion.CASCADE, to='sections.section')),
                ('sess_date', models.ForeignKey(default=1949, on_delete=django.db.models.deletion.CASCADE, to='sessionApps.sessiondate')),
            ],
        ),
    ]
