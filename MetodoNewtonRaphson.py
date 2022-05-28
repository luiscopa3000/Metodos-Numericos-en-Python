import sympy as sm
import pandas as pd
from sympy import symbols
from sympy.plotting import plot
#Aqui se ingresan el punto de partida
punto= 31.4159265359
# se define una tolerancia
tolerancia=0.00001

x=sm.Symbol('x')

# Definimos la funcion
#y= sm.exp(x)+(2**-x)+2*sm.cos(x)-6
y= (1/2)+(1/4)*x**2-x*sm.sin(x)-(1/2)*sm.cos(2*x)
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
#Aplicamos el metodo de newton
lista1.append(punto)
funcion_evaluada=y.evalf(subs={x:punto})
lista2.append(funcion_evaluada)
funcion_derivada=sm.diff(y,x).evalf(subs={x:punto})
lista3.append(funcion_derivada)
res1=punto-(funcion_evaluada/funcion_derivada)
lista4.append(res1)
lista5.append(0)
res2=0
while True:
    punto=res1
    funcion_evaluada=y.evalf(subs={x:punto})
    funcion_derivada=sm.diff(y,x).evalf(subs={x:punto})
    res2=punto-(funcion_evaluada/funcion_derivada)
    error=abs((res2-res1)/res2)
    lista1.append(punto)
    lista2.append(funcion_evaluada)
    lista3.append(funcion_derivada)
    lista4.append(res1)
    lista5.append(error)
    if error<tolerancia:
        break

    res1=res2
tabla = pd.DataFrame(list(zip(lista1,lista2,lista3,lista4,lista5)), columns=['x', 'f(x)',"f'(x)",'x_i+1','Error'])
print(tabla)
print("******MÉTODO DE NEWTON RAPHSON*****")
print("Funcion ingresada:  ",y)
print("La raiz encontrada es: ", res2)

plot(y, (x, -3, 3))