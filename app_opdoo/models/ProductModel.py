from email.policy import default
import imp
from pyexpat import model
from django.db import models
from app_opdoo.models import BrandModel, VendorModel
class ProductModel(models.Model):

    productDeclarationOui = 1
    productDeclarationNon = 2


    productMonture = 1
    productVerre = 2
    productProduit = 3
    productService = 4

    productGenreHomme = 1
    productGenreFemme = 2
    productGenreEnfant = 3
    productGenreUnisexe = 4

    productMontureTypeOptique = 1
    productMontureTypeSolaire = 2
    productMontureTypeClip = 3

    product_choice_type = [
        (productMonture, "Monture"),
        (productVerre, "Verre"),
        (productProduit, "Produit"),
        (productService, "Service")
    ]
    product_choice_genre = [
        (productGenreHomme, "Homme"),
        (productGenreFemme, "Femme"),
        (productGenreEnfant, "Enfant"),
        (productGenreUnisexe, "UniSexe")
    ]

    product_choice_monture_type = [
        (productMontureTypeOptique, "Optique"),
        (productMontureTypeSolaire, "Solaire"),
        (productMontureTypeClip, "Clip"),
    ]


    product_choice_declaration = [
        (productDeclarationOui, "C"),
        (productDeclarationNon, "NC"),
    ]


    product_reference = models.CharField(max_length=50, null=True, blank=True)
    product_lable = models.CharField(max_length=50, null=True, blank=True,)
    product_descreption = models.CharField(max_length=500, null=True, blank=True,)
    product_selling_price = models.FloatField(null=True, blank=True, default=0)
    product_buying_price = models.FloatField(null=True, blank=True, default=0)
    product_quantity = models.IntegerField(null=True, blank=True, default=0)
    product_ref_brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, null=True, blank=True)
    product_ref_vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE, null=True, blank=True)
    product_type = models.CharField(max_length=10,choices=product_choice_type, null=True, blank=True)
    product_genre = models.CharField(max_length=10,choices=product_choice_genre, null=True, blank=True)
    product_monture_type = models.CharField(max_length=10,choices=product_choice_monture_type, null=True, blank=True)
    product_discount = models.IntegerField(null=True, blank=True, default=20)
    product_excel_code = models.CharField(max_length=500,null=True,blank=True)
    product_declaration = models.CharField(max_length=10,choices=product_choice_declaration, null=True, blank=True)

    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.product_reference)

    @property
    def get_genre_text(self):
        return self.get_product_genre_display()

    def save(self, *args, **kwargs):
        self.product_selling_price = round(self.product_selling_price, 2)
        super(ProductModel, self).save(*args, **kwargs)        