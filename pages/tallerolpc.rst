
Taller OLPC
===========

Para bajar la charla y todos los ejemplos:

::

   svn checkout http://charla-pygame.googlecode.com/svn/trunk/ charla-pygame

Módulo OLPCGames: http://dev.laptop.org/~mcfletch/OLPCGames/OLPCGames-1.6.zip

Imagen de Qemu:

* http://xs-dev.laptop.org/~cscott/xo-1/streams/ship.2/build659/devel_ext3/olpc-redhat-stream-ship.2-build-659-20080229_1949-devel_ext3.img.bz2

* http://pilgrim.laptop.org/~pilgrim/olpc/streams/update.1/build708/devel_ext3/xo-1-olpc-stream-update.1-devel_ext3.img.bz2

Migrando juegos en pygame a XO: http://wiki.laptop.org/go/Porting_pygame_games_to_the_XO

-------------------------



Thread en PyAr_ sobre LiveCDs: http://article.gmane.org/gmane.org.user-groups.python.argentina/13266

* Instalar qemu y kqemu. En ubuntu:

::

   sudo apt-get install qemu kqemu-source kqemu-common
   sudo module-assistant prepare kqemu
   sudo module-assistant auto-install kqemu
   sudo modprobe kqemu

* bajarse y descomprimir la imagen de olpc:

::

   mkdir ~/olpc
   cd ~/olpc
   wget http://xs-dev.laptop.org/~cscott/xo-1/streams/ship.2/build659/devel_ext3/olpc-redhat-stream-ship.2-build-659-20080229_1949-devel_ext3.img.bz2
   bunzip xo-1-olpc-stream-update.1-devel_ext3.img.bz2
   chmod -w xo-1-olpc-stream-update.1-devel_ext3.img

* crear la imagen "Copy on Write" de qemu:

::

   mkdir /tmp/olpc
   cd /tmp/olpc
   qemu-img create -b ~/olpc/xo-1-olpc-stream-update.1-devel_ext3.img -f qcow olpc.img

* bootear qemu:

::

   cd /tmp/olpc
   qemu -m 256 -kernel-kqemu -soundhw es1370 -net user -net nic,model=rtl8139 -hda olpc.img

.. ############################################################################


.. _pyar: /pages/pyar
