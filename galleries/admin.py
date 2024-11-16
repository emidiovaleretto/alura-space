from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'caption', 'created_at', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('published',)
    list_per_page = 10


admin.site.register(Photo, PhotoAdmin)
