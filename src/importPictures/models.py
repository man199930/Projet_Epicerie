from django.db import models

# Create your models here.
class Facture(models.Model):
    name=models.CharField(max_length=99)
    photo=models.ImageField(upload_to='factures') #factures est un repertoire qui sera cree dans media
