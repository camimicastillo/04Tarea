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

        #Obtengo k1
        k1x = dt * vx_0
        k1y = dt * vy_0


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
        pass
