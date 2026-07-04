import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Ingenieur, Categorie
from .forms import IngenieurForm, CategorieForm, CustomUserCreationForm

logger = logging.getLogger(__name__)


@login_required
def categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie créée avec succès.')
            return redirect('categorie')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = CategorieForm()
    return render(request, 'categorie.html', {'form': form})


@login_required
def categories(request):
    categorie = Categorie.objects.all()
    return render(request, 'categories.html', {'categ': categorie})


@login_required
def modifyCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    form = CategorieForm(instance=categorie)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie modifiée avec succès.')
            return redirect('categories')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    return render(request, 'modif.html', {'form': form, 'Categorie': Categorie})


@login_required
@require_POST
def deleteCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    categorie.delete()
    messages.success(request, 'Catégorie supprimée avec succès.')
    return redirect('categories')
    



@login_required
def ajout_Ingenieur(request):
    if request.method == 'POST':
        form = IngenieurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingénieur ajouté avec succès.')
            return redirect('Ingenieur')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = IngenieurForm()
    return render(request, 'ingenieur.html', {'form': form})



@login_required
def liste_ingenieurs(request):
    ingenieurs_list = Ingenieur.objects.all()
    return render(request, 'Ingenieurs.html', {'Ingenieurs': ingenieurs_list})


@login_required
def modifyIngenieur(request, id):
    ingenieur = get_object_or_404(Ingenieur, id=id)
    form = IngenieurForm(instance=ingenieur)
    if request.method == 'POST':
        form = IngenieurForm(request.POST, instance=ingenieur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingénieur modifié avec succès.')
            return redirect('liste_ingenieurs')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    return render(request, 'modi_Ingenieur.html', {'form': form, 'Ingenieur': ingenieur})




def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie. Vous pouvez maintenant vous connecter.')
            return redirect('connexion')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})



def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if not username or not password:
            messages.error(request, 'Veuillez remplir tous les champs.')
            return render(request, 'connexion.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')




@login_required
@require_POST
def deleteIngenieur(request, id):
    ingenieur = get_object_or_404(Ingenieur, id=id)
    ingenieur.delete()
    messages.success(request, 'Ingénieur supprimé avec succès.')
    return redirect('liste_ingenieurs')


@login_required
def Accueil(request):
    return render(request, 'index.html')


@login_required
def Dashboard(request):
    return render(request, 'dashboard.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')



