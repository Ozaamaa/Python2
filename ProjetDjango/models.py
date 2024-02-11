from django.db import models

class SessionCours(models.Model):
    STATUT_CHOICES = [
        ('ouvert', 'Ouvert'),
        ('ferme', 'Fermé'),
    ]

    titre = models.CharField(max_length=255)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    lien_formulaire = models.URLField()
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='ouvert')
    heure_ouverture = models.TimeField(null=True, blank=True)
    heure_fermeture = models.TimeField(null=True, blank=True)