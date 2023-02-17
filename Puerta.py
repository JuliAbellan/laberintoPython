#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = None
        self.lado1 = None
        self.lado2 = None
    
    def entrar(self):
        if self.abierta:
            print("Puedes pasar al otro lado")
        else:
            print("La puerta esta cerrada")
    
    def esPuerta(self):
        return True
    
    def estaCerrad(self):
        return not self.abierta
    
    def abierta(self):
        return self.abierta
    
    def lado1(self):
        return self.lado1
    
    def lado2(self):
        return self.lado2
    
    def abierta(self, anObject):
        self.abierta = anObject

    def lado1(self, anObject):
        self.lado1 = anObject

    def lado2(self, anObject):
        self.lado2 = anObject


