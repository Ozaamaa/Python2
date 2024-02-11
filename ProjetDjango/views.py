from django.shortcuts import render, redirect
from .forms import SessionCoursForm
from .models import SessionCours

def creer_session(request):
    if request.method == 'POST':
        form = SessionCoursForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.lien_formulaire = f'http://127.0.0.1:5000/login'
            session.save()
            return redirect('liste_sessions')
    else:
        form = SessionCoursForm()
    return render(request, 'creer_session.html', {'form': form})

def liste_sessions(request):
    sessions = SessionCours.objects.all()
    return render(request, 'liste_sessions.html', {'sessions': sessions})