# Generated by Django 2.2.8 on 2020-02-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_auto_20200224_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='no_extract',
            field=models.BooleanField(default=False),
        ),
    ]
