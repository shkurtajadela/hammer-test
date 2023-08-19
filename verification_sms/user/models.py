from django.db import models

# Create your models here.
class Phone(models.Model):
    phone_number = models.CharField(max_length=13, blank=False)
    generated_code = models.CharField(max_length=6, blank=False)
    invitation_code = models.CharField(max_length=6, blank=True)
    friends_number = models.ManyToManyField('self', blank=True, symmetrical=False)
    login_code = models.CharField(max_length=4, blank=False)

    def __str__(self) -> str:
        return self.phone_number
