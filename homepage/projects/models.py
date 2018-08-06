from django.db import models

# Create your models here.

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_text = models.TextField()
    project_date = models.DateField('Date Finished')

    def __str__(self):
        return self.project_title
