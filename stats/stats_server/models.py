from django.db import models


# my data model
class BestScore(models.Model):
    username = models.CharField(max_length=200)
    best_score = models.CharField(max_length=200)
    objects = models.Manager()

    def update(self, best_score: str) -> None:
        self.best_score = best_score
        self.save()

    class Meta:
        ordering = ["best_score"]
        db_table = "Best_score"


class Stats(models.Model):
    username = models.CharField(max_length=200)
    all_levels = models.CharField(max_length=200)
    all_gold = models.CharField(max_length=200)
    enemies_killed = models.CharField(max_length=200)
    destroyed_obstacles = models.CharField(max_length=200)
    bosses_killed = models.CharField(max_length=200)
    devils_killed = models.CharField(max_length=200)
    fasts_killed = models.CharField(max_length=200)
    mutants_killed = models.CharField(max_length=200)
    ghosts_killed = models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        ordering = ["all_levels"]
        db_table = "Stats"

    def update(  # noqa: PLR0913
        self,
        all_levels: int,
        all_gold: int,
        enemies_killed: int,
        destroyed_obstacles: int,
        bosses_killed: int,
        devils_killed: int,
        fasts_killed: int,
        mutants_killed: int,
        ghosts_killed: int,
    ) -> None:
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
