import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

# entity - models.Model 상속
class Todo(models.Model):

    
    city_choices={
        ('서울',"서울"),
        ('경기',"경기"),
        ('인천',"인천"),
        ('대전,충청',"대전,충청"),
        ('대구,경북',"대구,경북"),
        ('부산',"부산"),
        ('울산',"울산"),
        ('광주',"광주"),
    }

    level_choices={
        ("1~5(전체)","1~5(전체)"),
        ('1~2(초보)',"1~2(초보)"),
        ('3~4(중수)',"3~4(중수)"),
        ('5(고수)',"5(고수)"),
    }

    sex_choices={
        ('남녀모두',"남녀모두"),
        ('남자만',"남자만"),
        ('여자만',"여자만"),
    }

    time_choices={
        ('09:00','09:00'),
        ('11:00','11:00'),
        ("13:00","13:00"),
        ('15:00','15:00'),
        ('17:00','17:00'),
        ("19:00","19:00"),
        ('21:00','21:00'),
    }
    
    objects=models.Manager
    title=models.CharField(max_length=100)  #정확한 주소
    sex=models.CharField(max_length=80,choices=sex_choices,null=True)  #성별
    city=models.CharField(max_length=80,choices=city_choices,null=True)  #도시
    level=models.CharField(max_length=80,choices=level_choices,null=True)  #수준
    now_date = models.DateTimeField(auto_now_add=True)  #현재시간
    schedule = models.DateField(blank=True,null=True)  #일정
    number=models.IntegerField(default=0) #인원수
    time=models.CharField(max_length=80,choices=time_choices,null=True)  #도시
    user=models.CharField(max_length=100,null=True)
    
    apply = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True, related_name='apply') 

    def count_apply_user(self): # total likes_user
        return self.apply.count()

    def __str__(self):
        return self.title
    