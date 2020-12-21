from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from .models import Profile,Profiles_Picture, Historique

admin.site.site_header = 'Tretis Administration'


class Profiles_Picture_Admin(admin.ModelAdmin):
    list_display = ('title','image')


admin.site.register(Historique)
admin.site.register(Profiles_Picture, Profiles_Picture_Admin)
admin.site.register(Profile)

