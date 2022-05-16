from django.db import models


class BrandModel(models.Model):

    brand_ref = models.CharField(max_length=50)
    brand_lable = models.CharField(max_length=50)

    brand_created_at = models.DateTimeField(auto_now_add=True)
    brand_updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.brand_ref) +" - " + str(self.brand_lable)
