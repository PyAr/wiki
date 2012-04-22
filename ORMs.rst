== ORMs ==

=== Que es? ===
El mapeo objeto-relacional (más conocido por su nombre en inglés, Object-Relational mapping, o sus siglas O/RM, ORM, y O/R mapping) es una técnica de programación para convertir datos entre el sistema de tipos utilizado en un lenguaje de programación orientado a objetos y el utilizado en una base de datos relacional, utilizando un motor de persistencia. En la práctica esto crea una base de datos orientada a objetos virtual, sobre la base de datos relacional. Esto posibilita el uso de las características propias de la orientación a objetos (básicamente herencia y polimorfismo). Hay paquetes comerciales y de uso libre disponibles que desarrollan el mapeo relacional de objetos, aunque algunos programadores prefieren crear sus propias herramientas ORM.

mas información en [[https://es.wikipedia.org/wiki/Mapeo_objeto-relacional|wikipedia]]

=== Alternativas ===

==== Sqlalchemy ====

SQLAlchemy es el toolkit SQL python y mapeador objeto relacional que provee a desarrolladores con el poder completo y la flexibilidad de SQL.

Provee un conjunto completo de conocidos patrones de persistencia de nivel enterprise, diseniados para acceso a base de datos eficiente y de alta performance, adaptado en un lenguaje de dominio especifico simple y pitonico.

[[http://www.sqlalchemy.org/|Pagina del proyecto]]

==== Elixir ====

Elixir es una capa declarativa sobre la librería SQLAlchemy, es una capa bastante fina, que provee la habilidad de crear simples clases en python que mapean directamente a tablas de una base de datos relacionales (este patrón es conocido como el patrón de disenio Active Record), proveyendo muchos de los beneficios de las bases de datos tradicionales sin perder la conveniencia de los objetos python.

Elixir tiene la intención de reemplazar la extensión ActiveMapper de SQLAlchemy, y el proyecto TurboEntity pero no intena reemplazar las características básicas de SQLAlchemy, en su lugar se enfoca en proveer una sintaxis mas simple para definir modelos de objetos cuando no necesitas la expresividad del mapeo manual de definiciones de SQLAlchemy.

[[http://elixir.ematia.de/trac/wiki|Pagina del proyecto]]
