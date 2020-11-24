from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
JobTypes = [
    (0, '技术类'),
    (1, '产品类'),
    (2, 'Operation'),
    (3, 'Design')
]

Cities = [
    (0, '北京'),
    (1, '上海'),
    (2, 'Melbourne'),
    (3, 'Sydney'),
]

class Job(models.Model):

    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='职位类别')
    job_city = models.SmallIntegerField(blank=False, choices=Cities, verbose_name='City')
    job_name = models.CharField(max_length=255, blank=False, verbose_name='职位名称')
    job_responsibility = models.TextField(max_length=1024, verbose_name='Position')
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name='Responsibility')
    creator = models.ForeignKey(User, verbose_name='Creator', null=True, on_delete=models.SET_NULL)
    create_date = models.DateTimeField(verbose_name='创建日期', default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.job_name
