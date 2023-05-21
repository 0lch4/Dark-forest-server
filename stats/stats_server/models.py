from django.db import models
from django.contrib.auth.models import User

class Stats(models.Model):
    username =  models.CharField(max_length=200)
    best_score = models.CharField(max_length=200)
    objects = models.Manager()
    
    def update(self, best_score):
        self.best_score = best_score
        self.save()