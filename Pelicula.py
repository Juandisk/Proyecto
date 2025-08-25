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
        return None
    except Exception as e: 
        print(f"Eror inesperado: {e}")
        return None 

def mostrar_estadisticas_carga(peliculas):
    if not peliculas: 
        return 
print("\n ESTADISTICAS DE CARGA:")
print("=" * 30)

total_peliculas = 0 
for genero, lista_peliculas in peliculas.items():
    cantidad = len(lista_peliculas)
    total_peliculas += cantidad
    print(f"{genero.replace('_',' ').title()}: {cantidad} peliculas")

print("=" * 30)
print(f"Total de peliculas: {total_peliculas}")

mejor_pelicula = None 
mejor_rating = 0

for genero in peliculas.values(): 
    for pelicula in genero:
        if pelicula['rating'] > mejor_rating:
            mejor_rating = pelicula['rating']
            mejor_pelicula = pelicula 

if mejor_pelicula:
    print(f"Mejor calificada: {mejor_pelicula['titulo']}({mejor_rating}/10)")

def main():
    print("NETFLIX CONSOLE - Cargando datos...")
    print("=" * 50)

    print("Cargando peliculas desde peliculas.json...")
    pelicula = cargar_peliculas()

    if peliculas: 
        print("¡Películas cargas exitosamente!")
        mostrar_estadisticas_carga(peliculas)
    else:
        print("Error: No se pudieron cargar las peliculas")
        print("Revisa que el archivo peliculas.json esté en la carpeta correcta")
        return
    print("\n Sistema listo para usar")

if__name__="__main__"
main()

import json 
import os 

def cargar_pelicula():
    try:
        if not os.path.exists('peliculas.json'):
            print("Error: No se encontró el archivo 'peliculas.json'")
            print("Asegúrate de que esté en la misma carpeta que main.py")
            return None 

        with open('peliculas.json','r', encoding="UTF=8") as archivo:
            pelicula = json.load(archivo)

        if not peliculas: 
            print("Error: El archivo JSON está vacio")
            return None
        
        return peliculas 
    
    except json.JSONDecodeError as e: 
        print(f"Error: El archivo JSON tiene formato incorrecto")
        print(f"Detalle del error: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado")
        return None
    
    def mostrar_estadisticas_carga(peliculas):
        if not peliculas:
            return
        
    print ("\n ESTADÍSTICAS DE CARGA:")
    print("=" * 30)


