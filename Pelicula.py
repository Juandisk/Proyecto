import json 
import os
import sys 

favoritas = []
historial = []

def main (): 
    print("Iniciando...")

    print("Programa iniciado correctamente")

if __name__ == "__main__":
    main()

import json 
import os 

def cargar_peliculas():
    try: 
        if not os.path.exists('peliculas_json.json'):
            print("Error: No se ha encontrado el archivo 'peliculas_json.json'")
            print("Porfavor asegurate que esté en la guardado en la carpeta proyecto")
            return None
        
        with open('peliculas_json.json', 'r', encoding='utf-8') as archivo: 
            peliculas = json.load(archivo)

        if not peliculas:
            print("Error: El archivo json no se ha encontrado o esta vacio")
            return None
        
        return peliculas
    
    except json.decoderError as e: 
        print(f"Error: El archivo json puede que tenga un formato incorrecto")
        print(f"Detalle del error: {e}")


    
        
