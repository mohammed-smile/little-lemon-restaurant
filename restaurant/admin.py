from django.contrib import admin

from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Menu, MenuAdmin)
admin.site.site_header = 'Little Lemon administratoin'
admin.site.site_title = 'Little Lemon administratoin'