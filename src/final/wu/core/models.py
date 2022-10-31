from django.db import models

class messageModel(models.Model):
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.title