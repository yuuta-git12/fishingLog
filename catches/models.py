from django.db import models


# Create your models here.
class Catch(models.Model):
    """釣果モデル"""
    users = models.CharField(max_length=10)  # 釣った人
    species = models.CharField(max_length=50)  # 釣った魚の種類
    size = models.FloatField()  # サイズ
    weight = models.FloatField()  # 重量
    date_caught = models.DateTimeField()  # 釣った日時
    location = models.CharField(max_length=100)  # 場所
    notes = models.TextField(blank=True, null=True)  # コメント
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)  # 写真1
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)  # 写真2
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)  # 写真3

    def __str__(self) -> str:
        return f"{self.species} - {self.size}cm - {self.weight}kg"
    
    
