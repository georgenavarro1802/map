# -*- coding: UTF-8 -*-

import json
from datetime import datetime

from django.core import serializers
from django.db import transaction
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render_to_response

from mapae.form import CompaniaForm
from mapae.models import Pais, Compania, TipoCompania, Provincia, Ciudad


def tipo_repr(x, pais):
    d = model_to_dict(x)
    d['cantidad_publicada'] = x.cantidad_publicada_pais(pais)
    return d


def model_repr(x):
    d = model_to_dict(x, exclude=['nombre', 'pais', 'direccion'])
    d['provincia'] = x.provincia.nombre
    return d


def generar_nombre(nombre, original):
    ext = ""
    if original.find(".") > 0:
        ext = original[original.rfind("."):]
    fecha = datetime.now().date()
    hora = datetime.now().time()
    return nombre + fecha.year.__str__() + fecha.month.__str__() + fecha.day.__str__() + hora.hour.__str__() + hora.minute.__str__() + hora.second.__str__() + ext


def paises(request):
    try:
        with transaction.atomic():
            pais = Pais.objects.get(pk=request.POST['id'])
            data = {'companias': [model_repr(x) for x in Compania.objects.filter(publicada=True, pais=pais)],
                    'result': 'ok',
                    'lat': pais.latitud,
                    'lng': pais.longitud,
                    'tipos': {str(x.id): "{} ({})".format(x.nombre, str(x.cantidad_publicada_pais(pais)))
                              for x in TipoCompania.objects.all()}}
            return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({"result": "bad", "error": str(ex)}), content_type="application/json")


def provincias(request):
    try:
        with transaction.atomic():
            provincia = Provincia.objects.get(pk=request.POST['id'])
            data = {'companias': [model_repr(x) for x in Compania.objects.filter(publicada=True, provincia=provincia)],
                    'result': 'ok',
                    'lat': provincia.latitud,
                    'lng': provincia.longitud,
                    'tipos': {str(x.id): "{} ({})".format(x.nombre, str(x.cantidad_publicada_provincia(provincia)))
                              for x in TipoCompania.objects.all()}}
            return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({"result": "bad", "error": str(ex)}), content_type="application/json")


def ciudades(request):
    try:
        with transaction.atomic():
            ciudad = Ciudad.objects.get(pk=request.POST['id'])
            data = {'companias': [model_repr(x) for x in Compania.objects.filter(publicada=True, ciudad=ciudad)],
                    'result': 'ok',
                    'lat': ciudad.latitud,
                    'lng': ciudad.longitud,
                    'tipos': {str(x.id): "{} ({})".format(x.nombre, str(x.cantidad_publicada_ciudad(ciudad)))
                              for x in TipoCompania.objects.all()}}
            return HttpResponse(json.dumps(data), content_type="application/json")
    except Exception as ex:
        return HttpResponse(json.dumps({"result": "bad", "error": str(ex)}), content_type="application/json")


def provincia_ciudades(request):
    try:
        with transaction.atomic():
            provincia = Provincia.objects.get(pk=request.POST['id'])
            json_ciudad = serializers.serialize("json", provincia.mis_ciudades())
            return HttpResponse(json_ciudad, content_type="application/javascript")
    except Exception as ex:
        return HttpResponse(json.dumps({"result": "bad", "error": str(ex)}), content_type="application/json")


def guardar(request):
    try:
        with transaction.atomic():
            if not Compania.objects.filter(nombre=request.POST['companianombre'], tipo_id=request.POST['companiatipo'],
                                           pais_id=request.POST['pais']).exists():
                compania = Compania(nombre=request.POST['companianombre'],
                                    alias=request.POST['companiaalias'],
                                    tipo_id=request.POST['companiatipo'],
                                    pais_id=request.POST['pais'],
                                    provincia_id=request.POST['provincia'],
                                    ciudad_id=request.POST['ciudad'],
                                    direccion=request.POST['direccion'],
                                    latitud=0,
                                    longitud=0,
                                    descripcion=request.POST['descripcion'],
                                    email=request.POST['email'],
                                    website=request.POST['website'],
                                    twitter=request.POST['twitter'],
                                    facebook=request.POST['facebook'],
                                    celular=request.POST['celular'],
                                    convencional=request.POST['convencional'],
                                    publicada=False)
                compania.save()
                return HttpResponse(json.dumps({"result": "ok"}), content_type="application/json")
            return HttpResponse(json.dumps({"result": "badexist"}), content_type="application/json")
    except Exception:
        return HttpResponse(json.dumps({"result": "bad"}), content_type="application/json")


def index(request):
    paises = Pais.objects.all().order_by('-id')
    data = {'paises': paises,
            'tipos': [tipo_repr(x, paises[0]) for x in TipoCompania.objects.all()],
            'companias': Compania.objects.filter(publicada=True, pais=paises[0]),
            'form': CompaniaForm(),
            'lat_ecu': paises[0].latitud,
            'lng_ecu': paises[0].longitud}
    return render_to_response("base.html", data)
