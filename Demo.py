import sympy as sm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def f(x):
    return x**2 - x + 2

x = np.array([1, 1.5, 1.9, 1.95, 1.99, 1.999, 2.001, 2.05, 2.1, 2.2, 2.5, 3 ])
y = f(x)
tabla = pd.DataFrame(list(zip(x, x,x)), columns=['x', 'f(x)',''])
print(tabla)
