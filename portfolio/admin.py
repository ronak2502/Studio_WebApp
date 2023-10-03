from django.contrib import admin

from .models import Portfolio
# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'categorie', 'show', 'project_date')
    list_display_links = ('id', 'name', 'categorie',)
    list_editable = ('show',)
    list_per_page = 20


admin.site.register(Portfolio, PortfolioAdmin)