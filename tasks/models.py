from django.db import models

# Create your models here.
class Task(models.Model) :
    title = models.CharField(max_length=230)
    description = models.CharField(blank=True)
    done = models.BooleanField(default=False)

    def __str__(self) :
        return self.title