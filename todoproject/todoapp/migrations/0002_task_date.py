# Generated by Django 4.1.1 on 2023-03-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-10-12'),
            preserve_default=False,
        ),
    ]
