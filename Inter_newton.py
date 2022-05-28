# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:00:00 2021

@author: IBM GAMER
"""

def genera_niveles_newton(x,y):
     niveles=[]
     polinomio=[]
     niveles.append(y)
     tam=len(y)-1
     esc=tam+1
     cont=0
     salto=0
     for i in range(tam):
         esc-=1
         aux_niv=[]
         aux_y=niveles[cont].copy()
         cont+=1
         salto+=1
         for j in range (esc):
             aux_niv.append((aux_y[j+1]-aux_y[j])/(x[j+salto]-x[j]))
         niveles.append(aux_niv.copy())
             
     for i in niveles: 
         polinomio.append(i[0])
     return niveles,polinomio
 
def calcular_nodo_newton(x,polinomio,nodo):
     suma=0
     itera=-1
     tam=len(polinomio)
     for i in range(tam):
         itera+=1
         mul=polinomio[i]
         for j in range(itera):
             mul*=(nodo-x[j])
         suma+=mul
     return suma
 
x=[1.6,2,2.5,3.2,4,4.5]
y=[2,8,14,15,8,2]
nodo=2.8

niveles, polinomio=genera_niveles_newton(x, y)
resultado=calcular_nodo_newton(x, polinomio, nodo)
print("*********** MÉTODO DE NEWTON **************")
print("Nodo a calcular:",nodo)
print("Resultado",resultado)
 
    
 
    
 
    
 
    
 
    
 
    