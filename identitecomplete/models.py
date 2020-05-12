from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # La liaison OneToOne vers le modèle User
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


class Payement(models.Model):
	payement_method = models.CharField(max_length=15)

	def __str__(self):
		return self.payement_method

class Zone(models.Model):
	name = models.CharField(max_length=100)
	commune = models.ForeignKey('Commune', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Zone, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name}"

	class Meta:
		unique_together = ('name', 'commune')


class Commune(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey('Province', on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100, unique=True)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Commune, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name} {self.province}"

	class Meta:
		unique_together = ('name', "province")

class Province(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	date = models.DateTimeField ( default = timezone.now )

	def save( self, *args, **kwargs ):
		self.slug = slugify(self.name+str(self.date))#to compare if the we found identical values
		super( Province, self ).save( *args, **kwargs )

	def __str__(self):
		return f"{self.name}"

class ZoneLeader(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	zone_leaded = models.ForeignKey(Zone, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.first_name} - {self.last_name} Chef de la Zone {self.zone_leaded}"

class CommuneLeader(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	commune_leaded = models.ForeignKey(Commune, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.first_name} - {self.last_name} Administrateur de la Commune {self.commune_leaded}"

class ProvinceLeader(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	province_leaded = models.ForeignKey(Province, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.first_name} - {self.last_name} Gouverneur de la province {self.province_leaded}"

class CompleteIdentity(models.Model):
	"""docstring for ClassName"""
	# 
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=1)
	first_name_beneficiary = models.CharField(max_length=20)
	last_name_beneficairy = models.CharField(max_length=20)
	father_fullname_beneficiary = models.CharField(max_length=50)
	mother_fullname_benefiaciary = models.CharField(max_length=50)
	birth_zone = models.CharField(max_length=20)
	birth_year = models.CharField(max_length=20)
	birth_commune = models.CharField(max_length=20)
	birth_province = models.CharField(max_length=20)
	nationality = models.CharField(max_length=20)
	marital_status = models.CharField(max_length=20)
	profession = models.CharField(max_length=20)
	residence_zone = models.CharField(max_length=20)
	residence_quarter = models.CharField(max_length=20)
	CNI_number_cp = models.CharField(max_length=20)
	payement_method = models.CharField(max_length=20)
	trans_code = models.IntegerField()

	def __str__(self):
		return f"{self.id}-{self.first_name_beneficiary}-{self.last_name_beneficairy}"

class CNI(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	first_name_CNI = models.CharField(max_length=20)
	last_name_CNI = models.CharField(max_length=20)
	father_fullname_CNI = models.CharField(max_length=20)
	mother_fullname_CNI = models.CharField(max_length=20)
	birth_province_CNI = models.CharField(max_length=20)
	birth_commune_CNI = models.CharField(max_length=20)
	birth_zone_CNI = models.CharField(max_length=20)
	birthday_CNI = models.DateField(max_length=20)
	marital_status_CNI = models.CharField(max_length=20)
	kind_of_work_CNI = models.CharField(max_length=20)
	CNI_number_CNI = models.CharField(max_length=20)
	delivered_date_CNI = models.CharField(max_length=20)
	delivered_zone_CNI = models.CharField(max_length=20)
	recto_CNI_pic_CNI = models.ImageField(blank=True, upload_to="CNI/recto/")
	verso_CNI_pic_CNI = models.ImageField(blank=True, upload_to="CNI/verso/")

	def __str__(self):
		return f"CNI de  : {self.user.username}"

	class Meta:
		unique_together = ('user', 'CNI_number_CNI')

# class Documents(models.Model):
# 	"""docstring for Documents"""
# 	doc_type = models.ForeignKey(IdentiteComplete, related_name='DocType', on_delete=models.CASCADE);
# 	slug = models.CharField(100)


# 	def save(self, *args, **kwargs):
# 		self.slug = slugify(self.doc_type+" "+str(self.id))
# 		super(Documents, self).save(*args, **kwargs)

# 	def __str__(self):
# 		return f"{self.doc_type}"


	
	