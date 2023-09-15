from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

@dataclass
class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.lista: List[Elemento] = []
        self.nombre: str = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, objeto):
        return objeto in self.lista

    def agregar_elemento(self, objeto):
        if not self.contiene(objeto):
            self.lista.append(objeto)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.lista = self.lista + otro_conjunto.lista
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [e for e in conjunto1.lista if conjunto2.contiene(e)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        nuevo_conjunto = Conjunto(nombre_resultado)
        nuevo_conjunto.lista = elementos_comunes
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(elem.nombre for elem in self.lista)
        return f"Conjunto {self.nombre}: ({elementos_str})"








