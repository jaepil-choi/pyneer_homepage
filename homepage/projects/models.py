from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    # 사진 ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)참
    image = models.ImageField(default="", blank=True)
    # 파일업로드
    file = models.FileField(upload_to='uploads', default="", blank=True)

    project_title = models.CharField(max_length=100)         # 프로젝트 제목
    project_shorten = models.TextField(default="", max_length=100)                     # 프로젝트 간략설명(2줄 이내)
    project_text = models.TextField()                        # 프로젝트 상세설명
    project_date = models.DateField('Date Finished')         # 프로젝트 날짜
    project_member = models.TextField(default="No one")      # 멤버 이름
    project_extra = models.TextField(default="", blank=True) # 기타정보
    project_year_semester = models.TextField()               # 년도-학기
    project_year = models.TextField()                        # 년도

    def project_year_semester(self):
        if self.project_date.month >= 1 & self.project_date.month <= 6:
            semester = 1
        elif self.project_date.month >= 7 & self.project_date.month <= 12:
            semester = 2
        else:
            semester = 3
        return str(self.project_date.year) + '-' + str(semester)

    def project_year(self):
        return str(self.project_date.year)

    def publish(self):
        self.project_date = timezone.now()
        self.save()

    def __str__(self):
        return self.project_title
