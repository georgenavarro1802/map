# -*- coding: UTF-8 -*-

from django.contrib import admin
from mapae.models import TipoCompania, Pais, Provincia, Ciudad, Compania


class TipoCompaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(TipoCompania, TipoCompaniaAdmin)


class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'latitud', 'longitud')
    ordering = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Pais, PaisAdmin)


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'latitud', 'longitud')
    ordering = ('nombre', 'pais')
    search_fields = ('nombre',)


admin.site.register(Provincia, ProvinciaAdmin)


class CiudadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'provincia', 'latitud', 'longitud')
    ordering = ('nombre', 'provincia')
    search_fields = ('nombre',)


admin.site.register(Ciudad, CiudadAdmin)


class CompaniaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias', 'tipo', 'pais', 'provincia', 'ciudad', 'direccion', 'latitud', 'longitud',
                    'descripcion', 'email', 'website', 'twitter', 'facebook', 'celular', 'convencional', 'publicada')
    ordering = ('nombre', 'pais')
    search_fields = ('nombre', 'pais__nombre', 'provincia__nombre', 'website', 'descripcion')
    list_filter = ('tipo', 'publicada')

admin.site.register(Compania, CompaniaAdmin)
