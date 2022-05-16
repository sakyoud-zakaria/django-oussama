from django.db import models

from app_opdoo.models.CustomerModel import CustomerModel


class CustomerHistoryModel(models.Model):

    provenance_choice = (('OPHTALMOLOGUE', 'Ophtalmologue'),
                         ('OPTICIEN', 'Opticien'),
                         ('AU', 'Opticien'))

    customer_history_od_SPH = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_CYL = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_AXE = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_ADD = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_IND = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_O = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_ECVL = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_EEVP = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_HT = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_ACC = models.CharField(max_length=10, null=True, blank=True)
    customer_history_od_BIN = models.CharField(max_length=10, null=True, blank=True)

    customer_history_og_SPH = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_CYL = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_AXE = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_ADD = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_IND = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_O = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_ECVL = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_EEVP = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_HT = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_ACC = models.CharField(max_length=10, null=True, blank=True)
    customer_history_og_BIN = models.CharField(max_length=10, null=True, blank=True)

    customer_history_provenance = models.CharField(max_length=20, null=True, blank=True,choices=provenance_choice)
    customer_history_ordonnance = models.FileField(null=True, blank=True)
    customer_history_ordonnance_medecin = models.CharField(max_length=50,null=True, blank=True)
    customer_history_ordonnance_date = models.DateField(null=True, blank=True)
    customer_history_ref_customer = models.ForeignKey(CustomerModel,null=True, blank=True,on_delete=models.CASCADE)
    

    customer_history_created_at = models.DateTimeField(auto_now_add=True)
    customer_history_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.brand_ref) + " - " + str(self.brand_lable)
