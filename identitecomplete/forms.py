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
	first_name_beneficiary = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom ','class':'form-control'}), label='nom')
	last_name_beneficairy = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Prenom ','class':'form-control'}), label='prenom')
	father_fullname_beneficiary = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom du Père ','class':'form-control'}), label='nom père')
	mother_fullname_benefiaciary = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom Mere ','class':'form-control'}), label='nom mère')
	birth_zone = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Colline de naissance ','class':'form-control'}), label='colline')
	birth_year = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Année de naissance','class':'form-control'}), label='année_naissance')
	birth_commune = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Commune de naissance ','class':'form-control'}), label='commune')
	birth_province = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Province de naissance ','class':'form-control'}), label='province')
	nationality = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nationalité ','class':'form-control'}), label='nationalite')
	marital_status = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Etat-civil ','class':'form-control'}), label='etat-civil')
	profession = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Profession ','class':'form-control'}), label='profession')
	residence_zone = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Zone de résidance actuelle ','class':'form-control'}), label='prenom')
	residence_quarter = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Quartier de résidance actuelle ','class':'form-control'}), label='prenom')
	CNI_number_cp = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Numéro CNI ','class':'form-control'}), label='cni')

	# first_name_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Non CNI ','class':'form-control'}), label='prenom_cni')
	# last_name_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Prenom CNI ','class':'form-control'}), label='prenom')
	# father_fullname_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom du Père CNI ','class':'form-control'}), label='nom_père_cni')
	# mother_fullname_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom Mere CNI ','class':'form-control'}), label='nom mère_cni')
	# province_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Province de naissance CNI ','class':'form-control'}), label='province_cni')
	# commune_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Commune de naissance CNI ','class':'form-control'}), label='commune_cni')
	# birth_zone_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Colline de naissance CNI ','class':'form-control'}), label='colline_cni')
	# birthday_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Date Naissance CNI','class':'form-control'}), label='date_naissance')
	# marital_status_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Etat-civil CNI ','class':'form-control'}), label='etat-civil_cni')
	# kind_of_work_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Fonction ','class':'form-control'}), label='fonction')
	# CNI_number_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Numéro CNI ','class':'form-control'}), label='etat-civil')
