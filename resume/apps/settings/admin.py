from django.contrib import admin
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):

    class Meta:
        model = Settings


admin.site.register(Settings, SettingsAdmin)
