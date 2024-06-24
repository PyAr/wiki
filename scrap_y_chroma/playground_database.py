"""
Crea una nueva coleccion con los datos del pyar. Para realizar queries a la base de datos ejectuar minimo_caso_de_uso.py
"""

import chromadb
from local_datasets import PYAR

cliente = chromadb.PersistentClient('database')

nombre_coleccion_pyar = 'pyar_searchbar_collection'

print('Creando una coleccion con los datos del pyar...')
coleccion_pyar = cliente.create_collection(nombre_coleccion_pyar)


pyar = PYAR()
pyar_data = pyar.get_data()
#para limitar la carga de datos a la base
limit = None

print('\nAsignando valores a la coleccion del pyar..')
for count, (document, metadata, id) in enumerate(zip(pyar_data['documents'], pyar_data['metadatas'], pyar_data['ids'])):
    count += 1

    coleccion_pyar.add(
        documents= document,
        metadatas= metadata,
        ids = id
    )
    if count%100 == 0:
        print(f'Se han agregados {count} valores a la coleccion')

    if limit and count == limit:
        print('Limite de carga de datos alcanzado. Finalizando ..')
        break

else:
    print('Datos del pyar agregados correctamente a la coleccion')
