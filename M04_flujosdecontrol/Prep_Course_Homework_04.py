#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num= 26
if num > 0 :
    print(f"El numero {num} es mayor a 0")
elif num < 0 :
    print(f"El numero {num} es menor a 0")
else:
    print(f"El numero {num} es igual a 0")



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
var1= 15
var2= 1.5
if type(var1)== type(var2):
    print(f"{var1} y {var2} son del mismo tipo de clase, {type(var2)}")
   
else:
    print(f"{var1} y {var2} son de distintos tipos de clases, {var1} es {type(var1)} y {var2} es {type(var2)}")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
valores_enteros= range(1,21)
for numero in valores_enteros:
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
 




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
val=0
while val <= 5:
    potencia=val**3
    print(f"{val} elevado a 3 es = {potencia}")
    val += 1





# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
var= 10
for num in range(1,var + 1):
    print('CICLO',num)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
n=4
if (type(n) == int and n > 0):
    factorial= n
    while (n > 2): 
        n = n - 1
        factorial= factorial * n
print('El factorial es', factorial)





# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
n = 0
while n <= 5:
    print (f" Ciclo {n} de while")
    for i in range(0, n+1 ):
        pass    
    print(f"Ciclo {n} de for")
    n+=1    




# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
n= 0
for i in range(0,10):
    print(f"Ciclo {n} de for")
    while (n <= 10):
        print (f" Ciclo {n} de while")
        n += 1
        break




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
rango = 30
n = 0
primo = True
while(n < rango):
    for div in range(2,n):
        if(n % div == 0):
            primo= False
    if primo:
        print(n)
    else:
        primo = True
    n += 1




# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
rango = 30
n = 0
primo = True
while(n < rango):
    for div in range(2,n):
        if(n % div == 0):
            primo= False
            break
    if primo:
        print(n)
    else:
        primo = True
    n += 1
    





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:
rango = 30
n = 0
primo = True
while(n < rango):
    for div in range(2,n):
        if(n % div == 0):
            primo= False
            print(n)
            # break
    # if primo:
        # print(n)
    else:
        primo = True
    n += 1 

# In[57]:

rango = 30
n = 0
primo = True
while(n < rango):
    for div in range(2,n):
        if(n % div == 0):
            primo= False
            print(n)
            break
    # if primo:
        # print(n)
    else:
        primo = True
    n += 1   
# hace el bucle se rompe cuando se cumple la condicion n % div == 0 y no recore toda la lista, apenas encuentra una coincidencia para. 



# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n=99
divisor=12
while (n <= 300):
    n += 1
    if (n % divisor != 0):
        continue
    print(n)




# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
n = 2
sigue=1
primo = True
while( sigue == 1):
    for div in range(2,n):
        if(n % div == 0):
            primo= False
    if primo:
        print(n)
        print('Para saber el siguiente primo preciona 1')
        if input()!= '1':
            print('fin de la lista')
            break
    else:
        primo = True
    n += 1
    



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:
n= 100
multiplo= False
while(n <= 300 ):
    n += 1
    if(n % 6 == 0):
        multiplo= True
        print(n)
        break


