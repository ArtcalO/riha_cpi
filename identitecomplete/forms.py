from django import forms
from .models import *




class ConnexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe', 'type':'password','class':'form-control'}))

class InscriptionForm(forms.Form):
	username = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom utilisateur ','class':'form-control'}), label='username')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Mot de passe ','class':'form-control'}), label='password')
	password2 = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Confirmer ','class':'form-control'}), label='confirm password')
	


class CompleteIdentityForm(forms.ModelForm):
	CHOICES = (('0', '----------'),
				('1','ECOCASH'),
				('2','LUMICASH'))

	gender = forms.CharField(
				widget=forms.TextInput(
					attrs={
						'placeholder':'Genre : M ou F ',
						'class':'form-control'
						}
					),
				label='nom'
				)

	nationality = forms.CharField(
				widget=forms.TextInput(
					attrs={
						'placeholder':'Nationalité ',
						'class':'form-control'
						}
					),
				label='nationalite'
				)
	residence_zone = forms.CharField(
					widget=forms.TextInput(
						attrs={
							'placeholder':'Zone de résidance actuelle ',
							'class':'form-control'
							}
						),
					label='prenom'
					)

	residence_quarter = forms.CharField(
						widget=forms.TextInput(
							attrs={
								'placeholder':'Quartier de résidance actuelle ',
								'class':'form-control'
								}
							),
						label='prenom'
						)
	payement_method = forms.ChoiceField(
						widget=forms.Select(
							attrs={
								'placeholder':'Methode de payement',
								'class':'form-control'
								}
							),
						choices=CHOICES,
						label='payement_method'
						)
	trans_code = forms.CharField(
				widget=forms.TextInput(
					attrs={
						'placeholder':'Code de transaction',
						'class':'form-control'
						}
					),
				label='transaction_code'
				)
	# email = forms.EmailField( widget = forms.TextInput( attrs = {'placeholder':'Adresse electronique ','class':'form-control'} ), label='your email adress')
	# avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), label='Avatar')


	class Meta:
		model = CompleteIdentity
		fields = ("gender","nationality","residence_zone","residence_quarter","payement_method","trans_code")

class RegisterCNIForm(forms.Form):
	first_name_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom ','class':'form-control'}), label='nom')
	last_name_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Prenom ','class':'form-control'}), label='prenom')
	father_fullname_CNI =  forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom du père ','class':'form-control'}), label='father_name')
	mother_fullname_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Nom de la mère ','class':'form-control'}), label='mother_name')
	birth_province_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Province de naissance ','class':'form-control'}), label='province_birth')
	birth_commune_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Commune de naissance ','class':'form-control'}), label='communde_birth')
	birth_zone_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Zone de naissance ','class':'form-control'}), label='province_birth')
	birthday_CNI = forms.DateField(widget = forms.SelectDateWidget(years = range(1950, 2020), attrs={'placeholder':'yyy-mm-dd','class':'form-control inline-forms-control'}),label='Birthday')
	marital_status_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Etat-civil ','class':'form-control'}), label='marital_status')
	kind_of_work_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Profession ','class':'form-control'}), label='province_birth')
	CNI_number_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Numéro CNI ','class':'form-control'}), label='CNI_number')
	delivered_date_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Date de livraison ','class':'form-control'}), label='delivered_date')
	delivered_zone_CNI = forms.CharField( widget=forms.TextInput(attrs={'placeholder':'Zone de livraison ','class':'form-control'}), label='delivered_zone')

class CNIPicsForm(forms.Form):
	recto_CNI_pic = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'Recto CNI','class': 'form-control'}), label='Recto CNI')
	verso_CNI_pic = forms.ImageField(widget=forms.FileInput(attrs={'placeholder':'Verso CNI','class': 'form-control'}), label='Verso CNI')