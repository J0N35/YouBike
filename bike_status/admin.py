from django.contrib import admin
from models import GzipFile
from models import Station
from models import History

admin.site.register(GzipFile)
admin.site.register(Station)
admin.site.register(History)