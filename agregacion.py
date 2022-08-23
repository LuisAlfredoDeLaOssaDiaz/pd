class Libro():
    def __init__(self, titulo, autor) -> None:
        self.titulo=titulo
        self.autor=autor

    def __repr__(self) -> str:
        return f'El Libro es {self.titulo} por {self.autor}'

class Biblioteca():
    def __init__(self, nombre, ciudad):
        self.nombre=nombre
        self.ciudad=ciudad
        self.libro=None

    def MuestraBiblioteca(self):
        print(self.nombre)
        print(self.ciudad)

        if self.libro==None:
            print('Dona Libros a la biblioteca.')
        else:
            print(self.libro)

    def AgregaLibro(self, libro):
        if isinstance(libro, Libro):
            self.libro=libro
        else:
            print('Coloca un libro')

# Creamos un libro
libro1=Libro('Programacion avanzada', 'Nicosio')

# Creamos la biblioteca
biblioteca1=Biblioteca('Biblioteca Central', 'NYC')

biblioteca1.MuestraBiblioteca()

print ('-----')

biblioteca1.AgregaLibro(libro1)
biblioteca1.MuestraBiblioteca()

print ('-----')

biblioteca1.AgregaLibro("hola")
