.. title: Test Formulario Con File Upload en Django


un ejemplo de como probar un formulario que tiene un campo para subir un archivo

::

    from django.test.client import Client
    from django.core.files.uploadedfile import SimpleUploadedFile

    client = Client()
    client.login(username=username, password=password)
    data = {'campo1': 'valor1',
            'campo2': 'valor2',
            'archivo': SimpleUploadedFile('nombre_de_archivo','contenido de archivo'),
    }

    response = c.post('/path/al/form', data)
    assert response.status_code == 200

