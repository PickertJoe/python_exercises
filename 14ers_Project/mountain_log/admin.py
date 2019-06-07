from django.contrib import admin

# Register your models here.
from mountain_log.models import Topic
from mountain_log.models import Entry

admin.site.register(Topic)
admin.site.register(Entry)
