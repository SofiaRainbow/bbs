# Generated by Django 3.0.7 on 2020-06-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('status', models.SmallIntegerField(choices=[(0, '未审核'), (1, '已审核'), (2, '已下架')], default=0, verbose_name='状态')),
                ('read_count', models.IntegerField(default=0, verbose_name='阅读量')),
                ('comments', models.IntegerField(default=0, verbose_name='评论量')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.CategoryModel', verbose_name='分类')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
                'db_table': 'tb_article',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.ArticleModel', verbose_name='评论文章id')),
            ],
        ),
    ]
