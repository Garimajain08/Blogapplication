# Generated by Django 4.2.1 on 2023-06-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_blogmodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
