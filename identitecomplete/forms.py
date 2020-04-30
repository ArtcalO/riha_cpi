from django import forms
from .models import *



class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
	first_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom ','class':'form-control'}), label='nom')
	last_name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Prenom ','class':'form-control'}), label='prenom')
	username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}), label='username')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe ','class':'form-control'}), label='password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirmer ','class':'form-control'}), label='confirm password')
	email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Adresse electronique ','class':'form-control'} ), label='your email adress')
	avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Avatar')


class CompleteIdentityForm(forms.Form):
	gender = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Genre : M ou F ','class':'form-control'}), label='nom')
	nationality = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationalité ','class':'form-control'}), label='nationalite')
	residence_zone = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Zone de résidance actuelle ','class':'form-control'}), label='prenom')
	residence_quarter = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Quartier de résidance actuelle ','class':'form-control'}), label='prenom')
	CNI_number_cp = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Numéro CNI ','class':'form-control'}), label='cni')

