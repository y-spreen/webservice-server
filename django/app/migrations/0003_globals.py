# Generated by Django 2.2.6 on 2019-10-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191014_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Globals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gs_webhook_working', models.BooleanField(default=False)),
                ('gs_webhook_fired', models.BooleanField(default=False)),
            ],
        ),
    ]