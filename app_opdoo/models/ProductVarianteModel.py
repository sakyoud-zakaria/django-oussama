import imp
from pyexpat import model
from django.db import models

from app_opdoo.models import ProductModel,VendorModel

class ProductVarianteModel(models.Model):

    product_variante_reference = models.CharField(max_length=500,null=True,blank=True)
    product_variante_ref_product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True,blank=True)
    product_variante_ref_vendor = models.ForeignKey(VendorModel,on_delete=models.CASCADE,null=True,blank=True)
    product_invoice_number = models.CharField(max_length=500,null=True,blank=True)
    product_variante_excel_code = models.CharField(max_length=500,null=True,blank=True)

    product_variante_created_at = models.DateTimeField(auto_now_add=True)
    product_variante_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.product_variante_reference) + " - " + str(self.product_variante_ref_product)
