import random


class Auto:
    #Constructor Auto
    def __init__(self, mk, tr, yr):
        self.marca = mk
        self.model = tr
        self.fecha = yr
        self._kilom = random.randint(0,10)
        
    #Getter km
    def leer_km(self):
        return self._kilom


    def __str__(self):
        return(f"Marca: {self.marca}\nModelo: {self.model}\nFecha: {self.fecha}\nkmtraje: {self.leer_km()}")


class ElectricCar(Auto):
    #Contructor ElectricCar
    def __init__(self, mk, tr, yr):
        #Heredar las propiedades de la clase Auto
        Auto.__init__(self,mk, tr, yr)
        self.carga = random.randint(1,100)

    #Imprimir la carga
    def leer_carga(self):
        print(self.carga)
     
     
    def __str__(self):
        return(f"Marca: {self.marca}\nModelo: {self.model}\nFecha: {self.fecha}\nkmtraje: {self.leer_km()}\nCarga: {self.carga}\n\n")


class Tesla:
    #Constructor de Tesla
    def __init__(self, trims):
        self.linea = list()
        for modelo in trims:
            #Iterar en cada elemento de la lista pasada como argumento 
            nuevo = ElectricCar("Tesla", modelo, random.randint(2009, 2020))
            self.linea.append(nuevo)
        
    
    def __str__(self):
        cadena = ""
        #Iterar en cada elemento(ElectricCar) almacenado en la lista
        for x in self.linea:
            cadena += f"Marca: {x.marca}\nModelo: {x.model}\nFecha: {x.fecha}\nkmtraje: {x.leer_km()}\nCarga: {x.carga}\n\n"
        
        return cadena


#Pruebas de la plantilla
a3 = ElectricCar("Audi", "A3", 1923)
print(a3)

modelos = ["Model 3", "Roadster", "Model X"]
print("\n" + "=" * 20 + "\n")

linea_final = Tesla(modelos)
print(linea_final)
