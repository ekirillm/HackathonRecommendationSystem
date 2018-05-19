from django.db import models


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Participant(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    key_skills = models.ManyToManyField(Skill)
    has_idea = models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
