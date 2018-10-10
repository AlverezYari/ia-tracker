from django.db import models

class Question(models.campaign):
    campaign_name = models.CharField(max_length=200)
    last_saved = models.DateTimeField('date published')


class Choice(models.players):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create your models here.
