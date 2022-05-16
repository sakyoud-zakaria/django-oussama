from django.contrib import admin
from app_opdoo.models import *

admin.site.register(VendorModel)
admin.site.register(BrandModel)
admin.site.register(ProductModel)
admin.site.register(ProductVarianteModel)
admin.site.register(SessionPOSModel)
admin.site.register(CustomerModel)
admin.site.register(CustomerHistoryModel)
admin.site.register(PaymentHistoryModel)



