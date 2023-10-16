from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    
    listaFubtolistas = []
    
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFubtolistas.append(self)
        
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
        
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    def getPiernaHabil(self):
        return self._piernaHabil
    
    @classmethod
    def setListaFutbolistas(cls, listaFubtolistas):
        cls.listaFubtolistas = listaFubtolistas
    
    @classmethod    
    def getListaFutbolistas(cls):
        return cls.listaFubtolistas
    
    def __str__(self):
        return "Mi nombre es " + self.getNombre() +  " soy profesional en el deporte " + self.getDeporte() + " Tengo " + str(self.getEdad()) + " años de edad y llevo " + str(self.getAñosPracticando()) + " años en el deporte"