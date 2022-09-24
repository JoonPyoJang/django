from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):  #유저모델 클래스 생성
    class Meta:                 #데이터 베이스의 정보?
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    