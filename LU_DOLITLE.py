# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 12:00:14 2021

@author: Gabriel Condori
"""
# Programamos el método
import numpy as np

def matrizLU(a):
    m=[]
    tam=len(a)
    L=np.zeros((tam,tam))
    for i in range(tam):
        L[i][i]=1
    fil=1
    col=0
    aux=a.copy()
    while(fil<tam):
        cont = 1
        for i in range(fil, tam):
            #Construimos L
            div = float(aux[i][col]) / float(aux[i - cont][col])
            L[i][col] = div
            #Construimos U
            for j in range(tam):
                aux[i][j] = (-div) * aux[i - cont][j] + aux[i][j]
            cont += 1
        col+=1
        fil+=1
    return np.array(aux),L


def LU(a,b):
    # Descomponemos la matriz a en U y L
    U,L=matrizLU(a)
    #Sacamos la inversa de la matriz L
    inv_l=np.linalg.inv(L)
    #Obtenemos d
    d=np.matmul(inv_l,b)
    #Obtenemos inversa de la matriz U
    inv_u=np.linalg.inv(U)
    #Finalmente obtenemos la solucion X
    x=np.matmul(inv_u,d)
    return x
    
#Definimos nuestra matriz a y b para procesarlas
a=[[8,4,-1],[-2,5,1],[2,-1,6]]
b=[11,4,7]   
#a=[[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]]
#b=[6,6,6,6,6]      
#Nos damos una tolerancia o error
#tolerancia=0.0005
#Llamamos a nuestro metodo
x=LU(a,b)
print("************************MÉTODO DOLITLE (Descomposicion de Matrices)*****************************")

print("El vector x solucion es: ",x)
for i in range(len(a)):
    print("x",i+1," = ",x[i])