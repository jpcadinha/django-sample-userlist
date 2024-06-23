from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=250)
    pub_date = models.DateTimeField("Date published")

    def __str__(self):
        return self.user
