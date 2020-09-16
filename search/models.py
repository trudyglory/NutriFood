from django.db import models

# Create your models here.
class Produit(models.Model):
    name = models.Charfield(max_length=)
    Infos_produits 
    categories

class CustomUser(AbstractUser):
    pass
    # add additional fields in here

    def __str__(self):
        return self.username
    
class Compte(AbstractUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    mdp = 


class Infos_produits(models.Model):
    produit
    quantity = 
    repères_nutri = 
    nutriscore =


class Categories(models.Model):
    nom = models.CharField(max_length=128)
    Produit = 

class Mots_cles(models.Model):
    marque =
    categorie =
    pays_origine = 


class Image(models.Model):
    url_image = 
    url_image_s = 


#def __str__(self):
   # return self.ingredient

   git rm --cached projectname/settings.py
   git commit -m "remove settings.py"