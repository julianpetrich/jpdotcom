# Generated by Django 3.2.2 on 2021-05-23 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.TextField(null=True),
        ),
    ]
