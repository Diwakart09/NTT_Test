from django.db import models

# Create your models here.



class router(models.Model):
    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14)
    loopback = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)
    #is_deleted = models.BooleanField(default=False)
