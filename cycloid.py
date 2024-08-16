import numpy as np
import matplotlib.pyplot as plt

a = 2
def x(t):
    return a*(t-np.sin(t))
def y(t):
    return a*(1-np.cos(t))
# Funcion 2
def x2(t):
    return a*(t+np.sin(t))
def y2(t):
    return a*(3+np.cos(t))
#Rango de valores para t
t = np.linspace(-10,10)
#Graficar las funciones
plt.figure()
plt.plot(x(t), y(t), label='Cycloid ')
plt.plot(x2(t), y2(t), label='Cycloid Involute')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()