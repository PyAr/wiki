.. title: Infraestuctura

.. class:: alert alert-warning

    El contenido de esta web está en progreso

Nuestro repo github: `https://github.com/PyAr/pyar_infra <https://github.com/PyAr/pyar_infra>`_

Si encontras algún problema por favor reportalo acá --> https://github.com/PyAr/pyar_infra/issues

Contacto:
---------
- vía e-mail a infra@ac.python.org.ar
- *#pyar-infra* en Freenode
- También podes buscar a `gilgamezh`, `tuxman` o `tomasdelvechio` en #pyar o en el `canal de telegram <https://t.me/pythonargentina>`_ de Python Argentina


Actualmente la infraestructura virtual de PyAr esta hosteada en `USLA <http://drupal.usla.org.ar/>`_ . Nuestro enorme agradecimiento a ellos por todos estos años de aguante.

El equipo de infra está manteniendo este sitio web y la lista de correos.

- Para el sitio web tenemos dos containers de LXC, uno ejecutando postgresql y el otro ejecutando la app web.
- Para la lista de correos tenemos un container LXC corriendo `Mailman <http://www.list.org/>`_

Estos 3 containers están configurados manualmente, como 3 pequeñas mascotas que fueron pasando por las manos de diferentes pyarenses
hasta hace un tiempo que llegaron a las manos de @gilgamezh. Uno de los problemas que queremos resolver actualmente es que no existe un proceso automatizado
para generar estos servers y tampoco un proceso automatizado para hacer deploy de la página web.

Para solucionar este problema estamos trabajando en migrar nuestra infra con la filosofia de *infraestructura como código*.
Charla que puede servir de referencia: https://speakerdeck.com/gilgamezh/infrastructure-as-code-docker-en-todos-lados


A dónde vamos:
--------------

- Utilizar containers para desarrollo y producción
- Hacer los cambios necesarios en la web y mailmain para migrar a containers.
- Mantener en el repo de `pyar-infra` Charts de Helm para deployar nuestros servicios en `Kubernetes <http://kubernetes.io/>`_
- Configurar un servicio de CI/CD para ejecutar automaticamente tests y deploys:
    * Merge a master == deploy en staging
    * Nuevo Tag == deploy a producción
- Con la nueva infra vamos a poder levantar nuevos servicios como páginas de PyDays, PyCons, etc de manera muy simple y siempre reproducible.
- De ser necesario podemos migrar entre diferentes cloud providers.
- Pequeños servicios como Bots (lalita) u otros proyectos se pueden deployar y ser mantenidos por nosotros.
- Administrar la infra va a ser más simple y nuevas personas van a poder participar simplemente utilizando nuestro repo de GitHub.

Quíero participar ¿Cómo hago?
-----------------------------

- Contactanos!
- Mira nuestros issues y proponé soluciones: https://github.com/PyAr/pyar_infra/issues
- Agrega mejoras en esta Wiki... _pyar: /pyar
