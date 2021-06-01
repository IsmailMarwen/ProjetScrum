from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    members = models.ManyToManyField(User)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Project(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class ProductBacklog(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name="projet")
    name = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Backlog de produit'
        verbose_name_plural = 'Backlogs de produit'

class Sprint(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()

class UserStory(models.Model):
    product_backlog = models.ForeignKey('ProductBacklog',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()