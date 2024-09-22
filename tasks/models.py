from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='No description provided')
    priority = models.IntegerField()  # Ce champ doit exister dans votre modèle
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

