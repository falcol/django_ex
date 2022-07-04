from django.contrib import admin

from .models import Car


class FilterCar(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name']
        }),
        ('Date information', {
            'fields': ['created_at'],
            'classes': ['collapse']
        }),
    ]
    list_display = ('id', 'name', 'color', 'brand', 'created_at', 'updated_at')
    list_filter = ['name']
    search_fields = ['name']


# Register your models here.
admin.site.register(Car, FilterCar)
