# Generated by Django 3.2.4 on 2021-06-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
