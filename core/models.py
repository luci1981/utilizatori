from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    number_of_login = models.IntegerField()

    def __str__(self):
        return self.first_name +' '+ self.last_name

    class Meta:
        verbose_name_plural = 'Utilizatori'