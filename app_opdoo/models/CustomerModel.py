from email.policy import default
import imp
from pyexpat import model
from django.db import models

from app_opdoo.models import BrandModel,VendorModel

class CustomerModel(models.Model):

    customerMale = 1
    customerFemale = 2

    customer_choice_sexe = [
    (customerMale, "Masculin"),
    (customerFemale, "Féminin"),
    ]

    customer_firstname = models.CharField(max_length=50,null=True,blank=True,)
    customer_lastname = models.CharField(max_length=50,null=True,blank=True,)
    customer_birthday = models.DateField(null=True,blank=True)
    customer_ville = models.CharField(max_length=50,null=True,blank=True)
    customer_cin = models.CharField(max_length=50,null=True,blank=True)
    customer_sexe = models.CharField(choices=customer_choice_sexe,max_length=10,null=True,blank=True,)
    customer_email = models.CharField(max_length=50,null=True,blank=True)
    customer_profession = models.CharField(max_length=50,null=True,blank=True)
    customer_phone = models.CharField(max_length=50,null=True,blank=True,default=0)
    customer_medical_mutual = models.CharField(max_length=50,null=True,blank=True)
    customer_comment = models.TextField(null=True,blank=True,)

    customer_authorization_mail = models.BooleanField(null=True,blank=True,default=False)
    customer_authorization_sms = models.BooleanField(null=True,blank=True,default=False)

    customer_created_at = models.DateTimeField(auto_now_add=True)
    customer_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.customer_firstname) + " - " + str(self.customer_lastname)
