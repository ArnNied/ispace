# Generated by Django 3.0.10 on 2020-11-07 14:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0006_auto_20201107_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='name',
            field=models.CharField(max_length=32, unique=True, validators=[django.core.validators.RegexValidator(' ', 'No spaces allowed', code='invalid_tag', inverse_match=True), django.core.validators.RegexValidator('^[a-zA-Z]+$', 'Lowercase and uppercase alphabet only', code='invalid_tag')], verbose_name="Hub's Name"),
        ),
    ]
