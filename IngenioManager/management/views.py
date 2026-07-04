from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST, require_http_methods
from .models import Ingenieur, Categorie
from .forms import IngenieurForm, CategorieForm, CustomUserCreationForm


@login_required
def categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categorie')
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
        return redirect('categories')

    return render(request, 'modif.html', {'form': form, 'Categorie': Categorie})


@login_required
@require_POST
def deleteCategorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    categorie.delete()
    return redirect('categories')


@login_required
def ajout_Ingenieur(request):
    if request.method == 'POST':
        form = IngenieurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ingenieur')
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
        return redirect('liste_ingenieurs')
    return render(request, 'modi_Ingenieur.html', {'form': form, 'Ingenieur': ingenieur})


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})


def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
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
    return redirect('Ingenieurs')


@login_required
def Accueil(request):
    return render(request, 'index.html')


@login_required
def Dashboard(request):
    return render(request, 'dashboard.html')


@require_POST
def deconnexion(request):
    logout(request)
    return redirect('connexion')



