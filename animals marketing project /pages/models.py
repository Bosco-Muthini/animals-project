
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class CattleSex(models.Model):
    sex=models.CharField(max_length=10)
    def __str__(self):
        return self.sex
class Cattle(models.Model):
    owner_name=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    owner_contact=models.IntegerField()
    breed=models.CharField(max_length=100)
    weight=models.IntegerField()
    date_time=models.DateTimeField(auto_now=True)
    selling_price_range=models.IntegerField()
    location=models.CharField(max_length=100)
    cattle_age=models.IntegerField()
    cattle_sex_based_on=models.ForeignKey(CattleSex,on_delete=models.CASCADE)
    health_record_book=models.FileField(upload_to='cattle/health_record/')
    cattle_picture=models.ImageField(upload_to='cattle/cattle_pictures/')
    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('cattle_list')


        #for goat
class GoatSex(models.Model):
    goat_sex=models.CharField(max_length=10)
    def __str__(self):
        return self.goat_sex
class Goat(models.Model):
    owner_name=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    owner_contact=models.IntegerField()
    breed=models.CharField(max_length=100)
    weight=models.IntegerField()
    date_time=models.DateTimeField(auto_now=True)
    maximum_selling_price=models.IntegerField()
    location=models.CharField(max_length=100)
    goat_age=models.IntegerField()
    goat_sex_based_on=models.ForeignKey(GoatSex,on_delete=models.CASCADE)
    health_record_book=models.FileField(upload_to='goat/health_record/')
    goat_picture=models.ImageField(upload_to='goat/goat_pictures/')
    def __str__(self):
        return self.breed

    def get_absolute_url(self):
        return reverse('goat_list')

        #for machinery tools & equipments
class ToolPurpose(models.Model):
    tools_purpose=models.CharField(max_length=200)
    def __str__(self):
        return self.tools_purpose
class AnimalType(models.Model):
    animal_types=models.CharField(max_length=100)
    def __str__(self):
        return self.animal_types
class Machinery(models.Model):
    owner_name=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    owner_contact=models.IntegerField()
    tool_name=models.CharField(max_length=200)
    date_time=models.DateTimeField(auto_now=True)
    brief_its_usage=models.TextField()
    location=models.CharField(max_length=100)
    tools_number=models.IntegerField()
    maximum_selling_price=models.IntegerField()
    tool_purpose=models.ForeignKey(ToolPurpose,on_delete=models.CASCADE)
    animal_type=models.ForeignKey(AnimalType,on_delete=models.CASCADE)
    animals_type=models.CharField(max_length=500,null=True,blank=True)
    machinery_tool_picture=models.ImageField(upload_to='machinery/machinery_tools_pictures/')
    def __str__(self):
        return self.tool_name

    def get_absolute_url(self):
        return reverse('machinery')