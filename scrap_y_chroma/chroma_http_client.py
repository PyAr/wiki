import chromadb

cliente = chromadb.HttpClient(host='127.0.0.1', port=8010)


collection = cliente.get_collection('pyar_searchbar_collection')

print(collection.query(
  query_texts='hola python',
  include=['documents', 'metadatas']
))
