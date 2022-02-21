# Generated by Django 4.0.2 on 2022-02-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTodo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='createDate',
            new_name='createdDate',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='updateDate',
            new_name='updatedDate',
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('M', 'Medium'), ('L', 'Low'), ('H', 'High')], max_length=50),
        ),
    ]
