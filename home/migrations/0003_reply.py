# Generated by Django 3.1 on 2020-09-06 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0002_articlemodel_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_time', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
                ('r_content', models.CharField(max_length=256, verbose_name='回复内容')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.articlemodel', verbose_name='评论文章id')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.user', verbose_name='用户')),
            ],
        ),
    ]