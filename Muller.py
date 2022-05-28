import sympy as sp
#Aqui se ingresan el punto de partida
x0=1.0
x1=1.2
x2=(x1+x0)/2
# se define una tolerancia
tolerancia=0.001

x=sp.Symbol('x')
# Definimos la funcion
fx=x**3-x-2
#fx=sp.cos(x)+3*x**4-5
fx0=fx.evalf(subs={x:x0})
fx1=fx.evalf(subs={x:x1})
fx2=fx.evalf(subs={x:x2})
delta0=(fx1-fx0)/(x1-x0)
delta1=(fx2-fx1)/(x2-x1)
h0=x1-x0
h1=x2-x1
a=(delta1-delta0)/(h1-h0)
b=a*h1+delta1
c=fx2
if b>0:
    x3=x2+((-2*c)/(b+sp.sqrt(b**2-4*a*c)))
else:
    x3=x2+((-2*c)/(b-sp.sqrt(b**2-4*a*c)))
while True:
    x_anterior=x3
    x0=x1
    x1=x2
    x2=x3
    print(x3)
    fx0=fx.evalf(subs={x:x0})
    fx1=fx.evalf(subs={x:x1})
    fx2=fx.evalf(subs={x:x2})
    delta0=(fx1-fx0)/(x1-x0)
    delta1=(fx2-fx1)/(x2-x1)
    h0=x1-x0
    h1=x2-x1
    a=(delta1-delta0)/(h1-h0)
    b=a*h1+delta1
    c=fx2
    if b>0:
        x3=x2+((-2*c)/(b+sp.sqrt(b**2-4*a*c)))
    else:
        x3=x2+((-2*c)/(b-sp.sqrt(b**2-4*a*c)))
    error=abs((x3-x_anterior)/x3)
    if (error<tolerancia or fx2==0):
        break
print("*********** METODO DE MULLER **************")
print("La raiz encontrada es:",x3)
    
def move_spines():
    """Esta funcion divide pone al eje y en el valor 
    0 de x para dividir claramente los valores positivos y
    negativos."""
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

# Importamos la libreria Matplotlib para graficar la funcion
import matplotlib.pyplot as plt
# Importamos la libreria numpy para generar los puntos
import numpy as np
# Generamos varios puntos para ser evaluados y posteriormete graficarlos
# En este caso generamos 100 puntos de x
# linspace genera puntos en un rango: linspace(arg1,arg2,arg3) arg1=limite inferior, arg2= limite superior, arg3=Cantidad de puntos a generar en el intervalo definido

# Ponemos la cuadricula en la gráfica
ax = move_spines()
ax.grid()


# En este caso generamos 100 puntos de x
t = np.linspace(-2, 6, num=100)
# Ponemos la cuadricula en la gráfica
ax = move_spines()
ax.grid()
# Graficamos la funcion dandole el conjunto de coordenadas 
ax.plot(t, [fx.subs(x,i).evalf() for i in t])
# Le podemos poner un titulo
plt.title(r"Grafico de $f(x)=x^3+2x^2+10x-20}$")
# Le ponemos titulo al eje y = f(x)
plt.ylabel('f(x)')
# Le ponemos titulo al eje x
plt.xlabel('x')
plt.show()