

# Create your models here.
from django.db import models

class Usermessage(models.Model):

    id=models.IntegerField(primary_key=True,db_column="Fld",default=10001)
    #object_id = models.CharField(primary_key=True, verbose_name="主键", max_length=50, default="")
    studend_name=models.CharField(max_length=50,verbose_name="姓名")
    studend_email=models.EmailField(max_length=50,verbose_name="邮箱")
    studend_address=models.CharField(max_length=100,verbose_name="地址信息")
    studend_phone=models.CharField(max_length=20,verbose_name="电话")

    class Meta:
        verbose_name = "用户留言信息"

