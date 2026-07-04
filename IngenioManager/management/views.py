from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Ingenieur, Categorie
from .forms import IngenieurForm, CategorieForm, CustomUserCreationForm
from .utils import handle_create_form, handle_update_form, handle_delete, handle_list


def categorie(request):
    return handle_create_form(request, CategorieForm, 'categorie.html', 'categorie')


def categories(request):
    return handle_list(request, Categorie, 'categories.html', 'categ')


def modifyCategorie(request, id):
    return handle_update_form(
        request, Categorie, CategorieForm, id,
        'modif.html', 'categories',
        context={'Categorie': Categorie},
    )


def deleteCategorie(request, id):
    return handle_delete(request, Categorie, id, 'categories')


def ajout_Ingenieur(request):
    return handle_create_form(request, IngenieurForm, 'ingenieur.html', 'Ingenieur')


def liste_ingenieurs(request):
    return handle_list(request, Ingenieur, 'Ingenieurs.html', 'Ingenieurs')


def modifyIngenieur(request, id):
    return handle_update_form(
        request, Ingenieur, IngenieurForm, id,
        'modi_Ingenieur.html', 'liste_ingenieurs',
        context={'Ingenieur': Ingenieur},
    )


def deleteIngenieur(request, id):
    return handle_delete(request, Ingenieur, id, 'Ingenieurs')


def inscription(request):
    return handle_create_form(request, CustomUserCreationForm, 'inscription.html', 'connexion')


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')


def Accueil(request):
    return render(request, 'index.html')


def Dashboard(request):
    return render(request, 'dashboard.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')
