
Escribe acerca de Recetario/Crypto/BlowfishConBlowfishpy aquí.

::

   ➜  ~  mkdir crypto_example
   ➜  ~  cd crypto_example
   ➜  crypto_example  wget http://www.seanet.com/\~bugbee/crypto/blowfish/blowfish.py3
   ➜  crypto_example  mv blowfish.py3 blowfish.py 

con este codigo

::

    import blowfish

    b = blowfish.Blowfish("secreto aca")
    mensaje = "hola!..."
    cifrado = b.encipher_block(mensaje)

    print "mensaje %s cifrado es %s" % (mensaje, cifrado)


salida:

::

   mensaje hola!... cifrado es 0@�WE

nota: el mensaje a cifrar parece que tiene que tener un largo de 8 (no se mucho de blowfish :D)

