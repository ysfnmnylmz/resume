from django.contrib import admin
from resume.apps.portfolio.models import Portfolio, PortfolioCategories, Techs


class PortfolioAdmin(admin.ModelAdmin):
    class Meta:
        model = Portfolio


class PortfolioCategoriesAdmin(admin.ModelAdmin):
    class Meta:
        model = PortfolioCategories


class TechsAdmin(admin.ModelAdmin):
    class Meta:
        model = Techs


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Techs, TechsAdmin)
admin.site.register(PortfolioCategories, PortfolioCategoriesAdmin)
