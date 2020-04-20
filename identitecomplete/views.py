from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm



def home_view(request):


	return render(request, "index.html", locals())


def logout_view(request):
	logout(request)
	return redirect(home_view)


def login_view(request):
	connexion_form = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and connexion_form.is_valid():
		username = connexion_form.cleaned_data['username']
		password = connexion_form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		print(username, password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			messages.success(request, "You're now connected!")
			if next_p:
				return redirect(next_p)
			else:
				return redirect(home_view)
		else:
			messages.error(request, "Wrong password!")
	connexion_form = ConnexionForm()
	return render(request, 'sign_in.html', locals())


def register_view(request):
	inscription_form = InscriptionForm(request.POST, request.FILES)
	if request.method == "POST":
		if inscription_form.is_valid():
			firstname = inscription_form.cleaned_data['first_name']
			lastname = inscription_form.cleaned_data['last_name']
			username = inscription_form.cleaned_data['username']
			password = inscription_form.cleaned_data['password']
			password2 = inscription_form.cleaned_data['password2']
			email = inscription_form.cleaned_data['email']
			avatar = inscription_form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					email=email,
					password=password)
				user.first_name, user.last_name = firstname, lastname
				user.save()
				print(username, email, firstname, lastname, password)
				Profil(user=user, avatar=avatar).save()
				messages.success(request, "Hello "+username+", youn are registered successfully!")
				if user:
					login(request, user)
					return redirect(home_view)
	inscription_form = InscriptionForm()
	return render(request, 'register.html', locals())

@login_required
def document_view(request):
	documents_query = CompleteIdentity.objects.filter(user=request.user)
	return render(request, 'all_documents.html', locals());

@login_required
def cp_one_view(request, id):
	query_cp = get_object_or_404(CompleteIdentity, id=id)
	# Headers
	zone = get_object_or_404(Zone, name= query_cp.residence_zone)
	commune = zone.commune
	municipalite = commune.province

	#Zone_Leader
	zone_leader = get_object_or_404(ZoneLeader, zone_leaded=zone)

	#CNI_stuff

	CNI_query = get_object_or_404(CNI, CNI_number_CNI=query_cp.CNI_number_cp)
	print(CNI_query)
	return render(request, 'display_cp.html', locals())

@login_required
def complete_identity_view(request):
	cp_form = CompleteIdentityForm(request.POST)
	if request.method == "POST":
		if cp_form.is_valid():
			gender = cp_form.cleaned_data['gender']
			first_name_beneficiary = cp_form.cleaned_data['first_name_beneficiary']
			last_name_beneficairy = cp_form.cleaned_data['last_name_beneficairy']
			father_fullname_beneficiary = cp_form.cleaned_data['father_fullname_beneficiary']
			mother_fullname_benefiaciary = cp_form.cleaned_data['mother_fullname_benefiaciary']
			birth_zone = cp_form.cleaned_data['birth_zone']
			birth_year = cp_form.cleaned_data['birth_year']
			birth_commune = cp_form.cleaned_data['birth_commune']
			birth_province = cp_form.cleaned_data['birth_province']
			nationality = cp_form.cleaned_data['nationality']
			marital_status = cp_form.cleaned_data['marital_status']
			profession = cp_form.cleaned_data['profession']
			residence_zone = cp_form.cleaned_data['residence_zone']
			residence_quarter = cp_form.cleaned_data['residence_quarter']
			CNI_number_cp = cp_form.cleaned_data['CNI_number_cp']
			print(CNI_number_cp)
			try:
				CNI_query = CNI.objects.get(CNI_number_CNI=CNI_number_cp)
				print(CNI_query)
				print(CNI_query.CNI_number_CNI)
				CompleteIdentity.objects.create(
					user=request.user,
					gender = gender,
				 first_name_beneficiary = first_name_beneficiary,
				  last_name_beneficairy = last_name_beneficairy,
				   father_fullname_beneficiary = father_fullname_beneficiary,
				    mother_fullname_benefiaciary = mother_fullname_benefiaciary,
				     birth_zone = birth_zone,
				      birth_year = birth_year,
				       birth_commune = birth_commune, 
				       birth_province = birth_province, 
				       nationality = nationality, 
				       marital_status = marital_status, 
				       profession = profession, 
				       residence_zone = residence_zone, 
				       residence_quarter = residence_quarter, 
				       CNI_number_cp = CNI_number_cp
					).save()
				messages.success(request, "Formulaire envoyé")
				return redirect(document_view)
			except:
				messages.error(request, "Pas de carte d'identité portant le numero : "+CNI_number_cp+"")
				return redirect(home_view)
	cp_form = CompleteIdentityForm()
	return render(request, 'complete_identity_form.html', locals())
