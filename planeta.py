#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.

        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecuacion_de_movimiento(self):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        G=1
        M=1
        m=1

        x, y, vx, vy = self.y_actual

        r = ((x**2 + y**2) ** (0.5))

        fx = (-x)*( G*M*m / r**3 - 2 * self.alpha *G*M*m / r**4)
        fy = (-y)*( G*M*m / r**3 - 2 * self.alpha *G*M*m / r**4)

        return [vx, vy, fx, fy]

    def avanza_euler(self, dt):
        '''
        Toma la condición actual del planeta y avanza su posicion y velocidad
        en un intervalo de tiempo dt usando el método de Euler explícito. El
        método no retorna nada, pero re-setea los valores de self.y_actual.
        '''
        vx, vy, fx, fy = self.ecuacion_de_movimiento()
        x_nuevo = self.y_actual[0] + vx * dt
        y_nuevo = self.y_actual[1] + vy * dt
        vx_nuevo = self.y_actual[2] + fx * dt
        vy_nuevo = self.y_actual[3] + fy * dt

        self.y_actual = [x_nuevo, y_nuevo, vx_nuevo, vy_nuevo]
        self.t_actual += dt

        pass

    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta 4.
        '''

        #Obtengo condiciones iniciales
        x_0, y_0, vx_0, vy_0 = self.y_actual

        #Obtengo la funcion para luego obtener k1
        f1=self.ecuacion_de_movimiento()
        k1vx = dt* f1[0]
        k1vy = dt* f1[1]
        k1fx = dt* f1[2]
        k1fy = dt* f1[3]
        #Actualizar valores para calcular k2
        self.y_actual=[x_0 + k1vx /2. , y_0 + k1vy /2. , vx_0 + k1fx /2., vy_0 + k1fy /2.]

        #Obtengo la funcion para luego obtener k2
        f2=self.ecuacion_de_movimiento()
        k2vx = dt* f2[0]
        k2vy = dt* f2[1]
        k2fx = dt* f2[2]
        k2fy = dt* f2[3]
        #Actualizar valores para calcular k3
        self.y_actual=[x_0 + k2vx /2. , y_0 + k2vy /2. , vx_0 + k2fx /2., vy_0 + k2fy /2.]

        #Obtengo la funcion para luego obtener k3
        f3=self.ecuacion_de_movimiento()
        k3vx = dt* f3[0]
        k3vy = dt* f3[1]
        k3fx = dt* f3[2]
        k3fy = dt* f3[3]
        #Actualizar valores para calcular k4
        self.y_actual=[x_0 + k3vx , y_0 + k3vy , vx_0 + k3fx, vy_0 + k3fy]

        #Obtengo la funcion para luego obtener k3
        f4=self.ecuacion_de_movimiento()
        k4vx = dt* f4[0]
        k4vy = dt* f4[1]
        k4fx = dt* f4[2]
        k4fy = dt* f4[3]


        x_nuevo = x_0 + (1/6.)*(k1vx+2*k2vx+2*k3vx+k4vx)
        y_nuevo = y_0 + (1/6.)*(k1vy+2*k2vy+2*k3vy+k4vy)
        vx_nuevo = vx_0 + (1/6.)*(k1fx+2*k2fx+2*k3fx+k4fx)
        vy_nuevo = vy_0 + (1/6.)*(k1fy+2*k2fy+2*k3fy+k4fy)

        #Se actualizan los valores de la condicion inicial y se avanza un dt
        self.y_actual = [x_nuevo, y_nuevo, vx_nuevo, vy_nuevo]
        self.t_actual += dt
        pass

    def avanza_verlet(self, dt):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''
        

        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        G=1
        M=1
        m=1
        #Obtener condiciones iniciales
        x, y, vx, vy = self.y_actual
        vx, vy, fx, fy = self.ecuacion_de_movimiento()

        r = ((x**2 + y**2)**(0.5))

        #Energia=T+U
        self.energia_t = (m*(vx**2 + vy**2))*0.5 - G*M*m / r + self.alpha*G*M*m / r**2

        pass
