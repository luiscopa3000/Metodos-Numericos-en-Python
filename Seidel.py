# -*- coding: utf-8 -*-
"""

@author: Gabriel Condori
"""
# Programamos el método
import numpy as np
def seidel(a,b,tol):
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
    x=[0]*tam
    #Creamos un vector auxiliar para guardar una iteracion anterior
    x0=[0]*tam
    #Creamos un vector errores
    error=[0]*tam
    while True:
        #Calculamos la iteracion
        x1=[]
        suma=0
        for i in range(tam):
            for j in range(tam):
                #Multiplicamos el coeficiente por el valor ya calculado
                suma+=m[i][j]*x[j]
            #Sumamos el coeficiente de la matriz C
            suma+=c[i]
            #Construimos la primera iteracion
            x1.append(suma)
            #!!!!! AQUI LA DIFERENCIA CON JACOBI, actualizamos el valor ya calculado
            x[i]=suma
            #Reinciamos suma para calcular los siguientes valores
            suma=0
            #Calculamos el error respecto al vector auxiliar que guarda la anterior iteracion
            error[i]=x1[i]-x0[i]
        #Buscamos el error máximo
        max_error=0
        for i in error:
            if i>max_error:
                max_error=i
        #Vemos si el error es menor que la tolerancia para salir del ciclo y tener nuestra solucion
        if max_error<tol:
            break
        x0=x1.copy()
        #Contamos las iteraciones
        iteraciones+=1
    return x,iteraciones
    


#Definimos nuestra matriz a y b para procesarlas
#a=[[10,-1,0],[-1,10,-2],[0,-2,10]]
#b=[9,7,6]   
#a=[[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]]
#b=[6,6,6,6,6]      
#a=[[10,2,-1],[-3,-6,2],[1,1,5]]
#b=[27,-61.5,-21.5]   
a=[[15,-3,-1],[-3,18,-6],[-4,-1,12]]
b=[3800,1200,2350]  
#Nos damos una tolerancia o error
tolerancia=0.05
#Llamamos a nuestro metodo
x,nro_iteraciones=seidel(a,b,tolerancia)
print("************************MÉTODO DE SEIDEL*****************************")
print("La solucion se encontro en: ",nro_iteraciones,"iteraciones")
print("El vector x solucion es: ",x)
for i in range(len(a)):
    print("x",i+1," = ",x[i])