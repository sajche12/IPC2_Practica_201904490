from typing import List
from .ListaSimple import ListaSimple

class Item:
    lista_temporal = ListaSimple()  #Lista temporal para ordenar los valores
    orden = ListaSimple()   #Variable para llamar al metodo de ordenamiento
    
    def __init__(self, item, cantidad_items, nivel1, nivel2, nivel3, costo_unidad) -> None: #Constructores del Item
        self.item = str(item)
        self.cantidad_items = int(cantidad_items)
        self.nivel1 = float(nivel1)
        self.nivel2 = float(nivel2)
        self.nivel3 = float(nivel3)
        self.costo_unidad = float(costo_unidad)
            
    def _calcular_margenes(self, items:List[object]):   #Metodo para calcular los productos con mayor margen de ganancia
        for i in items:     #Iterando la lista para acceder a los elementos del nivel1
            precio_nivel1 = i.nivel1
            costo = i.costo_unidad
            margen1 = ((precio_nivel1-costo)/(costo))*100
            margen1 = round(margen1, 2)
            self.lista_temporal.agregar_nodo(margen1) 
        nivel1_ordenada = self.orden.ordenar(self.lista_temporal)
        
        conteo = 1
        print("-----------------")
        print("TOP 10 DEL NIVEL 1")
        for j in nivel1_ordenada:   #Imprimiendo el margen del nivel1 ya ordenado
            print(f"{conteo}. {j}")
            conteo += 1
        print("-----------------")
        
        self.lista_temporal.limpiar()   #Limpiando la lista
        for i in items:     #Iterando la lista para acceder a los elementos del nivel2
            precio_nivel2 = i.nivel2
            costo = i.costo_unidad
            margen2 = ((precio_nivel2-costo)/(costo))*100
            margen2 = round(margen2, 2)
            self.lista_temporal.agregar_nodo(margen2) 
        nivel2_ordenada = self.orden.ordenar(self.lista_temporal)
        
        conteo = 1
        print("-----------------")
        print("TOP 10 DEL NIVEL 2")
        for k in nivel2_ordenada:   #Imprimiendo el margen del nivel2 ya ordenado
            print(f"{conteo}. {k}")
            conteo += 1
        print("-----------------")
        
        self.lista_temporal.limpiar()   #Limpiando la lista
        for i in items:     #Iterando la lista para acceder a los elementos del nivel3
            precio_nivel3 = i.nivel3
            costo = i.costo_unidad
            margen3 = ((precio_nivel3-costo)/(costo))*100
            margen3 = round(margen3, 2)
            self.lista_temporal.agregar_nodo(margen3) 
        nivel3_ordenada = self.orden.ordenar(self.lista_temporal)
        
        conteo = 1
        print("-----------------")
        print("TOP 10 DEL NIVEL 3")
        for l in nivel3_ordenada:   #Imprimiendo el margen del nivel3 ya ordenado
            print(f"{conteo}. {l}")
            conteo += 1
        print("-----------------")
        
    def _calcular_valor_inventario(self, items:List[object]):   #Metodo para saber el top 10 de productos con mayor valor del inventario
        self.lista_temporal.limpiar()   #Limpiando la lista
        for i in items:     #Iterando la lista para acceder a los elementos del inventario
            costo_unidad = i.costo_unidad
            cantidad_items = i.cantidad_items
            valor = costo_unidad*cantidad_items
            valor = round(valor, 2)
            self.lista_temporal.agregar_nodo(valor) 
        valor_ordenada = self.orden.ordenar(self.lista_temporal)
        
        conteo = 1
        print("-----------------")
        print("TOP 10 DE PRODUCTOS CON MAYOR VALOR DEL INVENTARIO ")
        for z in valor_ordenada:    #Imprimiendo los valores del inventario
            print(f"{conteo}. {z}")
            conteo += 1
        print("-----------------")