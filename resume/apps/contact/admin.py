from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact


class SocialAdmin(admin.ModelAdmin):
    class Meta:
        model = Social


class MailsAdmin(admin.ModelAdmin):
    class Meta:
        model = Mails


class FormAdmin(admin.ModelAdmin):
    class Meta:
        model = Form


admin.site.register(Contact, ContactAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Mails, MailsAdmin)
admin.site.register(Form, FormAdmin)
