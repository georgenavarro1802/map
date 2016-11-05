#!/usr/bin/env python
# coding=utf-8

import sys
import os
import unicodedata

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

# csv_filepathname = "migracion.csv"
# csv_filepathname2 = "fallos.csv"

your_djangoproject_home = os.path.split(SITE_ROOT)[0]

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'


def to_unicode(s):
    if isinstance(s, unicode):
        return s

    from locale import getpreferredencoding
    for cp in (getpreferredencoding(), "cp1255", "cp1250"):
        try:
            return unicode(s, cp)
        except UnicodeDecodeError:
            pass
    raise Exception("Conversion to unicode failed")


import django

django.setup()

from mapae.models import *
from datetime import date, datetime

import csv


dataReader = csv.reader(open('companias.csv', "rU"), delimiter=';')


def convertirfecha(fecha):
    try:
        return date(int(fecha[6:10]), int(fecha[3:5]), int(fecha[0:2]))
    except Exception as ex:
        return datetime.now().date()


def remover_caracteres_especiales(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD', unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()


listado = {
    u'Azuay': {u'lat': -2.996002,
               u'lng': -79.306153,
               u'ciudades': {u'Cuenca': [-2.900669, -79.005002],
                             u'Camilo Ponce Enriquez': [-3.062614, -79.742722],
                             u'Chordeleg': [-2.926937, -78.777144],
                             u'El Pan': [-2.786454, -78.664706],
                             u'Giron': [-3.158393, -79.146752],
                             u'Guachapala': [-2.768232, -78.712599],
                             u'Gualaceo': [-2.886273, -78.776307],
                             u'Nabon': [-3.336058, -79.064044],
                             u'Ona': [-3.469859, -79.153887],
                             u'Paute': [-2.795503, -78.767531],
                             u'Pucara': [-3.220062, -79.469743],
                             u'San Fernando': [-3.145602, -79.256231],
                             u'Santa Isabel': [-3.276130, -79.314745],
                             u'Sevilla de Oro': [-2.798212, -78.654867],
                             u'Sigsig': [-3.050975, -78.795576]}
               },
    u'Bolivar': {u'lat': -1.533004,
                 u'lng': -79.148553,
                 u'ciudades': {u'Guaranda': [-1.590496, -78.998995],
                               u'Caluma': [-1.631550, -79.257345],
                               u'Chillanes': [-1.943456, -79.065535],
                               u'Chimbo': [-1.685750, -79.022942],
                               u'Echeandia': [-1.415834, -79.279189],
                               u'Las Naves': [-1.285048, -79.315228],
                               u'San Miguel': [-1.713397, -79.038756]}
                 },
    u'Canar ': {u'lat': -2.631831,
                u'lng': -79.004357,
                u'ciudades': {u'Azogues': [-2.739186, -78.845358],
                              u'Biblian': [-2.713832, -78.889236],
                              u'Canar': [-2.556369, -78.939386],
                              u'Deleg': [-2.786960, -78.926253],
                              u'El Tambo': [-2.514252, -78.925899],
                              u'La Troncal': [-2.421742, -79.343648],
                              u'Suscal': [-2.436213, -79.051813]}
                },
    u'Carchi': {u'lat': 0.797663,
                u'lng': -77.995400,
                u'ciudades': {u'Tulcan': [0.814900, -77.716727],
                              u'Bolivar': [0.506287, -77.901628],
                              u'Espejo': [0.506287, -76.901628],
                              u'Mira': [0.550188, -78.040802],
                              u'Montufar': [0.565147, -77.772194],
                              u'Huaca': [0.632023, -77.726984]}
                },
    u'Chimborazo ': {u'lat': -1.624985,
                     u'lng': -78.831655,
                     u'ciudades': {
                         u'Riobamba': [-1.664365, -78.652647],
                         u'Alausi': [-2.199236, -78.846173],
                         u'Chambo': [-1.733773, -78.594518],
                         u'Chunchi': [-2.289771, -78.920084],
                         u'Colta': [-1.734244, -78.764205],
                         u'Cumanda': [-2.202782, -79.136830],
                         u'Guamote': [-1.936186, -78.709273],
                         u'Guano': [-1.607398, -78.631511],
                         u'Pallatanga': [-2.020494, -78.972183],
                         u'Penipe': [-1.554546, -78.539887]}
                     },
    u'Cotopaxi': {u'lat': -0.716710,
                  u'lng': -78.837854,
                  u'ciudades': {
                      u'Latacunga': [-0.931129, -78.605127],
                      u'La Mana': [-0.933298, -79.231263],
                      u'Pangua': [-0.929543, -78.625820],
                      u'Pujili': [-0.958255, -78.696227],
                      u'Salcedo': [-1.042356, -78.589840],
                      u'Saquisili': [-0.822422, -78.668332],
                      u'Sigchos': [-0.697271, -78.890419]}
                  },
    u'El Oro': {u'lat': -3.420035,
                u'lng': -79.885360,
                u'ciudades': {
                    u'Machala': [-3.257716, -79.956467],
                    u'Arenillas': [-3.555826, -80.065527],
                    u'Atahualpa': [-3.590649, -79.658175],
                    u'Balsas': [-3.759666, -79.823463],
                    u'Chilla': [-3.457306, -79.579747],
                    u'El Guabo': [-3.236754, -79.818850],
                    u'Huaquillas': [-3.476668, -80.221986],
                    u'Las Lajas': [-3.785520, -80.063376],
                    u'Marcabeli': [-3.784455, -79.911622],
                    u'Pasaje': [-3.325956, -79.804173],
                    u'Pinas': [-3.680418, -79.682293],
                    u'Portovelo': [-3.717163, -79.612813],
                    u'Santa Rosa': [-3.459790, -79.967766],
                    u'Zaruma': [-3.687228, -79.610109]}
                },
    u'Esmeraldas': {u'lat': 0.950949,
                    u'lng': -79.663131,
                    u'ciudades': {
                        u'Esmeraldas': [0.968155, -79.649484],
                        u'Atacames': [0.868006, -79.846246],
                        u'Eloy Alfaro': [0.965914, -79.655299],
                        u'Muisne': [0.610824, -80.019543],
                        u'Quininde': [0.326841, -79.463167],
                        u'Rioverde': [1.059879, -79.403270],
                        u'San Lorenzo': [1.269332, -78.843856]}
                    },
    u'Galapagos ': {u'lat': -0.323462,
                    u'lng': -91.242513,
                    u'ciudades': {
                        u'San Cristobal': [-0.861997, -89.436718],
                        u'Isabela': [-0.809473, -91.132497],
                        u'Santa Cruz': [-0.633301, -90.336896]}
                    },
    u'Guayas': {u'lat': -2.324873,
                u'lng': -79.881935,
                u'ciudades': {
                    u'Guayaquil': [-2.170912, -79.923264],
                    u'Alfredo Baquerizo': [-1.893635, -79.556272],
                    u'Balao': [-2.905096, -79.700620],
                    u'Balzar': [-1.366424, -79.899874],
                    u'Colimes': [-1.545259, -80.010123],
                    u'Daule': [-1.861365, -79.977583],
                    u'Duran': [-2.159970, -79.818743],
                    u'El Empalme': [-1.048664, -79.608436],
                    u'El Triunfo': [-2.173495, -79.596133],
                    u'General Antonio Elizalde': [-2.174470, -79.200096],
                    u'Isidro Ayora': [-1.880363, -80.145800],
                    u'Lomas de Sargentillo': [-1.875838, -80.088229],
                    u'Marcelino Mariduena': [-2.098131, -79.695118],
                    u'Milagro': [-2.139133, -79.593415],
                    u'Naranjal': [-2.669269, -79.621439],
                    u'Naranjito': [-2.176020, -79.435788],
                    u'Nobol': [-1.915191, -80.012140],
                    u'Palestina': [-1.627088, -79.978516],
                    u'Pedro Carbo': [-1.819948, -80.238047],
                    u'Playas': [-2.628029, -80.389624],
                    u'Salitre': [-1.834038, -79.814816],
                    u'Samborondon': [-1.997329, -79.786810],
                    u'Santa Lucia': [-1.714577, -79.985125],
                    u'Simon Bolivar': [-2.001540, -79.486148],
                    u'Yaguachi': [-2.096161, -79.693472]}
                },
    u'Imbabura': {u'lat': 0.406030,
                  u'lng': -78.286161,
                  u'ciudades': {
                      u'Ibarra': [0.339759, -78.121880],
                      u'Antonio Ante': [0.362315, -78.126673],
                      u'Cotacachi': [0.307187, -78.264928],
                      u'Otavalo': [0.234060, -78.260722],
                      u'Pimampiro': [0.389963, -77.940160],
                      u'San Miguel de Urcuqui': [0.420695, -78.194718]}
                  },
    u'Loja': {u'lat': -4.046672,
              u'lng': -79.287681,
              u'ciudades': {
                  u'Loja': [-4.007423, -79.210268],
                  u'Calvas': [-4.321841, -79.553146],
                  u'Catamayo': [-3.988416, -79.352059],
                  u'Celica': [-4.103101, -79.958475],
                  u'Chaguarpamba': [-3.878352, -79.646094],
                  u'Espindola': [-4.376737, -79.942726],
                  u'Gonzanama': [-4.230715, -79.435508],
                  u'Macara': [-4.375893, -79.936479],
                  u'Olmedo': [-3.935104, -79.646410],
                  u'Paltas': [-4.003965, -79.212928],
                  u'Pindal': [-4.116253, -80.107648],
                  u'Puyango': [-4.018240, -80.019669],
                  u'Quilanga': [-4.297229, -79.400892],
                  u'Saraguro': [-3.622975, -79.238699],
                  u'Sozoranga': [-4.328599, -79.791781],
                  u'Zapotillo': [-4.385543, -80.244087]}
              },
    u'Los Rios': {u'lat': -1.242321,
                  u'lng': -79.434776,
                  u'ciudades': {
                      u'Babahoyo': [-1.802147, -79.533463],
                      u'Baba': [-1.785688, -79.674964],
                      u'Buena Fe': [-0.885780, -79.487457],
                      u'Mocache': [-1.183789, -79.505423],
                      u'Montalvo': [-1.788035, -79.286549],
                      u'Palenque': [-1.432322, -79.753318],
                      u'Puebloviejo': [-1.550086, -79.533290],
                      u'Quevedo': [-1.022103, -79.459434],
                      u'Quinsaloma': [-1.204851, -79.310265],
                      u'Valencia': [-0.949780, -79.355171],
                      u'Ventanas': [-1.442338, -79.461626],
                      u'Vinces': [-1.550576, -79.763497]}
                  },
    u'Manabi': {u'lat': -0.620131,
                u'lng': -80.167917,
                u'ciudades': {
                    u'Portoviejo': [-1.053937, -80.446538],
                    u'24 de Mayo': [-0.957853, -80.743101],
                    u'Bolivar': [-1.236134, -80.812408],
                    u'Chone': [-0.713737, -80.107772],
                    u'El Carmen': [-0.271267, -79.465442],
                    u'Flavio Alfaro': [-0.404555, -79.905497],
                    u'Jama': [-0.204320, -80.264375],
                    u'Jaramijo': [-0.956818, -80.637074],
                    u'Jipijapa': [-1.352652, -80.583386],
                    u'Junin': [-0.927982, -80.206482],
                    u'Manta': [-0.968310, -80.710202],
                    u'Montecristi': [-1.046883, -80.657265],
                    u'Olmedo': [-1.394385, -80.205582],
                    u'Pajan': [-1.552187, -80.427475],
                    u'Pedernales': [0.072913, -80.050356],
                    u'Pichincha': [-1.044357, -79.822712],
                    u'Puerto Lopez': [-1.553688, -80.805204],
                    u'Rocafuerte': [-0.923026, -80.450842],
                    u'San Vicente': [-0.604666, -80.403485],
                    u'Santa Ana': [-1.206948, -80.369969],
                    u'Sucre': [-1.278170, -80.424042],
                    u'Tosagua': [-0.783953, -80.232983]}
                },
    u'Morona Santiago': {u'lat': -2.616959,
                         u'lng': -78.115192,
                         u'ciudades': {
                             u'Morona': [-2.616959, -78.002582],
                             u'Gualaquiza': [-3.406200, -78.572545],
                             u'Huamboya': [-1.945204, -77.991246],
                             u'Limon Indanza': [-2.965511, -78.429983],
                             u'Logrono': [-2.616607, -78.206384],
                             u'Palora': [-1.700871, -77.967396],
                             u'San Juan Bosco': [-3.104191, -78.520777],
                             u'Santiago de Mendez': [-2.715556, -78.318108],
                             u'Sucua': [-2.456408, -78.167296],
                             u'Taisha': [-2.334415, -77.440239]}
                         },
    u'Napo': {u'lat': -0.692828,
              u'lng': -77.947098,
              u'ciudades': {
                  u'Tena': [-0.996272, -77.813802],
                  u'Archidona': [-0.908179, -77.807579],
                  u'Carlos Julio Arosemena Tola': [-1.165479, -77.855784],
                  u'El Chaco': [-0.337012, -77.810819],
                  u'Quijos': [-0.321992, -77.790424]}
              },
    u'Orellana': {u'lat': -0.739822,
                  u'lng': -76.607967,
                  u'ciudades': {
                      u'Francisco de Orellana': [-0.461635, -76.993175],
                      u'Aguarico': [-0.377023, -76.365016],
                      u'La Joya de los Sachas': [-0.301710, -76.856051],
                      u'Loreto': [-0.690197, -77.305225]}
                  },
    u'Pastaza': {u'lat': -1.702935,
                 u'lng': -77.204000,
                 u'ciudades': {
                     u'Pastaza': [-1.450126, -78.130174],
                     u'Arajuno': [-1.238557, -77.674520],
                     u'Mera': [-1.460101, -78.111248],
                     u'Santa Clara': [-1.265535, -77.888024]}
                 },
    u'Pichincha': {u'lat': -0.028242,
                   u'lng': -78.695499,
                   u'ciudades': {
                       u'Quito': [-0.179041, -78.461446],
                       u'Cayambe': [0.032036, -78.150205],
                       u'Mejia': [-0.304355, -78.474581],
                       u'Pedro Moncayo': [0.330683, -78.118141],
                       u'Pedro Vicente Maldonado': [0.081679, -79.050107],
                       u'Puerto Quito': [0.116667, -79.266495],
                       u'Ruminahui': [-0.211068, -78.401137],
                       u'San Miguel de los Bancos': [0.024097, -78.894475]}
                   },
    u'Santa Elena': {u'lat': -2.069911,
                     u'lng': -80.620886,
                     u'ciudades': {
                         u'Santa Elena': [-2.267523, -80.730750],
                         u'La Libertad': [-2.230788, -80.900874],
                         u'Salinas': [-2.223211, -80.957721]}
                     },
    u'Santo Domingo': {u'lat': -0.260816,
                       u'lng': -79.233000,
                       u'ciudades': {
                           u'Santo Domingo': [-0.240153, -79.176064],
                           u'La Concordia': [0.009098, -79.391971]}
                       },
    u'Sucumbios': {u'lat': 0.100267,
                   u'lng': -76.700630,
                   u'ciudades': {
                       u'Lago Agrio': [0.099871, -76.866581],
                       u'Cascales': [0.079755, -77.210750],
                       u'Cuyabeno': [0.077253, -76.885079],
                       u'Gonzalo Pizarro': [0.016477, -77.378329],
                       u'Putumayo': [-0.058796, -75.458312],
                       u'Shushufindi': [-0.186059, -76.659186],
                       u'Sucumbios': [0.086941, -76.887614]}
                   },
    u'Tungurahua': {u'lat': -1.275023,
                    u'lng': -78.523297,
                    u'ciudades': {
                        u'Ambato': [-1.254912, -78.618529],
                        u'Banos': [-1.394718, -78.425217],
                        u'Cevallos': [-1.354229, -78.615911],
                        u'Mocha': [-1.418980, -78.658762],
                        u'Patate': [-1.313266, -78.508987],
                        u'Pelileo': [-1.325054, -78.538115],
                        u'Pillaro': [-1.174253, -78.543470],
                        u'Quero': [-1.382298, -78.607757],
                        u'Tisaleo': [-1.348072, -78.668643]}
                    },
    u'Zamora': {u'lat': -4.205457,
                u'lng': -78.875240,
                u'ciudades': {
                    u'Zamora': [-4.062156, -78.947625],
                    u'Centinela del Condor': [-3.916487, -78.786479],
                    u'Chinchipe': [-4.827668, -79.163197],
                    u'El Pangui': [-3.625470, -78.588038],
                    u'Nangaritza': [-4.309606, -78.718793],
                    u'Palanda': [-4.651369, -79.130788],
                    u'Paquisha': [-3.932514, -78.675188],
                    u'Yacuambi': [-3.611589, -78.966431],
                    u'Yantzaza': [-3.829015, -78.762209]}
                },

}

pais = Pais.objects.get(pk=1)  # Ecuador
for p, i in listado.items():
    if not Provincia.objects.filter(nombre=p, pais=pais).exists():
        provincia = Provincia(nombre=p, pais=pais)
        provincia.save()
    else:
        provincia = Provincia.objects.filter(nombre=p, pais=pais)[0]
    provincia.latitud = i['lat']
    provincia.longitud = i['lng']
    provincia.save()

    for c, l in i['ciudades'].items():
        if not Ciudad.objects.filter(nombre=c, provincia=provincia).exists():
            ciudad = Ciudad(nombre=c, provincia=provincia)
            ciudad.save()
        else:
            ciudad = Ciudad.objects.filter(nombre=c, provincia=provincia)[0]
        ciudad.latitud = l[0]
        ciudad.longitud = l[1]
        ciudad.save()
        print "Ciudad: " + str(ciudad.id)

    print "Provincia: " + str(provincia.id)


# Load companies from csv
next(dataReader)
for row in dataReader:
    if not Compania.objects.filter(nombre=row[1]).exists():
        company = Compania(nombre=row[1],
                           alias=row[2],
                           direccion=row[3],
                           latitud=float(row[4]),
                           longitud=float(row[5]),
                           descripcion=row[6],
                           email=row[7],
                           website=row[8],
                           twitter=row[9],
                           facebook=row[10],
                           celular=row[11],
                           convencional=row[12],
                           publicada=row[13],
                           ciudad_id=int(row[14]),
                           pais_id=int(row[15]),
                           provincia_id=int(row[16]),
                           tipo_id=int(row[17])
        )
        company.save()
        print company.nombre
    else:
        print "Ya existe {}".format(row)