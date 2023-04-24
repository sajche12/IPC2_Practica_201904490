class Nodo:     #Clase Nodo 
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente
 
class ListaSimple:
  
    def __init__(self):     #Constructor de la lista simple
        self.cabeza = None
        self.tamano = 0
 
    def agregar_nodo(self, dato):   #Metodo para agregar los nodos a la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
        self.tamano += 1
    
    def __iter__(self): #Metodo para convertir la lista a una lista iterable y asi poder imprimirla sin que de error
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
    
    def imprimir_lista(self):   #Metodo para imprimir la lista
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
    
    def ordenar(self, numero):  #Metodo para ordenar la lista de manera descendente
        return sorted(numero, reverse=True)
    
    def limpiar(self):  #Metodo para limpiar la lista y asi poder reutilizarla nuevamente
        nodo_actual = self.cabeza
        while nodo_actual != None:
            siguiente_nodo = nodo_actual.siguiente
            del nodo_actual.dato
            del nodo_actual.siguiente
            nodo_actual = siguiente_nodo
        self.cabeza = None
