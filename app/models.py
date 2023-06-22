from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    sex = models.CharField(max_length=1)
    tel = models.CharField(max_length=11)
    birth = models.DateField()
    address = models.CharField(max_length=50)
    specialize_id = models.IntegerField() # 专业
    def to_json(self):
        data = {
            "id": self.id,
            "name": self.name,
            "sex": self.sex,
            "tel": self.tel,
            "address": self.address,
            "birth": self.birth.strftime('%Y-%m-%d'),
            "specialize": self.specialize_id
        }
        return data
    class Meta():
        db_table = 'app_contact'
class Specialize(models.Model):
    specialize_id = models.IntegerField()
    specialize_name = models.CharField(max_length=50)
    academy_name = models.CharField(max_length=50)
    class Meta():
        db_table = 'app_specialize'
class User(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    identity = models.IntegerField() # 0 代表普通用户 1代表管理员
    class Meta():
        db_table = 'app_user'


