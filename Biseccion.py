import math
ecuacion = input('ingrese la funcion a resolver')
xa = float(input('ingrese la cota inferior: '))
xb = float(input('ingrese la cota superior: '))
tolerancia = float(input('ingrese la tolerancia: '))

def f(x):
    return eval(ecuacion)
iter = 0
f_c = 999999
while abs(f_c)>=tolerancia:
    puntoMedio = (xa + xb)/2
    f_a = f(xa)
    f_b = f(xb)
    f_c = f(puntoMedio)

    iter += 1
    print("x_a: ", xa, "x_b", xb, " c: ", puntoMedio, " f_c", f_c, "N_Iteraciones: ", iter)

    if(f_a * f_c) < 0:
        xb = puntoMedio
    elif(f_b*f_c) < 0:
        xa=puntoMedio

    if abs(f_c)<tolerancia:
        break
print("La Raiz aproximada es: ", puntoMedio)







# x**3+3*x**2+12*x+8  intervalos(-5, 5) tolerancia:0.0001
# x**2-0.5  intervalos(0,1)  tolerancia: 0.0003
# x+3   intervalos(-5,5)  tolerancia: 0.0001
# math.e**(3*x)-4  intervalos (0,1)   tolerancia:0.0001
#2*x*math.cos(2*x)-(x+1)**2
