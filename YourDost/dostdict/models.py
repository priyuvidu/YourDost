from django.db import models



class Word(models.Model):
    word_title = models.CharField(max_length=200)

    def __str__(self):
        return self.word_title

# Create your models here.
