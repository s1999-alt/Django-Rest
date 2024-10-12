from django.db import models



class Team(models.Model):
  team_name = models.CharField(max_length=50)

  def __str__(self):
    return self.team_name



class Person(models.Model):
  name = models.CharField(max_length=50)
  age = models.IntegerField()
  location = models.CharField(max_length=50)
  team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="members")

  def __str__(self):
    return self.name
  
  
