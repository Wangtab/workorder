from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    role_choices = (('user', '员工'), ('leader', '领导'))
    role = models.CharField(verbose_name='角色', choices=role_choices, max_length=12)
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)

    def __str__(self):
        return self.username


class Template(models.Model):
    """模板表"""
    title = models.CharField(verbose_name="标题", max_length=32)
    leader = models.ForeignKey(verbose_name='审批者', to="UserInfo", on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Order(models.Model):
    """工单表"""
    user = models.ForeignKey(verbose_name="发起者", to='UserInfo', on_delete=models.CASCADE, related_name='users')
    tpl = models.ForeignKey(verbose_name="模板", to='Template', on_delete=models.CASCADE)
    leader = models.ForeignKey(verbose_name="审批者", to='UserInfo', on_delete=models.CASCADE, related_name='leaders')

    status = models.SmallIntegerField(verbose_name="状态", choices=((1, '待审批'), (2, '通过'), (3, '未通过')),default=1)
    create_datetime = models.DateTimeField(verbose_name="创建时间")
    update_datetime = models.DateTimeField(verbose_name="更新时间", null=True, blank=True)
