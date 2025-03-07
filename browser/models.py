from django.db import models
from django.contrib.auth.models import User

# La classe HistoriqueDeRecherche sera représenté par une table dans la base de données.
# Chaque instance de cette classe sera une nouvelle ligne (row) dans la table.
# Chaque attribut de cette classe sera une colonne dans la table.

class HistoriqueDeRecherche(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # Si l'utilisateur est supprimé, son historique aussi
    url = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    liens_internes = models.IntegerField(default=0)
    liens_externes = models.IntegerField(default=0)
    images = models.IntegerField(default=0)
    tableaux = models.IntegerField(default=0)

    def __str__(self):
       return f"{self.utilisateur.username} - {self.url}"  # Affichage de l'url dans l'admin Django
