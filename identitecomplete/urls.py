from django.urls import path, include
from . import views



urlpatterns = [
	path("", views.home_view, name='riha_home'),
	path('login/', views.login_view, name="riha_connexion"),
	path('logout/', views.logout_view, name="riha_deconnexion"),
	path('register/', views.register_view, name='riha_register'),
	path('register/cni_all/', views.register_CNI, name='riha_register_CNI'),
	path('register/cni_pics/', views.register_CNI_pics, name='riha_register_CNI_pics'),
	path('documents/cp/preview/', views.cp_preview, name='riha_cp_preview'),
	path('documents', views.document_view, name='riha_all_user_documents'),
	path('documents/complete_identity/<id>/', views.cp_one_view, name='riha_cp_one'),
	path('documents/complete_identity/', views.complete_identity_view, name='riha_complete_identity'),
]