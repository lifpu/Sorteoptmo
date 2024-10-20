#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor Orfeo mas conocido como Seth-Root
  
import random
  
# Programa que emula el sorteo del Kino, no pretendo introducirlos en juegos de azar solo que no he visto nada sobre esto en internet y hace tiempo lo busque y es una de las cosas pendientes que tengo
  
loteria_jugada = [1, 2, 3, 4, 5, 6]
lista_de99 = []
sorteo = 0
 
lista6 = []
 
lista_completa = []
  
 
 
   
while sorteo < 12271512: # Iteramos 10 Veces
   
    num_metidos = 0
    lista99 = range (1 , 49)  # Creamos la lista del 1 a 15, recuerda que range no agrega el ultimo indice
    lista6 = []
    for i in range(1 , 7): # Iteramos 6 Veces
  
 
        lista_de99 = lista99  # Cambiamos el nombre de la lista por si algun error
     
 
        cuantos_hay = len( lista_de99 ) # contamos cuantos elementos hay, recuerda que la lista varia y pierde un elemenrto por ciclo y no queremos ese horrible error de fuera de rango
 
        x = random.randrange(cuantos_hay) # Buscams un numero Aleatorio
     
        lista6.append(x) # Pasamos el numero aleatorio y lo sacamos del Sorteo
     
    print ("Has Jugado", loteria_jugada)
 
    print (lista6)
     
    sorteo += 1
 
     
     
### Esto es lo nuevo, iteramos sobre uno de los 2 kinos el jugado o el ganador y asi verificamos cuantos aciertos tenemos
for h in lista6: # Iteramos sobre el ganador
   
    if h in loteria_jugada:
        num_metidos += 1
           
     
### Aqui la asalida importante
        lista_completa.append(num_metidos)
 
 
 
     
    # estas lineas habian sido agregadas en la entrada anterior aunque realmente no hacian nada, solo si en 20 jugadas pegabas el gordo lo que estaba muy cuesta arriba de acuerdo a las ṕrobabilidades
    if loteria_jugada == lista6:
            print ("En el sorteo:",  sorteo , ", Felicitaciones has ganado" ,      num_metidos)
            print ("Tu jugaste:",  loteria_jugada , "y el ganador es",  lista6 )
             
meti_1 = lista_completa.count(1)
meti_2 = lista_completa.count(2)
meti_3 = lista_completa.count(3)
meti_4 = lista_completa.count(4)
meti_5 = lista_completa.count(5)
meti_6 = lista_completa.count(6)
 
 
 
print ("Has metido",  meti_1 ,"veces 1 en" ,      sorteo)
print ("Has metido",  meti_2 , "veces 2 en" ,      sorteo)
print ("Has metido",  meti_3 , "veces 3 en" ,      sorteo)
print ("Has metido",  meti_4 , "veces 4 en" ,      sorteo)
print ("Has metido",  meti_5 , "veces 5 en" ,      sorteo)
print ("Has metido",  meti_6 , "veces 6 en" ,      sorteo)
