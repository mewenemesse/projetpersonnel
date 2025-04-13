from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . models import Ingenieur, Categorie
from .forms import IngenieurForm, CategorieForm, CustomUserCreationForm


def categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST,request.FILES)
        if form.is_valid():
            cat = form.save()
            return redirect('categorie')
        else:
            print(form.errors)
            
    else: 
        form =CategorieForm()
    return render(request, 'categorie.html', {'form': form})


def categories(request):
    categorie = Categorie.objects.all()
    return render(request, 'categories.html', {'categ': categorie})


def modifyCategorie(request,id):
    
    categorie= Categorie.objects.get(id=id)
    form = CategorieForm(instance=categorie)
    if request.method == 'POST':
        form = CategorieForm(request.POST,instance=categorie )
        if form.is_valid():
            form.save()
        return redirect ('categories')

    return render (request, 'modif.html', {'form':form, 'Categorie':Categorie})


def deleteCategorie(request,id):
    categorie = Categorie.objects.get(id=id)
    categorie.delete()
    return redirect ('categories')
    



def ajout_Ingenieur(request):
    if request.method == 'POST':
        form = IngenieurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ingenieur')  # Vérifie que le nom est exactement celui défini dans urls.py
    else:
        form = IngenieurForm()
    return render(request, 'ingenieur.html', {'form': form})



def liste_ingenieurs(request):
    ingenieurs_list = Ingenieur.objects.all()
    return render(request, 'Ingenieurs.html', {'Ingenieurs': ingenieurs_list})


def modifyIngenieur(request,id):  
    ingenieur= Ingenieur.objects.get(id=id)
    form = IngenieurForm(instance=ingenieur)
    if request.method == 'POST':
        form = IngenieurForm(request.POST,instance=ingenieur )
        if form.is_valid():
            form.save()
        return redirect ('liste_ingenieurs')
    return render (request, 'modi_Ingenieur.html', {'form':form, 'Ingenieur':ingenieur})




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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')




def deleteIngenieur(request,id):
    ingenieur = Ingenieur.objects.get(id=id)
    ingenieur.delete()
    return redirect ('Ingenieurs')


def Accueil(request):
    return render(request, 'index.html')


def Dashboard(request):
    return render(request, 'dashboard.html')


def deconnexion(request):
    logout(request)
    return redirect('connexion')



