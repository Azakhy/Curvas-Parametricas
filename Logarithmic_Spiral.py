import numpy as np
import matplotlib.pyplot as plt

b = 0.3

def x(t):
    return np.cos(t)*np.exp(b*t)
def y(t):
    return np.sin(t)*np.exp(b*t)
# Funcion 2
def x2(t):
    return (np.sin(t)*np.exp(b*t))/b
def y2(t):
    return -(np.cos(t)*np.exp(b*t))/b
#Rango de valores para t
t = np.linspace(-5,5)
#Graficar las funciones
plt.figure()
plt.plot(x(t), y(t), label='Logarithmic Spiral')
plt.plot(x2(t), y2(t), label='Logarithmic Spiral Involute')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()