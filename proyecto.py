import json
import os
import sys 

favoritas = []
historial = []

def main(): 
    print("Iniciando el programa, Bienvenido")
    print("Programa iniciado")
    
    
import os
import json

def cargar_peliculas():
    try:
        if not os.path.exists('peliculas.json'):
            print("Error: No se ha encontrado el archivo 'peliculas.json'")
            print("Asegúrate de que esté en la misma carpeta que main.py")
            return None

        with open('peliculas.json', 'r', encoding='utf-8') as archivo:
            peliculas = json.load(archivo)  

        return peliculas

    except json.JSONDecodeError as e:
        print("Error: El archivo JSON tiene un formato incorrecto")
        print(f"Detalle del error: {e}")
        return None

    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def mostrar_estadisticas_carga(peliculas):
    if not peliculas:
        return

    print("\nEstadísticas de carga:")
    print("=" * 30)

    total_peliculas = 0
    for genero, lista_peliculas in peliculas.items():
        cantidad = len(lista_peliculas)
        total_peliculas += cantidad
        print(f"{genero.replace('_', ' ').title()}: {cantidad} películas")

    print("=" * 30)
    print(f"Total de películas: {total_peliculas}")

    mejor_pelicula = None
    mejor_rating = 0

    for genero in peliculas.values():
        for pelicula in genero:
            if pelicula['rating'] > mejor_rating:
                mejor_rating = pelicula['rating']
                mejor_pelicula = pelicula

    if mejor_pelicula:
        print(f"Mejor calificada: {mejor_pelicula['titulo']} ({mejor_rating}/10)")

def main():
    print("Netflix Console - Cargando datos...")
    print("=" * 50)

    print("Cargando películas desde peliculas.json...")
    peliculas = cargar_peliculas()

    if peliculas:
        print("Películas cargadas exitosamente")
        mostrar_estadisticas_carga(peliculas)
    else:
        print("Error: No se pudieron cargar las películas")
        print("Revisa que el archivo peliculas.json esté en la carpeta correcta")
        return

    print("\nSistema listo para usar")

    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')
    def mostrar_header():
        print("=" * 60)
        print("🎬" + " " * 20 + "NETFLIX CONSOLE" + " " * 20 + "🎬")
        print("=" * 60)
        print("Tu plataforma de peliculas favoritas en la consola")
        print("=" * 60)
    def mostrar_menu_pricipal():
        print("\n ¿Que quieres hacer hoy?")
        print("-" * 35)
        print("1. Peliculas de acción")
        print("2. Películas de Comedia")
        print("3. Películas de Terror")
        print("4. Películas de Romance")
        print("5. Películas de Ciencia Ficción")
        print("6. Buscar película específica")
        print("7. Top 10 mejor calificadas")
        print("8. Ver mis películas favoritas")
        print("9. Estadísticas del sistema")
        print("0. Salir del programa")
        print("━" * 35)
    def obtener_apcion_usuario():
        while True: 
            try:
                opcion = input("\n Elige una opción (0-9): ").strip()
                if opcion in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return opcion 
                else:
                    print("Opción no válidar. usa números del 0 al 9.")
            except KeyboardInterrupt: 
                print("\n\n ¡Hasta luego!")
                sys.exit(0)
            except Exception as e:
                print(f"Error: {e}")
    def pausar(): 
        input("\n Presionar Enter para continuar...")
    
    def main():
        
        print("Iniciando Netflix console...")
        peliculas = cargar_peliculas()
        
        if not peliculas:
            print("No se puede continuar sin las películas")
            return
        
        print("Sistema cargado correctamente")
        pausar()

        while True:
            limpiar_pantalla()
            mostrar_header()
            mostrar_menu_pricipal()

            opcion = obtener_apcion_usuario()

            if opcion == "0":
                limpiar_pantalla()
                print("¡Gracias por usar Netflix console!")
                print("¡Que disfrutes viendo películas!")
                print("¡Hasta la próxima!")
                break

            elif opcion == "1":
                print("\n🔥 Has elegido: PELÍCULAS DE ACCIÓN")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "2":
                print("\n😂 Has elegido: PELÍCULAS DE COMEDIA")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "3":
                print("\n👻 Has elegido: PELÍCULAS DE TERROR")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "4":
                print("\n❤️ Has elegido: PELÍCULAS DE ROMANCE")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "5":
                print("\n🚀 Has elegido: PELÍCULAS DE CIENCIA FICCIÓN")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "6":
                print("\n🔍 Has elegido: BUSCAR PELÍCULA")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "7":
                print("\n🏆 Has elegido: TOP 10")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "8":
                print("\n❤️ Has elegido: MIS FAVORITAS")
                print("🚧 Función en desarrollo...")
                pausar()
            
            elif opcion == "9":
                limpiar_pantalla()
                mostrar_header()
                mostrar_estadisticas_carga(peliculas)
                pausar()
                
if __name__ == "__main__": 
    main()