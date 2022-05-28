# GRUPO 21 INTEGRACION SIMPSON
#UNIVERSIDAD MAYOR DE SAN ANDRES
#       INFORMATICA
#MAMANI CALAMABI ELIAS
#PARI YUJRA VICTOR LENIN
#RAMOS ZAPANA FABIO JUAN

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def simpson(ec,a,b,inter):
     print("***************** MÉTODO DE SIMPSON 1/3 *****************")
     x = sp.Symbol('x')
     print(a,b,inter)
     h=(b-a)/inter
     #print(h)
     vx=list(np.linspace(a,b,inter+1))
     vy=[]
     func=ec.replace("^","**")
     func=sp.sympify(func)
     for i in vx:
         vy.append(func.subs(x,i))
     #h=vx[2]-vx[1]
     sumaimp=0
     sumapar = 0
     for i in range(1,inter):
         if i%2==0:
             sumapar+=vy[i]
         else:
             sumaimp += vy[i]
    ######## FORMULA DE SIMPSON COMPUESTO
     print(vx)
     integral=(h/3)*(vy[0]+vy[inter]+(2*sumapar)+(4*sumaimp))
     
     print()
     print("LA FUNCIÓN ES : ",func)
     print("x = ",vx)
     print("y = ", vy)
     print("h= ",h)
     print()
     print("EL AREA ES DE : ",integral)
     
     graficar(vx,vy)

def integrar(ec,a,b):
     print("***************** SOLUCIÓN REAL *****************")
     x = sp.Symbol('x')
     func = ec
     func = func.replace("^", "**")
     eva = sp.sympify(func)
     print("FUNCIÓN INGRESADA : ",eva)
     integral = sp.integrate(eva, (x, a, b))
     print("FUNCIÓN INTEGRADA QUAD : ",integral.evalf())
     
def graficar(x,y):
    #x_gra=np.linspace(x[0],x[len(x)-1],1000)
    #y_gra=np.linspace(y[0],y[len(x)-1],1000)
    #plt.plot(x_gra, y_gra,'-', 'b')
    #plt.title("GRÁFICA")
    plt.ylim(2, 3)
    #plt.xlim()
    plt.plot(x, y,'-', 'b')
    
    plt.show()
     
ec=input("INGRESE UNA ECUACION : ")
a=float(input("INGRESE UNA LIMITE INFERIOR (a) : "))
b=float(input("INGRESE UNA LIMITE SUPERIOR (b) : "))
inter=int(input("INGRESE UNA NRO DE INTERVALOS: "))

print()
simpson(ec,a,b,inter)
print()
integrar(ec,a,b)
