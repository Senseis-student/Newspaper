# Generated by Django 3.2 on 2021-06-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='section_post',
            field=models.ManyToManyField(to='blog.Section'),
        ),
    ]
