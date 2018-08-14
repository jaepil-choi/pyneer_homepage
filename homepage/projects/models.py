from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_text = models.TextField()
    project_date = models.DateField('Date Finished')
    # 멤버 이름
    project_member = models.TextField(default="No one")
    # 기타정보
    project_extra = models.TextField(default=" ")
    # 년도-학기
    project_year_semester = models.TextField()
    # 년도
    project_year = models.TextField()

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
