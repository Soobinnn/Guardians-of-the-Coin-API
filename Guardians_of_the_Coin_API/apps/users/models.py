from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(db_index=True, max_length=255, unique=True)
    name = models.CharField(max_length=128, null=True, default='')
    nick_name = models.CharField(db_index=True, max_length=255, unique=True, null=True, default='')
 
    class Meta:
        db_table = "User" #Table이름을 "User"로 정한다 default 이름은 api_user_user가 된다.
 
class Config(models.Model):
    UPBIT = 'UB'
    BYBIT = 'BB'
    EXCHANGE_CHOICES = [
        (UPBIT, 'upbit'),
        (BYBIT, 'bybit'),
    ]
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    exchange = models.CharField(
        max_length=2,
        choices=EXCHANGE_CHOICES,
        default=BYBIT
    )
    access_key = models.CharField(db_index=True, max_length=255, unique=True)
    