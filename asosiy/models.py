from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=40)
    sana = models.DateField()
    matn = models.TextField()
    rasm = models.FileField()

    def __str__(self):
        return self.sarlavha


class Intervyu(models.Model):
    sana =  models.DateField()
    sarlavha = models.CharField(max_length=40)
    video = models.CharField(max_length=70)
