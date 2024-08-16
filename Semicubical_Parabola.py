import numpy as np
import matplotlib.pyplot as plt
#Funcion 1
a = 0.1
def x(t):
    return t**2
def y(t):
    return a*(t**3)
# Funcion 2
def x2(t):
    return (t**2/3)-(8/(27*(a**2)))
def y2(t):
    return -(4*t)/(9*a)


# Rango de valores para t
t = np.linspace(-20, 20)

# Graficar las funciones
plt.figure()
plt.plot(x(t), y(t), label='Semicubical Parabola')
plt.plot(x2(t), y2(t), label='Semicubical Parabola Involute')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()