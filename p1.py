lista = list()

print("Elija una de las siguientes opciones (Si colocas un número distinto, se usará la opción 1):")
print("1. Usar la lista predeterminada")
print("2. Usar una lista propia")
while True:
    try:
        opcion = int(input(""))
    except:
        print("La opción debe ser numérica!!\n")
    else:
        if opcion == 2:
            while True:
                try:
                    largo = int(input("Cuantos elementos deseas incluir: "))
                except:
                    print("La opción debe ser numérica!!")
                else:
                    for _ in range(largo):
                        while True:
                            try:
                                elemento = int(input("Ingresa un número: "))
                            except:
                                print("La opción debe ser numérica!!\n")
                            else:
                                lista.append(elemento)
                                break
                    
                    break
        else:
            lista = [1 , -12 , 3 , 34 , -5 , 6 , 7 , 48 , -19]
            
        break



#Variable que almacena la cantidad de números divisibles por 3
contador = 0

for q in lista:
    if(q%3 == 0):
        contador += 1
        
        
print(f"Divisibles entre 3: {contador}")
   
