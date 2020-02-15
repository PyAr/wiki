
Obtener Ubicacion Geografica
============================

* Como obtener distintos datos de la ubicacion Geografica, usando Python-Geoip, ejemplo simple.

**Requisitos:** Base de Datos de Geo-Location en la misma ubicacion que el programa, descargarla usando:

::

    wget --verbose http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz


**Nota:** *Depende de la conectividad con Internet usando direccion ip publica version 4, se desconoce el comportamiento con ip version 6.*

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    #
    import urllib
    try:
        import GeoIP
    except ImportError:
        print(" ERROR: No PYTHON-GEOIP avaliable!!!. ") # que hacer si falla la importacion de la libreria
        pass

    # La base de datos GeoLiteCity.dat debe estar en la misma ubicacion que este programa
    gi = GeoIP.open(
    "GeoLiteCity.dat", GeoIP.GEOIP_INDEX_CACHE | GeoIP.GEOIP_CHECK_CACHE)

    # Obtiene la IP Publica
    try:
        # esta URL puede ser reemplazada con otra que preste similar servicio
        ip = urllib.urlopen(
        'http://www.whatismyip.com/automation/n09230945.asp').read()
        print ip
    except: # que hacer si falla la conectividad
        print ("ERROR: Network error!!!. ")
        pass

    # Obtiene los datos de la DataBase usando la IP Publica
    data = gi.record_by_name(ip)

    # Imprime los datos en la linea de comandos
    print data


**Ejemplo:**

::

    /usr/bin/env python geolocation.py
    190.17.169.XXX
    {'city': 'XXXXXX', 'region_name': 'Buenos Aires', 'region': '01', 'area_code': 0, 'time_zone': 'America/Argentina/Buenos_Aires', 'longitude': -58.92079000071094, 'metro_code': 0, 'country_code3': 'ARG', 'latitude': -34.17680005629883, 'postal_code': None, 'dma_code': 0, 'country_code': 'AR', 'country_name': 'Argentina'}


**Colaboracion:** *Si tenes conectividad con internet con ip version 6 NATIVA, puedes documentar tu experiencia aqui.*

*Disclaimer: el uso o no de SheBang/Declaracion de Encoding queda a criterio del usuario.*

*Fe de Erratas: seguramente hay una forma mejor de hacerlo, pero esta funciona correctamente.*

