from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
        用户模型
        """
    username = models.CharField(max_length=30, unique=True, verbose_name="用户名")


    def __str__(self):
        return f"用户名: {str(self.username)}"

    class Meta:
        db_table = 'user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
