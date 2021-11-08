#Lista input
lista = [1 , -12 , 3 , 34 , -5 , 6 , 7 , 48 , -19]

#Variable que almacena la cantidad de números divisibles por 3
contador = 0

for q in lista:
    if(q%3 == 0):
        contador += 1
        
        
print(f"Divisibles entre 3: {contador}")
   
