import os
import random

from django.db import models

#dossier de stockage des images
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "galerie/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename)

class Galerie(models.Model):
    name  = models.CharField(max_length=200)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def __str__(self):
        return 

