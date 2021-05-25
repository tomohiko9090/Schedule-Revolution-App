from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Oneteam_model(models.Model):
    お名前 = models.CharField(max_length=50)

    所属部署 = models.CharField(max_length=100)

    更新日 = models.DateField(auto_now_add=True)

    日曜日の予定 = models.TextField(blank=True)
    
    月曜日の予定 = models.TextField(blank=True)

    火曜日の予定 = models.TextField(blank=True)

    水曜日の予定 = models.TextField(blank=True)
 
    木曜日の予定 = models.TextField(blank=True)

    金曜日の予定 = models.TextField(blank=True)

    土曜日の予定 = models.TextField(blank=True)

    limit = [MinValueValidator(1), MaxValueValidator(6)]
    # タスクデータ
    task1 = models.CharField(max_length=50 ,blank=True)
    urgency_weight1 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight1 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight1 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight1 = models.IntegerField(null=True, blank=True, validators=limit)

    task2 = models.CharField(max_length=50 ,blank=True)
    urgency_weight2 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight2 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight2 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight2 = models.IntegerField(null=True, blank=True, validators=limit)

    task3 = models.CharField(max_length=50 ,blank=True)
    urgency_weight3 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight3 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight3 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight3 = models.IntegerField(null=True, blank=True, validators=limit)

    task4 = models.CharField(max_length=50 ,blank=True)
    urgency_weight4 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight4 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight4 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight4 = models.IntegerField(null=True, blank=True, validators=limit)

    task5 = models.CharField(max_length=50 ,blank=True)
    urgency_weight5 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight5 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight5 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight5 = models.IntegerField(null=True, blank=True, validators=limit)

    task6 = models.CharField(max_length=50 ,blank=True)
    urgency_weight6 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight6 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight6 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight6 = models.IntegerField(null=True, blank=True, validators=limit)

    task7 = models.CharField(max_length=50 ,blank=True)
    urgency_weight7 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight7 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight7 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight7 = models.IntegerField(null=True, blank=True, validators=limit)

    task8 = models.CharField(max_length=50 ,blank=True)
    urgency_weight8 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight8 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight8 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight8 = models.IntegerField(null=True, blank=True, validators=limit)

    task9 = models.CharField(max_length=50 ,blank=True)
    urgency_weight9 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight9 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight9 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight9 = models.IntegerField(null=True, blank=True, validators=limit)

    task10 = models.CharField(max_length=50 ,blank=True)
    urgency_weight10 = models.IntegerField(null=True, blank=True, validators=limit)
    importance_weight10 = models.IntegerField(null=True, blank=True, validators=limit)
    motivation_weight10 = models.IntegerField(null=True, blank=True, validators=limit)
    difficult_weight10 = models.IntegerField(null=True, blank=True, validators=limit)

    def __str__(self):
        return self.お名前


