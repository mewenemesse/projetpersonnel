from django.forms import ModelForm
from .models import Categorie, Ingenieur
from django.contrib.auth.forms import UserCreationForm, forms


class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"

class IngenieurForm(ModelForm):
    class Meta:
        model = Ingenieur
        fields = "__all__"
        
          
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")
        
        
        
        
        
