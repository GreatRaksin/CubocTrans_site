from django.contrib import admin

from .models import Head
class HeadAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'title_on_image', 'image_preview')
admin.site.register(Head, HeadAdmin)


from .models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email', 'subject', 'message')
admin.site.register(Contact, ContactAdmin)
