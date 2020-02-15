
SimpleSoapClient
----------------

Descripción
:::::::::::

En este ejemplo se muestra utilizar servicios webs de manera simple (código usado en `Factura Electronica`_)

Utiliza SimpleXmlElement_ y SimpleSoapClient_, manejando de manera simple el protocolo SOAP y XML.

**Nota**: Ver otras librerias más avanzadas.

Ejemplo: Feriados (Ministerio del Interior)
:::::::::::::::::::::::::::::::::::::::::::

Ver: http://www.mininterior.gov.ar/servicios/wsferiados.asp

::

        # Demo & Test: Feriados (Ministerio del Interior):
        from datetime import datetime, timedelta
        client = SoapClient(
            location = "http://webservices.mininterior.gov.ar/Feriados/Service.svc",
            action = 'http://tempuri.org/IMyService/', # SOAPAction
            namespace = "http://tempuri.org/FeriadoDS.xsd",
            trace = True)
        dt1 = datetime.today() - timedelta(days=60)
        dt2 = datetime.today() + timedelta(days=60)
        feriadosXML = client.FeriadosEntreFechasAsXml(dt1=dt1.isoformat(), dt2=dt2.isoformat());
        print feriadosXML


Autor / Autores:
::::::::::::::::

MarianoReingart_

.. ############################################################################

.. _Factura Electronica: http://www.nsis.com.ar/public/browser/pyafip/ws/php.py

.. _simplexmlelement: /simplexmlelement
.. _simplesoapclient: /Recetario/simplesoapclient
.. _marianoreingart: /marianoreingart
