# Generated by Django 4.0.1 on 2022-01-24 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Student_List'},
        ),
        migrations.AlterModelTable(
            name='student',
            table='Student_Table',
        ),
    ]
