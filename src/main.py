
from models.libro import Libro
from data.biblioteca import libros as lista_libros, categorias as conjunto_categorias
from utils.operaciones import mostrar_libros_disponibles
from utils.operaciones import contar_libros, promedio_paginas, agregar_categoria_nueva
continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")
    

    if opcion == "1":
        print("Mostrando libros disponibles...")
        print("cantidad en lista_libros: ", len(lista_libros))
        disponibles = mostrar_libros_disponibles(lista_libros, 10000)
        print("cantidad de libros disponibles: ", len(disponibles))
        for libro in disponibles:
            print(f"{libro['titulo']} - {libro['paginas']} páginas")
    
      
          
    elif opcion == "2":
        try:
            limite = int(input("Ingresa el límite de páginas: "))
            resultados = mostrar_libros_disponibles(lista_libros, limite)
            print(f"Libros con menos de {limite} páginas:")
            
            for libro in resultados:
                print(f"{libro['titulo']} - {libro['paginas']} páginas")
        except ValueError:
            print("Por favor, ingresa un número válido.")
        max_paginas = 400
        # aqui agregamos la funcion de mostrar libros disponibles
        
    elif opcion == "3":
        cantidad_total = contar_libros(lista_libros)
        promedio = promedio_paginas(lista_libros)
        print(f"Cantidad total de libros: {cantidad_total}")
        print(f"Promedio de páginas: {promedio:.2f}")
        print("\n=== ESTADÍSTICAS DE LIBROS ===")
        # aqui agregamos la funcion de contar libros y promedio de paginas
            
    elif opcion == "4":
        nuevacategoria = input("Ingresa la nueva categoría: ")
        agregar_categoria_nueva(conjunto_categorias, nuevacategoria)
        print("que nueva categoria se agrego:", nuevacategoria)
        print("conjunto de categorias actualizado:", conjunto_categorias)
        # Llama contar_libros()
        # aqui agregamos la funcion de agregar categoria nueva
        
    elif opcion == "5":
        continuar = "n"
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")

    print("!Gracias por usar la biblioteca. ¡Hasta luego!")
    # ... y asi hize la funcion de agregar categoria y mostrar libros disponibles y contar libros y promedio de paginas