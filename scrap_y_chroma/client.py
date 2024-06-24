"""
API REST en Flask
Instrucciones para Windows:
1. Instalar waitress: pip install waitress
2. Ejecutar la aplicación: waitress-serve --port=3000 app:app

@autor: Martinez, Nicolas Agustin
"""
# Importación de módulos necesarios

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import webbrowser, chromadb

# Inicialización de la aplicación Flask
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pyar_search', methods=['POST'])
def query_abc():
    """
    Endpoint para obtener similitudes basadas en el texto proporcionado.
    
    Entrada: JSON con el campo 'text'
    Salida: JSON con las similitudes encontradas o un objeto JSON vacío en caso de error

    
    """
    collection_name = 'pyar_searchbar_collection'
    collection = client.get_collection(collection_name)
    
    # Obtener datos del cuerpo de la solicitud
    #data:dict = request.json
    #print('DENTRO DE query_abc() EN APP.py')
    data = request.json
    print('data:', data)
    # Si no hay datos, retornar None
    if not data:
        return None
    
    # Extraer el texto del JSON
    pregunta:str = data['pregunta']

    # Intentar obtener similitudes y devolver la respuesta
    try:
        response:chromadb.QueryResult = collection.query(
            query_texts=pregunta, 
            n_results=5,
            include=['documents', 'metadatas', 'distances'])
        
        #return response
        print(response)
        return jsonify(response)
    
    except Exception as e:
        # Imprimir el error y devolver un objeto JSON vacío
        print('Error al obtener similitudes:', e)
        return {}

if __name__ == '__main__':
    #webbrowser.open('http://localhost:8010')

    client = chromadb.HttpClient(host='127.0.0.1', port=8010)
    # Habilitación de CORS para la aplicación

    CORS(app)

    # (Opcional) Para montar la API en línea, descomentar la siguiente línea
    # run_with_ngrok(app)

    app.run(host='localhost', port=5500, debug=True)