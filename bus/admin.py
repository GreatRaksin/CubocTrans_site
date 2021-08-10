from django.contrib import admin
from .models import Contact, Head


class HeadAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'title_on_image', 'image_preview')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'cargo_name', 'volume', 'cost')
    list_filter = ('company_name', 'phone', 'email', 'cost')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Head, HeadAdmin)
