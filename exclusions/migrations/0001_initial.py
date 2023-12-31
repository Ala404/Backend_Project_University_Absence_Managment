# Generated by Django 4.1.2 on 2022-11-24 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modules', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exclusion',
            fields=[
                ('id_exc', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('id_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.module')),
                ('id_stud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
