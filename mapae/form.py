# -*- coding: UTF-8 -*-

import os

from django import forms
from mapae.models import TipoCompania, Pais, Provincia, Ciudad


class ExtFileField(forms.FileField):
    """
    * max_upload_size - a number indicating the maximum file size allowed for upload.
            500Kb - 524288
            1MB - 1048576
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    t = ExtFileField(ext_whitelist=(".pdf", ".txt"), max_upload_size=)
    """
    def __init__(self, *args, **kwargs):
        ext_whitelist = kwargs.pop("ext_whitelist")
        self.ext_whitelist = [i.lower() for i in ext_whitelist]
        self.max_upload_size = kwargs.pop("max_upload_size")
        super(ExtFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        upload = super(ExtFileField, self).clean(*args, **kwargs)
        if upload:
            size = upload.size
            filename = upload.name
            ext = os.path.splitext(filename)[1]
            ext = ext.lower()
            if size == 0 or ext not in self.ext_whitelist or size > self.max_upload_size:
                raise forms.ValidationError("Tipo de fichero o tamanno no permitido!")


class CompaniaForm(forms.Form):
    nombre = forms.CharField(label=u'Razón social')
    alias = forms.CharField(label=u'Alias', required=False)
    tipo = forms.ModelChoiceField(TipoCompania.objects, label=u'Tipo')
    pais = forms.ModelChoiceField(Pais.objects, label=u"País")
    provincia = forms.ModelChoiceField(Provincia.objects, label=u'Provincia')
    ciudad = forms.ModelChoiceField(Ciudad.objects, label=u'Ciudad', required=False)
    direccion = forms.CharField(label=u'Dirección', required=False)
    descripcion = forms.CharField(label=u"Descripción", widget=forms.Textarea(attrs={'rows': '3', 'cols': '3'}),
                                  required=False)
    email = forms.CharField(label=u'Email', required=False)
    website = forms.CharField(label=u'Website', required=False)
    twitter = forms.CharField(label=u'Twitter', required=False)
    facebook = forms.CharField(label=u'Facebook', required=False)
    celular = forms.CharField(label=u'Celular', required=False)
    convencional = forms.CharField(label=u'Convencional', required=False)
