# Generated by Django 3.1 on 2020-09-07 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'verbose_name': '评论管理', 'verbose_name_plural': '评论管理'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': '回复管理', 'verbose_name_plural': '回复管理'},
        ),
        migrations.AlterModelTable(
            name='commentmodel',
            table='tb_comment',
        ),
        migrations.AlterModelTable(
            name='reply',
            table='tb_reply',
        ),
    ]
