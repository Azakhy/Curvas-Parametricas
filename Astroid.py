import numpy as np
import matplotlib.pyplot as plt
#Funcion 1
def x(t):
    return np.cos(t)**3
def y(t):
    return np.sin(t)**3
# Funcion 2
def x2(t):
    return 1/8*(3*np.cos(t)-np.cos(3*t))
def y2(t):
    return 1/8*(3*np.sin(t)+np.sin(3*t))


# Crear un rango de valores para t
t = np.linspace(0, 2 * np.pi, 400)

# Graficar las funciones
plt.figure()
plt.plot(x(t), y(t), label='Astroid')
plt.plot(x2(t), y2(t), label='Astroid Involute')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()