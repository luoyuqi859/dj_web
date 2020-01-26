from django.contrib import admin
from lwebcms.models import Userinfo
# Register your models here.

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    pass