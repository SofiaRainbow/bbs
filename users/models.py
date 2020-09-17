from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    username = models.CharField(max_length=20, unique=True, verbose_name=_('用户名'))
    password = models.CharField(max_length=100, verbose_name=_('密码'))
    user_img = models.ImageField(upload_to='user', verbose_name=_('头像'), default='user')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'tb_user'
        verbose_name = _('用户管理')
        verbose_name_plural = verbose_name
