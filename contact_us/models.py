from django.db import models

class Contact(models.Model):
    nom     = models.CharField(max_length=200)
    email   = models.EmailField(max_length=100)
    objet   = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom