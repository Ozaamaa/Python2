from django import forms
from .models import SessionCours

class SessionCoursForm(forms.ModelForm):
    class Meta:
        model = SessionCours
        fields = ['titre', 'date_debut', 'date_fin', 'statut', 'heure_ouverture', 'heure_fermeture']