from email.policy import default
import imp
from pyexpat import model
from django.db import models

from app_opdoo.models import ProductModel

class SessionPOSModel(models.Model):

    session_pos_ref_product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True,blank=True)
    session_pos_user_key = models.CharField(max_length=50,null=True,blank=True)
    session_pos_reciept_key = models.CharField(max_length=50,null=True,blank=True)
    session_pos_quantity = models.IntegerField(default=0,null=True,blank=True)
    session_pos_discount = models.IntegerField(default=0,null=True,blank=True)
    session_pos_created_at = models.DateTimeField(auto_now_add=True)
    session_pos_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.session_pos_user_key) +"-"+str(self.session_pos_reciept_key)
