from django.urls import path, include
from . import views



urlpatterns = [
	path('', views.home_view, name='riha_home'),
	path('login/', views.login_view, name="riha_connexion"),
	path('logout/', views.logout_view, name="riha_deconnexion"),
	path('register/', views.register_view, name='riha_register'),
	path('documents', views.document_view, name='riha_all_user_documents'),
	path('documents/complete_identity/<id>/', views.cp_one_view, name='riha_cp_one'),
	path('documents/complete_identity/', views.complete_identity_view, name='riha_complete_identity'),
]