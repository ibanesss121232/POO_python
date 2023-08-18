

class Celular:
    #constructor

    def __init__(self,name,model,camera, year):
        self.name=name
        self.model=model
        self.camera=camera
        self.year=year
    
    #metodos(cuando esta dentro de la clase)

    def Llamar(self):
        return f"Estas llamando desde tu :{self.model}" 


class Estudiante:
    def __init__(self,name, year,grado):
        self.name=name
        self.year=year
        self.grado=grado

    #metodos
    def Estudiar(self):
       print (f"El estudiente {self.name} esta estudiando"
              )


def execute():
    name=input("Digame su nombre:\n")
    year=int(input("Digame su edad:\n"))
    grado=input("Digame su en que grado estas:\n")

    ibañes=Estudiante(name,year,grado)
    print(f"""DATOS DEL ESTUDIANTE: \n\n
        Name:{ibañes.name}\n
        Year:{ibañes.year}\n
        Grado:{ibañes.grado}""")
    estudiar=input()
    if(estudiar.lower()=="estudiar"):
        ibañes.Estudiar()



        


celular1=Celular("samsung","s21","48mp",4)
print(celular1.Llamar())
execute()