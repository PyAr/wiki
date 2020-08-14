.. title: pasarrecaptcha.rst

**(Por Carlos Bustillo)**

# Superar la prueba "I'm not a robot" de reCAPTCHA con ayuda pyautogui.

.. image:: /images/Recetario/pasarrecaptcha/captcha.jpg

En este caso vamos a probarlo este código con esta demo api: https://www.google.com/recaptcha/api2/demo .

## Librerías utilizadas:

* pyautogui
* cv2
* time

## Implementación

Realizamos un polling (hace referencia a una operación de consulta constante) para cuando aparezca la imagen de la api demo. Por eso está tomando screenshot de la pantalla cada cierto período de tiempo hasta encontrarlo. Sino lo encuentra después de un cierto valor máximo de tiempo, se detiene la ejecución. Y una vez que encuentra la ventana de la api, hará un rectángulo negro alrededor del objeto "I'm not a robot" detectado y terminará el polling.

.. code-block:: python

    import pyautogui
    import cv2
    import time

    # Cargar plantilla o imagen de referencia
    plantilla = cv2.imread("./captcha.jpg",0)
    w, h = plantilla.shape[::-1]

    # Valores de inicializacion
    min_val = 1     #min_val ronda en valores menores a 1
    cont = 0
    contMax=60
    delay = 1       #1 segundos 

    while ((min_val > 0.015) or (cont==contMax)):      #Generelmente 0.015... es el valor que devuelve cuando no encuentra el objeto
    
        # Realizar screenshot de la pantalla para analizarla
        imagen = pyautogui.screenshot()
        # Para guardar cada screenshot
        imagen.save("screenshot.png")
    
        imagenCopy = cv2.imread("screenshot.png",0)
    
        metodo = eval('cv2.TM_SQDIFF_NORMED')
    
        # Aplicar coincidencia de plantillas
        res = cv2.matchTemplate(imagenCopy,plantilla,metodo)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cont=cont+1
        time.sleep(delay)
    
        print(min_val)
    
        if (min_val < 0.015):
            # Colocar un rectangulo en la imagen blanco y negro -> solo tiene un canal por eso aparece 0 
            # (El rectangulo queda con una especie de color negro en la imagen)
            cv2.rectangle(imagenCopy,top_left, bottom_right, 0, 8)
            cv2.imwrite("./coincidencia.png",imagenCopy)    

Este es el resultado:
            
.. image:: /images/Recetario/pasarrecaptcha/coincidencia.png
            
Una vez detectado el objeto "I'm not a robot" se procede a posicionar el mouse donde éste se encuentre y se procede a dar click.

.. code-block:: python

    import pyautogui

    # Ingresar imagen que debemos buscar
    reCAPTCHAlocation = pyautogui.locateOnScreen('captcha.jpg')

    # Posiciones donde se encuentra el elemento buscado
    reCAPTCHApoint = pyautogui.center(reCAPTCHAlocation)
    reCAPTCHAx, reCAPTCHAy = reCAPTCHApoint

    # Hacer click en las coordenadas encontradas
    pyautogui.click(reCAPTCHAx, reCAPTCHAy)

.. image:: /images/Recetario/pasarrecaptcha/resultado.png

¡Enhorabuena! Lograste superar el reCAPTCHA.
