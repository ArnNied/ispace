# Generated by Django 3.0.10 on 2020-11-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='This is my Bio', max_length=500, verbose_name="User's Bio"),
        ),
    ]
