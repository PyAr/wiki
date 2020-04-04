.. title: Cdpedia On Android

Cdpedia-on-android es una aplicación android que permite correr la Cdpedia en este sistema operativo.

Para que funcione correctamente es necesario tener descomprimido (no soporta el archivo .iso) alguno de los releases de la cdpedia en la carpeta /mnt/sdcard/cdpedia. A continuación una mini receta:

::

   mount -t iso9660 -o loop cdpedia-0.8-cd.iso /mnt
   cp -R /mnt/cdpedia /media/android_sdcard
   sync
   umount /mnt

Si querés probar la primera versión de la aplicación para android, podés descargarte el .apk desde
`acá <http://cdpedia.python.org.ar/CDPedia-release.apk>`_.


