# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:26:29 2021

@author: IBM GAMER
"""


# Programamos el método
import numpy as np
def jacobi(a,b,tol):
    #Contador de iteraciones
    iteraciones=0
    #Construimos m
    tam=len(a)
    #Creamos una matriz del mismo tamano que la matriz a llenada de ceros 
    m=np.zeros((tam,tam))
    #Creamos el vector o matriz donde se almacenara c
    c=[]
    #Recorremos la matriz m contruyendola
    for i in range(tam):
        for j in range(tam):
            # Con esta condicion dejamos la diagonal principal en 0
            if i != j:
                #Aqui dividimos los coeficientes de la matriz a respecto a la diagonal principal y cambiamos el signo
                m[i][j]=-a[i][j]/a[i][i]
        #Aqui construimos la matriz c
        c.append(b[i]/a[i][i])
    #EMPEZAMOS CON LAS ITERACIONES
    #Nos damos los valores iniciales en un vector todo iniciado en 0
    x=[0]*tam # [0,0,0]
    #Creamos un vector errores
    error=[0]*tam
    while True:
    #for i in range(8):
        #Calculamos la iteracion
        x1=[]
        suma=0
        for i in range(tam):
            for j in range(tam):
                #Multiplicamos el coeficiente por el valor inicial
                suma+=m[i][j]*x[j]
            #Sumamos el coeficiente de la matriz C
            suma+=c[i]
            #Construimos la primera iteracion
            x1.append(suma)
            #Reinciamos suma para calcular los siguientes valores
            suma=0
            #Calculamos el error
            error[i]=abs(x1[i]-x[i])
        #Buscamos el error máximo
        max_error=0
        for i in error:
            if i>max_error:
                max_error=i
        #Vemos si el error es menor que la tolerancia para salir del ciclo y tener nuestra solucion
        if max_error<tol:
            break
        x=x1.copy()
        #Contamos las iteraciones
        iteraciones+=1
    return x,iteraciones
    


#Definimos nuestra matriz a y b para procesarlas
#a=[[10,-1,0],[-1,10,-2],[0,-2,10]]
#b=[9,7,6] 
#a=[[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]]
#b=[6,6,6,6,6]       
#a=[[10,2,-1],[-3,-6,2],[1,1,5]]
#b=[27,-65.5,-21.5]       
a=[[2,-6,-1],[-3,-1,7],[-8,1,-2]]
b=[-38,-34,-20] 
#Nos damos una tolerancia o error
tolerancia=0.00001
#Llamamos a nuestro metodo
x,nro_iteraciones=jacobi(a,b,tolerancia)
print("************************MÉTODO DE JACOBI*****************************")
print("La solucion se encontro en: ",nro_iteraciones,"iteraciones")
print("El vector x solucion es: ",x)
for i in range(len(a)):
    print("x",i+1," = ",x[i])
