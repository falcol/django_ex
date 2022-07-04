from django.contrib import admin

from .models import Snippet


# Register your models here.
class FilterSnippet(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['code']
        }),
        ('Date information', {
            'fields': ['created_at'],
            'classes': ['collapse']
        }),
    ]
    list_display = (
        'id',
        'created',
        'updated',
        'title',
        'code',
        'linenos',
        'language',
    )
    list_filter = ['code']
    search_fields = ['code']


# Register your models here.
admin.site.register(Snippet, FilterSnippet)