# Generated by Django 2.2.10 on 2020-03-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0062_workflow_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='finished_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]