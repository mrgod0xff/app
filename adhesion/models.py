from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Adhesion(models.Model):
    nom_complet  = models.CharField(max_length=200)
    phone_regex  = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Le numéro de téléphone doit être entré au format: '+22587147883'. le code pays(+225) suivi de votre numero.")
    numero_de_telephone = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    date_de_naissance = models.DateField()
    email = models.EmailField(max_length=100)
    domicile = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    commune = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    quartier = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_complet
