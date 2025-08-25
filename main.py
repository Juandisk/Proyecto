import json
import os
import sys 

#Dejar texto de iniciado del programa 

favoritas = []
historial = []

def main(): 
    print("Iniciando el programa, Bienvenido")
    print("Programa iniciado")
    
if __name__ == "__main__": 
    main()
    
#Cargar datos json
 
import json
import os

def cargar_peliculas():
    try:
        if not os.path.exists('peliculas.json')
        print("Error: No se a encontrado el archivo 'peliculas_json.json")
        print("Asegurate de que esté en la misma carpeta que main.py")
    return None 

with open('peliculas.json', 'r', encoding='utf-8') as archivo:   
    peliculas = json.load 

    return peliculas    

except json.JSONDecodeError as e:
    print("Error: El archivo JSON tiene un formato incorrecto")
    print(f"Detalle del error: {e}")
    return None
 
except Exception as e: 
    print(f"Error inesperado: {e}")
    return None 

def mostrar_estadisticas_carga:
    if not peliculas: 
    return
    
    print("\n Estadisticas de carga:")
    print("=" * 30)
    
    total_peliculas = 0 
    for genero, lista_peliculas in peliculas.item():
        cantidad = len(lista_peliculas)
        total_peliculas += cantidad 
        print(f"{genero.replace('_','').title()}: {cantidad} peliculas")
    
    print("=" * 30)
    print(f"Total de peliculas: {total_peliculas}")
    
    mejor_pelicula = None 
    mejor_rating = 0 
    
    for genero in peliculas.values(): 
                