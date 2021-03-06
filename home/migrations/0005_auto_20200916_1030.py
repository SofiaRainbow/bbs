# Generated by Django 3.1 on 2020-09-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200907_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='name_en',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='分类名'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='name_ja',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='分类名'),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='name_zh_hans',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='分类名'),
        ),
    ]
