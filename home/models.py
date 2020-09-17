from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# 模型对应数据库中的表
'''
class ModelName(models.Model):
    field_name = models.字段类型(字段选项)
'''


class CategoryModel(models.Model):
    # id字段是django自动添加的，是表的主键,可以不用手动添加
    # name即分类名称，CharField即字段类型,max_length即最大长度,unique即唯一的,分类名称不能重复
    # verbose_name主要用于admin后台展示使用
    name = models.CharField(max_length=20, unique=True, verbose_name=_('分类名'))
    # parent即分类的父级id,ForeignKey即外键,self即设置自关联,on_delete即设置外键的级联操作
    # null即允许数据库数据为null, blank主要是admin表单可以为空
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('上一级分类id'))

    # 实现__str__方法,方便在Admin后台站点显示
    def __str__(self):
        return self.name

    # 设置表选项信息
    class Meta:
        db_table = 'tb_category'  # 修改表名
        verbose_name = _('分类管理')  # 方便Admin后台站点显示
        verbose_name_plural = verbose_name
        # translatable_fields = "name"


class ArticleModel(models.Model):
    StatusEnum = (
        (0, _('未审核')),
        (1, _('已审核')),
        (2, _('已下架'))
    )
    title = models.CharField(max_length=50, verbose_name=_('标题'))
    content = models.TextField(verbose_name=_('内容'))
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, verbose_name=_('分类'))
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name=_('用户'))
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=_('发布日期'))
    status = models.SmallIntegerField(choices=StatusEnum, default=0, verbose_name=_('状态'))
    read_count = models.IntegerField(default=0, verbose_name=_('阅读量'))
    comments = models.IntegerField(default=0, verbose_name=_('评论量'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'
        verbose_name = _('文章管理')
        verbose_name_plural = verbose_name
        # translatable_fields = ("title", "content")


class CommentModel(models.Model):
    content = models.TextField(verbose_name='评论内容')
    article = models.ForeignKey(ArticleModel, on_delete=models.SET_NULL, null=True, verbose_name='评论文章id')

    class Meta:
        db_table = 'tb_comment'
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name


class Reply(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.SET_NULL, null=True, verbose_name=_('评论文章id'))
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name=_('用户'))
    # r_photo = models.CharField(verbose_name='回复的图片', max_length=128, null=True)
    r_time = models.DateTimeField(verbose_name=_('留言时间'), auto_now_add=True)
    r_content = models.CharField(verbose_name=_('回复内容'), max_length=256)

    def __str__(self):
        return self.r_content

    class Meta:
        db_table = 'tb_reply'
        verbose_name = _('回复管理')
        verbose_name_plural = verbose_name
        # translatable_fields = "r_content"
