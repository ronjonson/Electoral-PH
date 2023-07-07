from django.db import models

class Province(models.Model):
    Province = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.Province}"

class Candidate(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

class Reps_2004(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    electors = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}: {self.province} with {self.electors} electors"