from django.contrib import admin

# Register your models here.
from mountain_log.models import Mountain
from mountain_log.models import Entry

admin.site.register(Mountain)
admin.site.register(Entry)
