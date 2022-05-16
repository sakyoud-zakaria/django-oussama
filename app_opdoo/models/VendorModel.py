from django.db import models


class VendorModel(models.Model):

    vendor_reference = models.CharField(max_length=50,null=True,blank=True)
    vendor_lable = models.CharField(max_length=50,null=True,blank=True)
    vendor_descreption = models.CharField(max_length=500,null=True,blank=True)
    vendor_phone = models.CharField(max_length=20,null=True,blank=True)
    vendor_email = models.EmailField(null=True,blank=True)
    vendor_adress = models.CharField(max_length=100,null=True,blank=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.vendor_reference) +" "+ str(self.vendor_lable)
