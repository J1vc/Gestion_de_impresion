from collections import deque

class Impresion:
    def __init__(self, nombre, usuario, prioridad):
        self.nombre = nombre
        self.usuario = usuario
        self.prioridad = prioridad

    def __str__(self):
        prioridad_str = "Alta" if self.prioridad == "alta" else"Baja"
        return f"Nombre: {self.nombre}, Usuario: {self.usuario}, Prioridad: {prioridad_str}"
    

cola_prioridad_alta = deque()
cola_prioridad_baja = deque()

def agregar_impresion(nombre, usuario, prioridad):
    impresion = Impresion(nombre, usuario, prioridad)
    if prioridad == "alta":
        cola_prioridad_alta.append(impresion)
    else:
        cola_prioridad_baja.append(impresion)
    print("Documento agregado a la cola de impresion")

def cola_impresion():
    if cola_prioridad_alta:
        impresion = cola_prioridad_alta.popleft()
    
    elif cola_prioridad_baja:
        impresion = cola_prioridad_baja.popleft()

    else:
        print("No hay documentos en la cola")
        return
    print("Procesando documento:",impresion)

def estado_de_cola():
    print("\nEstado de la cola de impresion")
    print("Prioridad alta: ")
    for i in cola_prioridad_alta:
        print(" ", i)
    print("Prioridad baja:")
    for i in cola_prioridad_baja:
        print(" ", i)


agregar_impresion("Documento 1", "Jhon", prioridad="baja")
agregar_impresion("Documento 2", "Juan", prioridad="alta")
agregar_impresion("Documento 3", "Jeronimo", prioridad="baja")
agregar_impresion("Documento 4", "Jonas", prioridad="alta")

cola_impresion()

estado_de_cola()
