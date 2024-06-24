import uuid
import csv

class PYAR:
    """
    Dataset con la informacion del ABC Consultas Frecuentes de AFIP
    
    Metodos que incluye la clase:
        - build_data -> Construye el dataset con informacion del archivo de datos csv
        - get_data -> Retorna la informacion del dataset
    """
    def __init__(self, data_path:str='./data/url_content_searchbar.csv', collection_name:str='pyar_searchbar_collection', auto_build:bool=True) -> None:
        self.data_path = data_path
        self.collection_name = collection_name
        self.preguntas = []
        self.respuestas = []
        self.ids = []

        if auto_build:
            self.build_data()

    def build_data(self):
        """ 
        Extrae la informacion del archivo de datos csv y la almacena dentro los arrays 'preguntas', 'respuestas' y 'ids'
        """

        with open(self.data_path, 'r', encoding='utf-8') as input_file:
            csv_reader = csv.reader(input_file, delimiter=';')
            
            #omitir el header
            _ = next(csv_reader)    
            
            for line in csv_reader:
                pregunta = line[0]
                respuesta = line[1]
                
                self.preguntas.append(pregunta)
                self.respuestas.append(respuesta)
                #ids ficticios
                self.ids.append(str(uuid.uuid4()))
                           
    def get_data(self):
        """
        Retorna un diccionario con informacion relacionada al dataset
        
        ```python
        return {
            'collection_name': str,
            'documents': list[str],
            'doc_info': list[str]
            'metadatas': list[dict],
            'ids': list[str],
            'count': int
            }
        ```
        - collection_name: string con el nombre de la coleccion para acceder a la base de datos
        - documents: lista de preguntas del abc
        - metadatas: lista que contiene diccionarios de estructura:
        
            ```python
            [{'preguntas': pregunta, 'respuestas': respuesta}, ...]
            ```
        
        - ids: ids unicos de cada pregunta
        - count: cantidad de datos que contiene el dataset
        """
        
        return {
            'collection_name': self.collection_name,
            'documents': self.preguntas,
            'doc_info': ['pregunta', 'respuesta'],
            'metadatas': [
                {'pregunta':pregunta, 'respuesta':respuesta} for pregunta, respuesta in zip(self.preguntas, self.respuestas)
                ],
            'ids': self.ids,
            'count': len(self.preguntas)
        }


   
if __name__== '__main__':
    
    abc = ABC()
    abc.build_data()
    print(abc.get_data())