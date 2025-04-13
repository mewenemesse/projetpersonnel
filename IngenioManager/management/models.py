from django.db import models


# Create your models here.

class Categorie(models.Model):
    libeller = models.CharField(default=100)

    def __str__(self):
        return self.libeller

class Ingenieur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    niveaux_experience = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='ingenieurs')
    dteNaissance = models.DateField()
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)  
    mot_de_passe = models.CharField(max_length=50)



    



    
    