# Generated by Django 2.2.8 on 2020-01-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_workflow_updated_resources'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='resource_exhaustion',
            field=models.BooleanField(default=False),
        ),
    ]
