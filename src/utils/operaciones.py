from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    """Calcula el promedio de páginas de todos los libros"""
    total_paginas = 0

    for libro in libros:
        total_paginas += libro["paginas"]

    return total_paginas / len(libros)

# Función para contar la cantidad total de páginas de todos los libros
def contar_libros(lista_libros: list[Libro]):
    
    """Cuenta la cantidad total de libros"""
    # función que cuenta la cantidad total de libros en la lista
    return len(lista_libros)

def mostrar_libros_disponibles(lista_libros: list[Libro], max_paginas: int):
    """Aqui ,mostramos solo los libros que tienen menos de max_paginas"""
    #funcion que filtra los libros disponibles , se 
    return [libro for libro in lista_libros if libro["paginas"] < max_paginas]

def agregar_categoria_nueva(set_categorias: set[str],nueva_categoria: str,):
    print("Agregando nueva categoría...")
    """Aqui agregarenos una categoria nueva al conjunto de categorias"""
    # funcion que agrega una nueva categoria al conjunto de categorias
    if nueva_categoria and nueva_categoria .strip():
        set_categorias.add(nueva_categoria)
        return set_categorias