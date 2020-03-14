from django.contrib import admin
from .models import *


class EmploymentsAdmin(admin.ModelAdmin):
    class Meta:
        model = Employments


class EducationsAdmin(admin.ModelAdmin):
    class Meta:
        model = Educations


class SkillsAdmin(admin.ModelAdmin):
    class Meta:
        model = Skills


admin.site.register(Employments, EmploymentsAdmin)
admin.site.register(Educations, EducationsAdmin)
admin.site.register(Skills, SkillsAdmin)
