from django.contrib import admin
from pinger.models import Domain, ResponseTime

admin.site.register(Domain)
admin.site.register(ResponseTime)
