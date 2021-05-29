# Generated by Django 3.2.2 on 2021-05-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20210523_0553"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default="test", max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=250),
        ),
    ]
