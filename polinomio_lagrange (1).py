import numpy as np
import sympy as sp
def generar_polinomio_lagrange(datos_x,datos_y,nodo):
     inter=[]
     suma=0
     x=sp.Symbol('x')
     tamaño_x=len(datos_x)
     for i in range(tamaño_x):
         numerador=1
         denominador=1
         for j in range(tamaño_x):
             if i!=j:
                 numerador*=(x-datos_x[j])
                 denominador*=(datos_x[i]-datos_x[j])
         inter.append(numerador/denominador)
     for i in range(len(datos_y)):
         suma+=(datos_y[i]*inter[i])
     polinomio=sp.simplify(suma)
     print ("POLINIOMIO DE LAGRANGE: ",str(polinomio).replace("**",'^'))
     print ("POLINOMIO EVALUADO EN EL PUNTO",nodo,"es: ",polinomio.subs(x,nodo))
     return inter

#x=[-2,-1,0,2,3]
#y=[-15,-2,1,1,10]
#nodo=1
#x=[0,1,2,4]
#y=[5,8,1,5]
#x=[-1,0,1,2,3]
#y=[-1,3,0,-13,18]
#x=[1,2,3,5,7,8]
#y=[3,6,19,99,291,444]
x=[-3, -1, 0, 1,2,3,5]
y=[-588, -1, 3, 0,-13,18,1388]
nodo= 7
print("**************** MÉTODO DE LAGRANGE ***************")
generar_polinomio_lagrange(x,y,nodo)
