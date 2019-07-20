
GmailMail
---------

Este script permite enviar emails a través de GMail. Los emails pueden tener texto plano, HTML y archivos adjuntos (todos opcionales).

**Nota:** :small:`el script lo escribí originalmente en inglés. Debería entenderse, pero pienso traducirlo cuando tenga algo más de tiempo.`

**Archivo:** GmailMail.py

::

    #!/usr/bin/env python

    # requires Python >= 2.5
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.audio import MIMEAudio
    from email.mime.image import MIMEImage
    from email.encoders import encode_base64
    from mimetypes import guess_type
    from os.path import basename

    class GmailMail():
        def __init__(self, gmail_user, gmail_pwd):
            """
            Prepares an instance with basic authentication

            """
            self.gmail_user = gmail_user
            self.gmail_pwd = gmail_pwd

        def getAttachment(self, path, charset='ASCII'):
            contentType, encoding = guess_type(path)

            if contentType is None or encoding is not None:
                contentType = 'application/octet-stream'

            mainType, subType = contentType.split('/', 1)
            _file = open(path, 'rb')

            if mainType == 'text':
                attachment = MIMEText(_file.read(), subType, charset)
            elif mainType == 'message':
                attachment = email.message_from_file(_file)
            elif mainType == 'image':
                attachment = MIMEImage(_file.read(), _subType=subType)
            elif mainType == 'audio':
                attachment = MIMEAudio(_file.read(), _subType=subType)
            else:
                attachment = MIMEBase(mainType, subType)
                attachment.set_payload(_file.read())
                encode_base64(attachment)

            _file.close()

            attachment.add_header('Content-Disposition', 'attachment',
                filename=basename(path))

            return attachment

        def send(self, to, subject, text=u"", html=None, attachments=None, charset="iso-8859-15"):
            """
            Sends an email through Gmail using the authentication
            given to this instance.

            If given, attachments must be a list of paths pointing
            to the files we want to include.

            This script does not embed inline content (multipart/related)

            """
            if charset in ['utf8','utf-8']: #bug?
                from email.charset import add_charset, SHORTEST
                add_charset('utf-8', SHORTEST, None, None)

            if isinstance(text, unicode):
                text = text.encode(charset, 'replace')

            if isinstance(html, unicode):
                html = html.encode(charset, 'replace')

            if attachments is None:
                attachments = []

            if text: plain_part = MIMEText(text, 'plain', charset)
            if html: html_part = MIMEText(html, 'html', charset)

            is_alternative = html and text
            layers = []
            if attachments or is_alternative:
                msg = MIMEMultipart() #mixed
                msg.set_charset(charset)
                msg.preamble = 'This is a multi-part message in MIME format.'
                msg.epilogue = ''
                layers.append(msg)

                if is_alternative:
                    msgAlternative = MIMEMultipart('alternative')
                    msg.attach(msgAlternative)
                    layers.append(msgAlternative)

                if text:
                    layers[-1].attach(plain_part)
                if html:
                    layers[-1].attach(html_part)

            elif text:
                msg = plain_part
            else: #html only
                msg = html_part

            for path in attachments:
                msg.attach(self.getAttachment(path, charset))

            msg['From'] = self.gmail_user
            msg['To'] = to
            msg['Subject'] = subject

            mailServer = smtplib.SMTP("smtp.gmail.com", 587)
            mailServer.ehlo()
            mailServer.starttls()
            mailServer.ehlo()
            mailServer.login(self.gmail_user, self.gmail_pwd)
            mailServer.sendmail(self.gmail_user, to, msg.as_string())
            # Should be mailServer.quit(), but that crashes...
            mailServer.close()


Algunos tests (ejemplos, casos de uso):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Archivo:** GmailMail_tests.py

::

    # -*- coding: utf-8 -*-

    from GmailMail import GmailMail
    from urllib2 import urlopen

    text = u"""\
    Éste es el contenido en modo texto plano
    Tenemos acentos y eñes.

    """
    url = "http://python.com.ar/moin"
    html = urlopen(url).read()

    user = 'XXXXXX@gmail.com' # mi usuario de GMail
    pwd  = '********'         # mi contraseña de GMail

    m = GmailMail(user, pwd)

    print "mandando texto plano solamente"
    m.send(user, u'prueba de sólo texto', text)

    print "mandando html solamente"
    m.send(user, u'prueba con sólo html', html=html)

    print "mandando texto plano y html (sin attachments)"
    m.send(user, u'prueba con texto plano y html (sin attachments)', text, html)

    print "mandando texto plano y attachments"
    m.send(user, u'prueba con texto plano y attachments', text, attachments=['GmailMail.py'])

    print "mandando html y attachments"
    m.send(user, u'prueba con html y attachments', html=html, attachments=['GmailMail.py'])

    print "mandando attachments solamente"
    m.send(user, u'prueba con attachments solamente', attachments=['GmailMail.py'])

    print "mandando todo"
    m.send(user, u'prueba con todo', text, html, attachments=['GmailMail.py'])


Referencias (que recuerdo):
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://docs.python.org/lib/module-email.html  

* http://codecomments.wordpress.com/2008/01/04/python-gmail-smtp-example/  

* http://mg.pov.lt/blog/unicode-emails-in-python.html  

* http://www.peterbe.com/plog/zope-html-emails  

-------------------------



  CategoryRecetas_



.. role:: small
   :class: small

.. _gmailmail: /pages/Recetario/gmailmail
.. _categoryrecetas: /pages/categoryrecetas
