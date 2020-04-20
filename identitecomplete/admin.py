from django.contrib import admin
from .models import *

class ProvinceAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}

class CommuneAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}

class ZoneAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_filter = ('name',)
	search_fields = ('name',)
	prepopulated_fields = {'slug' : ('name', )}


admin.site.register(CompleteIdentity)
admin.site.register(Profil)
admin.site.register(Province,ProvinceAdmin)
admin.site.register(Commune,CommuneAdmin)
admin.site.register(Zone,ZoneAdmin)
admin.site.register(CNI)
admin.site.register(ZoneLeader)
admin.site.register(CommuneLeader)
admin.site.register(ProvinceLeader)


