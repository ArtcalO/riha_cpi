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
	return render(request, 'all_forms.html', locals())


def register_view(request):
	inscription_form = InscriptionForm(request.POST, request.FILES)
	if request.method == "POST":
		if inscription_form.is_valid():
			username = inscription_form.cleaned_data['username']
			password = inscription_form.cleaned_data['password']
			password2 = inscription_form.cleaned_data['password2']
			if password==password2:
				user = User.objects.create_user(
					username=username,
					password=password)
				user.save()
				Profil(user=user).save()
				messages.success(request, "Hello "+username+", youn are registered successfully!")
				if user:
					login(request, user)
					return redirect(register_CNI)
	inscription_form = InscriptionForm()
	return render(request, 'all_forms.html', locals())

@login_required
def register_CNI(request):
	register_cni_form = RegisterCNIForm(request.POST, request.FILES)
	if request.method == "POST":
		if register_cni_form.is_valid():
			first_name_CNI = register_cni_form.cleaned_data['first_name_CNI'] 
			last_name_CNI = register_cni_form.cleaned_data['last_name_CNI'] 
			father_fullname_CNI = register_cni_form.cleaned_data['father_fullname_CNI'] 
			mother_fullname_CNI = register_cni_form.cleaned_data['mother_fullname_CNI'] 
			birth_province_CNI = register_cni_form.cleaned_data['birth_province_CNI'] 
			birth_commune_CNI = register_cni_form.cleaned_data['birth_commune_CNI'] 
			birth_zone_CNI = register_cni_form.cleaned_data['birth_zone_CNI'] 
			birthday_CNI = register_cni_form.cleaned_data['birthday_CNI'] 
			marital_status_CNI = register_cni_form.cleaned_data['marital_status_CNI'] 
			kind_of_work_CNI = register_cni_form.cleaned_data['kind_of_work_CNI'] 
			CNI_number_CNI = register_cni_form.cleaned_data['CNI_number_CNI'] 
			delivered_date_CNI = register_cni_form.cleaned_data['delivered_date_CNI'] 
			delivered_zone_CNI = register_cni_form.cleaned_data['delivered_zone_CNI']

			
			new_CNI_obj = CNI.objects.create(	user = request.user,
												first_name_CNI = first_name_CNI,
												last_name_CNI = last_name_CNI,
												father_fullname_CNI = father_fullname_CNI,
												mother_fullname_CNI = mother_fullname_CNI,
												birth_province_CNI = birth_province_CNI,
												birth_commune_CNI = birth_commune_CNI,
												birth_zone_CNI = birth_zone_CNI,
												birthday_CNI = birthday_CNI,
												marital_status_CNI = marital_status_CNI,
												kind_of_work_CNI = kind_of_work_CNI,
												CNI_number_CNI = CNI_number_CNI,
												delivered_date_CNI = delivered_date_CNI,
												delivered_zone_CNI = delivered_zone_CNI
												)
			new_CNI_obj.save()
			return redirect(register_CNI_pics)
			
				
	register_cni_form = RegisterCNIForm()
	return render(request, 'all_forms.html',locals())

@login_required
def register_CNI_pics(request):
	register_CNI_pics_form = CNIPicsForm(request.POST , request.FILES)
	if request.method == "POST":
		if register_CNI_pics_form.is_valid():
			new_CNI_obj = CNI.objects.filter(user=request.user).get()
			print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
			print(new_CNI_obj)
			recto_CNI_pic = register_CNI_pics_form.cleaned_data['recto_CNI_pic']
			verso_CNI_pic = register_CNI_pics_form.cleaned_data['verso_CNI_pic']
			new_CNI_obj.recto_CNI_pic = recto_CNI_pic
			new_CNI_obj.verso_CNI_pic = verso_CNI_pic
			new_CNI_obj.save()
			messages.success(request, "Your CNI was registered successfully!")
			return redirect(home_view)
	register_CNI_pics_form = CNIPicsForm()
	return render(request, "all_forms.html", locals())


@login_required
def document_view(request):
	try:
		documents_query = CompleteIdentity.objects.filter(user=request.user)
	except:
		return redirect(_404)
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
	# Headers
	try:
		CNI_query = CNI.objects.get(user=request.user)
	except:
		messages.error(request, "Vous deveze enregistrer votre Carte d'Idéntité !")
		return redirect(register_CNI)
	template_name='all_forms.html'
	cp_form = CompleteIdentityForm(request.POST)
	if request.method == "POST":
		if cp_form.is_valid():
			complete_id = cp_form.save(commit=False)
			complete_id.user = request.user
			complete_id.first_name_beneficiary = CNI_query.first_name_CNI
			complete_id.last_name_beneficairy = CNI_query.last_name_CNI
			complete_id.father_fullname_beneficiary = CNI_query.father_fullname_CNI
			complete_id.mother_fullname_benefiaciary = CNI_query.mother_fullname_CNI
			complete_id.birth_province = CNI_query.birth_province_CNI
			complete_id.birth_commune = CNI_query.birth_commune_CNI
			complete_id.birth_zone = CNI_query.birthday_CNI
			complete_id.marital_status = CNI_query.marital_status_CNI
			complete_id.profession = CNI_query.kind_of_work_CNI
			complete_id.birth_year = CNI_query.birthday_CNI
			complete_id.CNI_number_cp = CNI_query.CNI_number_CNI

			#Chiesfs queries

			zone = get_object_or_404(Zone, name=complete_id.residence_zone)
			commune = zone.commune
			municipalite = commune.province
			zone_leader = get_object_or_404(ZoneLeader, zone_leaded=zone)

			if '_preview' in request.POST:
				template_name = 'cp_preview.html'
				if '_cancel' in request.POST:
					return redirect(complete_identity_view)
				elif '_send' in request.POST:
					complete_id.save()
					messages.success(request, "Formulaire envoyé")
					return redirect(document_view)

			elif '_send' in request.POST:
				print('#########################')
				print(complete_id)
				complete_id.save()
				messages.success(request, "Formulaire envoyé")
				return redirect(document_view)

	cp_form = CompleteIdentityForm()
	return render(request, template_name, locals())

@login_required
def _404(request):
	
	return render(request, "404_.html", locals())
