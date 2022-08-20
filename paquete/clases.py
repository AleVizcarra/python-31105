class Persona():

    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
    
    def saludar(self):
        print(f'Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años')