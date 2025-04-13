

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- Importe RedirectView
from  .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    
    path('index', views.Accueil, name='acceuil'),
    
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    
    path('categorie/', views.categorie, name='categorie'),
    
    path('categories/', views.categories, name='categories'),
    
    path('Ingenieur/ajout/', views.ajout_Ingenieur, name='Ingenieur'),
    
    path('Ingenieur/liste/', views.liste_ingenieurs, name='liste_ingenieurs'),
    
    path('modifyCategorie/<int:id>/', views.modifyCategorie, name='modifyCategorie'),
    
    path('deleteCategorie<int:id>/', views.deleteCategorie, name='deleteCategorie'),
    
    path('modifyIngenieur/<int:id>/', views.modifyIngenieur, name='modifyIngenieur'),
    
    path('deleteIngenieur/<int:id>/', views.deleteIngenieur, name='deleteIngenieur'),
    
    path('inscription/', views.inscription, name='inscription'),
    
    path('', views.connexion, name='connexion'),
    
    
    path('deconnexion/', views.deconnexion, name='deconnexion'),

    
    # path('Sinscrire/', Sinscrire, name='Sinscrire'),
    
    # path('Se_connecter/', Se_connecter, name='Se_connecter'),
    
    # #c'est le lien qui condut vers la page de vent
    # path('vente/', views.vente, name='vente'),

    # #c'est le lien qui nous dirige vers la liste des vent 
    # path('liste_ventes/', views.liste_ventes, name='liste_ventes'),
    
    # #c'est le lien qui me condut vers la facture
    # path('voir_facture/', views.voir_facture, name='voir_facture'),
    
    # #c'est le lien qui me dirige vers la page de paiement
    # path('paiement/', views.paiement, name='paiement'),
]











