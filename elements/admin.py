from django.contrib import admin
from .models import *

@admin.register(Tab)
class TabAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links =('id', 'title',)
    search_fields = ('id', 'title',)

@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = ('tab_id', 'tab', 'id', 'title',)
    list_display_links =('id', 'title',)
    search_fields = ('id', 'tab', 'title',)

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tab', 'element', 'files',)
    list_display_links =('id', 'files',)
    search_fields = ('id', 'tab', 'element', 'files',)
    
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tab', 'element', 'photo',)
    list_display_links =('id', 'photo',)
    search_fields = ('id', 'tab', 'element', 'photo',)