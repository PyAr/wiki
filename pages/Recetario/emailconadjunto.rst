.. title: Email con Adjunto


Descripción
:::::::::::

Esta receta es un ejemplo sencillo de como enviar un email, con una parte de texto y otra binaria (adjunto)

Ejemplo:
::::::::

.. code-block:: python

    # -*- coding: iso-8859-1 -*-
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from smtplib import SMTP

    msg = MIMEMultipart()
    msg['Subject'] = 'Esto es una prueba'
    msg['From'] = 'yo@example.com'
    msg['Reply-to'] = 'responder-aca@example.com'
    msg['To'] = 'vos@example.com'

    # Esto es lo que se ve si uno no tiene un lector de mails como la gente:
    msg.preamble = 'Mensaje de multiples partes.\n'

    # Esta es la parte textual:
    part = MIMEText("Hola, te paso un archivo interesante")
    msg.attach(part)

    # Esta es la parte binaria (puede ser cualquier extensión):
    part = MIMEApplication(open("factura.pdf","rb").read())
    part.add_header('Content-Disposition', 'attachment', filename="factura.pdf")
    msg.attach(part)

    # Se pueden seguir agregando partes (texto, imágenes, datos binarios, etc.)

    # Crear una instancia del servidor para envio de correo (hacerlo una sola vez)
    smtp = SMTP("smtp.example.com")
    # Iniciar sesión en el servidor (si es necesario):
    smtp.ehlo()
    smtp.login("yo@example.com", "mipassword")

    # Enviar el mail (o los mails)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())


Autor / Autores:
::::::::::::::::

MarianoReingart_

.. _marianoreingart: /marianoreingart
