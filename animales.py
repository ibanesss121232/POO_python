
class Animales:
    def __init__(self,name,type,year):
        self.name=name
        self.type=type
        self.year=year
    def Sonido(self):
        print(f"Este es el sonido de animal {self.name}")

class Domesticos:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def Mostrar_Habilidad(self):
        return f'Mi habilidad es:{self.habilidad}'

#HERENCIA
class Animales_Terrestres(Animales):
    def __init__(self,name,type,year,place):
        super().__init__(name,type,year)
        self.place=place


class Animales_Acuaticos(Animales):
    def __init__(self,name,type,year,type_water,place):
        super().__init__(name,type,year)
        self.type_water=type_water
        self.place=place


class Animales_Domesticos_Terrestres(Animales,Domesticos):
    def __init__(self, name, type,year,habilidad,place):
        Animales.__init__(self,name,type,year)
        Domesticos.__init__(self,habilidad)
        self.place=place

    def Presentarse(self):
       print(f'Hola, soy : {self.name}, y mi habilidad es {super().Mostrar_Habilidad()} y vivo en {self.place}')  #Con "super" siempre accedemos a la clase padre.
                                                                                                                #con "self" accedemos al metodo actual.

""""Para saber las instancia y herencia se utiliza el siguiente
herencia=issubclass(hijo,padre)
instancia=isinstance(roberto,clase)"""





# Leon=Animales_Terrestres("Leon","Felino",23,"africa")
# print(Leon.name)
# Leon.Sonido()

Gato=Animales_Domesticos_Terrestres("gato","felino",2,"captar ratones", "casa")
Gato.Presentarse()