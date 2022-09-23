from django.db import models


# Create your models here.
class UserModel(models.Model):  #유저모델 클래스 생성
    class Meta:                 #데이터 베이스의 정보?
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)  
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)