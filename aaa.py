import sympy as sm
# Definimos la funcion matematica a traves de una funcion.

def f(x):
  return -0.5*x**2+2.5*x+4.5
# Importamos la libreria Matplotlib para graficar la funcion
import matplotlib.pyplot as plt
# Importamos la libreria numpy para generar los puntos
import numpy as np
# Generamos varios puntos para ser evaluados y posteriormete graficarlos
# En este caso generamos 100 puntos de x
# linspace genera puntos en un rango: linspace(arg1,arg2,arg3) arg1=limite inferior, arg2= limite superior, arg3=Cantidad de puntos a generar en el intervalo definido
x = np.linspace(-20, 20, num=100)
# Funcion para poner la cuadricula
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

# Ponemos la cuadricula en la gráfica
ax = move_spines()
ax.grid()
# Graficamos la funcion dandole el conjunto de coordenadas 
ax.plot(x, f(x))
# Le ponemos titulo al eje y = f(x)
plt.show()

