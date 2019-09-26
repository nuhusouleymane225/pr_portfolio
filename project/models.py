from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    tech = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Detail(models.Model): 
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    image_detail = models.ImageField(upload_to='media')
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    tech = models.CharField(max_length=255)
    statut = models.BooleanField(default=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


