from django.db import models
from django.contrib.auth.models import User

#my data model
class Best_score(models.Model):
    username =  models.CharField(max_length=200)
    best_score = models.CharField(max_length=200)
    objects = models.Manager()
    
    def update(self, best_score):
        self.best_score = best_score
        self.save()
        
    class Meta:
        ordering = ['best_score']
        db_table = 'Best_score'
        
class Stats(models.Model):
    username =  models.CharField(max_length=200)
    all_levels =  models.CharField(max_length=200)
    all_gold =  models.CharField(max_length=200)
    enemies_killed =  models.CharField(max_length=200)
    destroyed_obstacles =  models.CharField(max_length=200)
    bosses_killed =  models.CharField(max_length=200)
    devils_killed =  models.CharField(max_length=200)
    fasts_killed =  models.CharField(max_length=200)
    mutants_killed =  models.CharField(max_length=200)
    ghosts_killed =  models.CharField(max_length=200)
    objects = models.Manager()
    
    class Meta:
        ordering = ['username']
        db_table = 'Stats'
    
    def update(self,all_levels,all_gold,enemies_killed,destroyed_obstacles,
               bosses_killed,devils_killed,fasts_killed,mutants_killed,ghosts_killed):
        
        self.all_levels = all_levels
        self.all_gold = all_gold
        self.enemies_killed = enemies_killed
        self.destroyed_obstacles = destroyed_obstacles
        self.bosses_killed = bosses_killed
        self.devils_killed = devils_killed
        self.fasts_killed = fasts_killed
        self.mutants_killed = mutants_killed
        self.ghosts_killed = ghosts_killed
        self.save()
        

        