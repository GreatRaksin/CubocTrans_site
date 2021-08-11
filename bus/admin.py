from django.contrib import admin
from .models import Contact, Head, Partner


class HeadAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'title_on_image', 'image_preview')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'cargo_name', 'volume', 'cost')
    list_filter = ('company_name', 'phone', 'email', 'cost')

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Head, HeadAdmin)
admin.site.register(Partner, PartnerAdmin)
