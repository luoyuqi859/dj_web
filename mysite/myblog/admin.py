from django.contrib import admin
from myblog.models import TopMenu,Banner,Artical
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class ArticalSummer(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(TopMenu)
admin.site.register(Banner)
admin.site.register(Artical,ArticalSummer)
