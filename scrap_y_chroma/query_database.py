import chromadb

cliente = chromadb.PersistentClient('playground_database')

#cliente.list_collections()
# >>> [Collection(name='mi_coleccion_abc'), Collection(name='mi_coleccion_crm')]

coleccion_abc = cliente.get_collection('pyar_searchbar_collection')
#coleccion_crm = cliente.get_collection('mi_coleccion_crm')

while True:
    resultados_similares = coleccion_abc.query(
        query_texts= input('Ingresa una query >> '),
        n_results= 2
    )
    
    print(resultados_similares)