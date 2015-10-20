#!/usr/bin/env python
# -*- coding: utf-8 -*-

from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt


condicion_inicial = [10, 0, 0, 0.4]

#RUT 18.889.762-2
p = Planeta(condicion_inicial, alpha= 10**(-2.762))

'''
Complete el código a continuación.
'''
#Arreglo del tiempo y el dt
N_pasos = 200000
dt = 20000./N_pasos
t = np.linspace(0, 20000, N_pasos)

#Arreglos para guardar valores de posicion x e y, y energia
x = np.zeros(N_pasos)
y = np.zeros(N_pasos)
E = np.zeros(N_pasos)

#Fijo las condiciones iniciales
x[0] = condicion_inicial[0]
y[0] = condicion_inicial[1]
E[0] = p.energia_total()

for i in range(1,N_pasos):
    #Avanzo posicion y velocidad del planeta en un dt
    p.avanza_verlet(dt)
    #Obtengo los valores de la posicion del planeta, en x y en y
    x[i]=p.y_actual[0]
    y[i]=p.y_actual[1]
    #Calculo la energia del planeta para estos valores (habiendo avanzado en dt)
    p.energia_total()
    E[i] = p.energia_t

fig = plt.figure(1)
fig.clf()
#Grafico Trayectoria de la orbita
ax1=fig.add_subplot(211)
ax1.plot(x,y)
#Grafico Energia vs tiempo
ax2=fig.add_subplot(212)
ax2.plot(t,E)

ax1.set_xlabel('Posicion en X')
ax1.set_ylabel('Posicion en Y')

ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Energia total')

plt.draw()
plt.show()
plt.savefig('verletalpha.png')
