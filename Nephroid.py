import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return 1/2*(3*np.cos(t)-np.cos(3*t))
def y(t):
    return 1/2*(3*np.sin(t)-np.sin(3*t))
# Funcion 2
def x2(t):
    return 4*(np.cos(t)**3)
def y2(t):
    return 3*np.sin(t)+np.sin(3*t)
#Rango de valores para t
t = np.linspace(-5,5)
#Graficar las funciones
plt.figure()
plt.plot(x(t), y(t), label='Nephroid ')
plt.plot(x2(t), y2(t), label='Nephroid Involute')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()