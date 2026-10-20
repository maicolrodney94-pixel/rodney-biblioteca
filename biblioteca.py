"""Libros y categorías almacenadas"""
from models.libro import Libro

# Lista de libros (usa esta estructura)
#att.maicor cambie algunos libros para qu
libros: list[Libro] = [
    {"titulo": "Cien años de soledad", "autor": "García Márquez",
        "paginas": 471, "disponible": True},
    {"titulo": "Don Quijote", "autor": "Cervantes",
        "paginas": 863, "disponible": False},
    {"titulo": "El principito", "autor": "Saint-Exupéry",
        "paginas": 96, "disponible": True},
    {"titulo": "1984", "autor": "George Orwell",
     "paginas": 328, "disponible": True},
    {"titulo": "El gran Gatsby", "autor": "F. Scott Fitzgerald",
      "paginas": 180, "disponible": True},
    { "titulo": "Moby Dick", "autor": "Herman Melville",
      "paginas": 635, "disponible": False },
    { "titulo": "Orgullo y prejuicio", "autor": "Jane Austen",
      "paginas": 279, "disponible": True },
    { "titulo": "La Odisea", "autor": "Homero",
      "paginas": 541, "disponible": True },
    { "titulo": "Hamlet", "autor": "William Shakespeare",
      "paginas": 160, "disponible": False },
    { "titulo": "El Hobbit", "autor": "J.R.R. Tolkien",
      "paginas": 310, "disponible": True },
    { "titulo": "Cumbres Borrascosas", "autor": "Emily Brontë",
      "paginas": 416, "disponible": True },
    { "titulo": "El Código Da Vinci", "autor": "Dan Brown",
      "paginas": 489, "disponible": False },
    { "titulo": "La Divina Comedia", "autor": "Dante Alighieri",
      "paginas": 798, "disponible": True },
    { "titulo": "El Alquimista", "autor": "Paulo Coelho",
      "paginas": 208, "disponible": True },
    { "titulo": "El Retrato de Dorian Gray", "autor": "Oscar Wilde",
      "paginas": 254, "disponible": False },
    { "titulo": "El Señor de los Anillos", "autor": "J.R.R. Tolkien",
      "paginas": 1178, "disponible": True },
    { "titulo": "La Metamorfosis", "autor": "Franz Kafka",
      "paginas": 201, "disponible": True },
    { "titulo": "El Perfume", "autor": "Patrick Süskind",
      "paginas": 255, "disponible": False },
    { "titulo": "El Nombre de la Rosa", "autor": "Umberto Eco",
      "paginas": 512, "disponible": True },
    { "titulo": "El Diario de Ana Frank", "autor": "Ana Frank",
      "paginas": 283, "disponible": True } 
]
# otras categorías que puedes agregar según tus necesidades
# SET con las categorías disponibles
categorias = {"Ficción", "Ciencia", "Historia", "Poesía", "Biografía", "Aventura", "Fantasía", "Romance"}
# jajaja posdata me gusta mucho la programacion y estoy aprendiendo mucho con este proyecto de bibliotecafa
#quisiera leer mas libros yo solo he leido algunos libros de la lista y me gustaria leer mas libros de la lista y aprender mas sobre los libros y sus autores 