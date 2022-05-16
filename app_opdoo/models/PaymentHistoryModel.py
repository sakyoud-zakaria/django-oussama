from email.policy import default
import imp
from pyexpat import model
from django.db import models
from app_opdoo.models import CustomerModel

class PaymentHistoryModel(models.Model):

    historique_payement_methode = models.CharField(max_length=50, null=True, blank=True)
    historique_payement_customer = models.ForeignKey(CustomerModel, null=True, blank=True,on_delete=models.CASCADE)
    historique_payement_total = models.CharField(max_length=50, null=True, blank=True)
    historique_payement_session_key = models.CharField(max_length=50, null=True, blank=True)
    historique_payement_carte_montant = models.FloatField(null=True, blank=True)
    historique_payement_carte_numero_recu = models.CharField(max_length=50, null=True, blank=True)
    historique_payement_cheque_montant = models.FloatField( null=True, blank=True)
    historique_payement_cheque_numero = models.CharField(max_length=50, null=True, blank=True)
    historique_payement_espece_montant = models.FloatField(null=True, blank=True)
    historique_payement_espece_remarque = models.CharField(max_length=50, null=True, blank=True)

    historique_payement_created_at = models.DateTimeField(auto_now_add=True)
    historique_payement_updated_at = models.DateTimeField(auto_now=True)
