#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Habitación(ElementoMapa):
    def __init__(self):
        self.norte = None
        self.este = None
        self.oeste = None
        self.sur = None
        self.num = None
    
    def entrar(self):
        print(f"Estas en la habitacion {self.num}")

    def esHabitacion(self):
        return True
    
    def este(self):
        return self.este
    
    def oeste(self):
        return self.oeste
    
    def sur(self):
        return self.sur
    
    def norte(self):
        return self.norte
    
    def este(self, anObject):
        self.este = anObject
    
    def oeste(self, anObject):
        self.oeste = anObject

    def sur(self, anObject):
        self.sur = anObject

    def norte(self, anObject):
        self.norte = anObject
    
    def num(self):
        return self.num
    
    def num(self, anObject):
        self.num = anObject


