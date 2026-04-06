from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50) # تم تعديل الطول لـ 50 حسب اللاب
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1) # إضافة هذا الحقل الجديد

    def __str__(self):
        return self.title