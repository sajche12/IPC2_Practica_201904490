import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import filedialog
from classes.Item import Item
from .ListaSimple import ListaSimple

class Menu():
    lista_items = ListaSimple()
    item = Item.__new__(Item)   #Variable que no utiliza los constructores de la clase Item
    
    def _extrar_datos(self, archivo):   #Metodo para extraer los datos del archivo xml
        
        root = archivo.getroot()
        
        for item in root.findall('./Item'):     #Accediendo a los elementos del item
            codigo = item.find('ItemCode').text
            cantidad_items = item.find('QuantityOnHand').text
            nivel1 = item.find('PriceLevel1').text
            nivel2 = item.find('PriceLevel2').text
            nivel3 = item.find('PriceLevel3').text
            costo_unidad = item.find('LastTotalUnitCost').text
            nuevo_item = Item(codigo, cantidad_items, nivel1, nivel2, nivel3, costo_unidad)     #Creando objeto Item
            self.lista_items.agregar_nodo(nuevo_item)   #Agregando el objeto a la lista de Items
        
    def pedirNumeroEntero(self):    #Metodo para seleccionar una opcion en el menu
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')
        return num
    
    def menu(self): #Menu con las opciones a elejir
        salir = False
        opcion = 0
        while not salir:
            print("\n-----MENU PRINCIPAL-----")
            print("1. Cargar archivo xml de entrada")
            print("2. Top 10 productos con mayor margen de ganancia")
            print("3. Top 10 productos con mayor valor del inventario")
            print("4. Ayuda")
            print("5. Salir")
            print("------------------------\n")
            
            print ("Elige una opcion")
 
            opcion = self.pedirNumeroEntero()
 
            if opcion == 1:
                #Carga de datos
                print("Seleccione el archivo a cargar...")
                root = tk.Tk()
                root.withdraw()
                filename = "C:\\Users\\ACER\\Desktop\\Practica\\entrada_practica.xml"
                #filename = filedialog.askopenfilename()
                xml = ET.parse(filename)
                self._extrar_datos(xml)
                print("\n¡ARCHIVO CARGADO CORRECTAMENTE!")
            elif opcion == 2:
                #Productos con mayor margen
                self.item._calcular_margenes(self.lista_items)
            elif opcion == 3:
                #Productos con mayor valor
                self.item._calcular_valor_inventario(self.lista_items)
            elif opcion == 4:
                #Ayuda
                print("\nNombre: Diego Aldair Sajche Avila")
                print("Codigo estudiantil: 201904490")
                print("CUI: 3011869790101")
                print("Repositorio: ")
            elif opcion == 5:
                #Salir
                salir = True
            else:
                print ("\nIntroduce un numero entre 1 y 5")
        print ("\nFIN DEL PROGRAMA")
    
    def mostrar(self):  #Metodo para mostrar el programa desde el archivo main.py
        self.menu()