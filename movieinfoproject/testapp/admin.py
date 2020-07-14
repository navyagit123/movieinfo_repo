from django.contrib import admin
from testapp.models import movie

class movieadmin(admin.ModelAdmin):
    list_display=['moviename','hero','heroine']

# Register your models here.
admin.site.register(movie,movieadmin)
