# -*- coding: UTF-8 -*-

from django.db import models


class TipoCompania(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = u"Tipo de compañia"
        verbose_name_plural = u"Tipos de compañias"
        ordering = ('nombre', )
        unique_together = ('nombre', )

    def cantidad_publicada(self):
        return self.compania_set.filter(publicada=True).count()

    def cantidad_publicada_pais(self, pais):
        return self.compania_set.filter(publicada=True, pais=pais).count()

    def cantidad_publicada_provincia(self, provincia):
        return self.compania_set.filter(publicada=True, provincia=provincia).count()

    def cantidad_publicada_ciudad(self, ciudad):
        return self.compania_set.filter(publicada=True, ciudad=ciudad).count()

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.nombre = self.nombre.upper()
        super(TipoCompania, self).save(force_insert, force_update, using)


class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = u"Pais"
        verbose_name_plural = u"Paises"
        unique_together = ('nombre', )

    def mis_provincias(self):
        return self.provincia_set.all()


class Provincia(models.Model):
    pais = models.ForeignKey(Pais)
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)

    def __str__(self):
        return u"{}".format(self.nombre)

    class Meta:
        verbose_name = u"Provincia"
        verbose_name_plural = u"Provincias"
        unique_together = ('pais', 'nombre')
        ordering = ('pais', 'nombre')

    def mis_ciudades(self):
        return self.ciudad_set.all()


class Ciudad(models.Model):
    provincia = models.ForeignKey(Provincia)
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = u"Ciudad"
        verbose_name_plural = u"Ciudades"
        unique_together = ('provincia', 'nombre')
        ordering = ('provincia', 'nombre')


class Compania(models.Model):
    nombre = models.CharField(max_length=200)
    alias = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.ForeignKey(TipoCompania)
    pais = models.ForeignKey(Pais)
    provincia = models.ForeignKey(Provincia)
    ciudad = models.ForeignKey(Ciudad, blank=True, null=True)
    direccion = models.CharField(max_length=300)
    latitud = models.FloatField(default=0)
    longitud = models.FloatField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=100, blank=True, null=True)
    convencional = models.CharField(max_length=100, blank=True, null=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name = u"Compañia"
        verbose_name_plural = u"Compañias"
