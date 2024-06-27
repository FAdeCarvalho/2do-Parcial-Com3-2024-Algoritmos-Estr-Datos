from datetime import datetime, timedelta
import random

class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def calcular_dif_fecha(self, otra_fecha):
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        delta = fecha1 - fecha2
        return abs(delta.days)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"

    def __add__(self, días):
        fecha = datetime(self.año, self.mes, self.dia) + timedelta(days=días)
        return Fecha(fecha.day, fecha.month, fecha.year)

    def __eq__(self, otra_fecha):
        return self.dia == otra_fecha.dia and self.mes == otra_fecha.mes and self.año == otra_fecha.año
    
fecha1 = Fecha(12, 5, 2022)
fecha2 = Fecha(15, 6, 2022)

print(fecha1)  # 12/05/2022
print(fecha2)  # 15/06/2022

print(fecha1.calcular_dif_fecha(fecha2))  # 34 días

fecha3 = fecha1 + 10
print(fecha3)  # 22/05/2022

print(fecha1 == fecha2)  # False
print(fecha1 == fecha1)  # True

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }

    def cambiar_dato(self, clave, nuevo_valor):
        if clave in self.datos:
            self.datos[clave] = nuevo_valor
        else:
            print(f"La clave '{clave}' no existe en el diccionario del alumno.")

    def cambiar_datos(self, nuevos_datos):
        for clave, valor in nuevos_datos.items():
            self.cambiar_dato(clave, valor)

    def antiguedad(self):
        fecha_actual = datetime.now()
        fecha_ingreso_datetime = datetime(
            self.datos["FechaIngreso"].año, 
            self.datos["FechaIngreso"].mes, 
            self.datos["FechaIngreso"].dia
        )
        dias_transcurridos = (fecha_actual - fecha_ingreso_datetime).days
        return dias_transcurridos

    def __str__(self):
        return f"Nombre: {self.datos['Nombre']}\nDNI: {self.datos['DNI']}\nFecha de Ingreso: {self.datos['FechaIngreso']}\nCarrera: {self.datos['Carrera']}"

    def __eq__(self, otro_alumno):
        if isinstance(otro_alumno, Alumno):
            return self.datos == otro_alumno.datos
        return False

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None:
            return  # Lista vacía, no hay nada que ordenar
        actual = self.cabeza
    
    # Bubble Sort para ordenar la lista
        ordenado = False
        while not ordenado:
            ordenado = True
            siguiente = actual.siguiente
            while siguiente is not None:
                fecha_ingreso_actual = datetime(actual.dato.datos["FechaIngreso"].año, actual.dato.datos["FechaIngreso"].mes, actual.dato.datos["FechaIngreso"].dia)
                fecha_ingreso_siguiente = datetime(siguiente.dato.datos["FechaIngreso"].año, siguiente.dato.datos["FechaIngreso"].mes, siguiente.dato.datos["FechaIngreso"].dia)
                if fecha_ingreso_actual > fecha_ingreso_siguiente:

                    self.intercambiar_nodos(actual,siguiente)
                    ordenado = False
                actual = siguiente
                siguiente = siguiente.siguiente

            actual = self.cabeza
                

    def intercambiar_nodos(self, nodo1, nodo2):
        """Intercambia dos nodos en la lista."""
        if nodo1 == self.cabeza:
            self.cabeza = nodo2
        if nodo2 == self.cola:
            self.cola = nodo1

        # Intercambio de referencias para los nodos adyacentes
        if nodo1.anterior is not None:
            nodo1.anterior.siguiente = nodo2
        if nodo2.siguiente is not None:
            nodo2.siguiente.anterior = nodo1

        # Intercambio de referencias de los nodos a intercambiar
        nodo1.siguiente, nodo2.siguiente = nodo2.siguiente, nodo1.siguiente
        nodo1.anterior, nodo2.anterior = nodo2.anterior, nodo1.anterior

    def lista_ejemplo(self):
        carreras = ["Ingeniería", "Medicina", "Derecho", "Psicología"]
        for _ in range(5):
            nombre = f"Alumno {random.randint(1, 100)}"
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), 2022)
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.agregar_al_final(alumno)
        return self
    
    def __iter__(self):
        return IteradorListaDoblementeEnlazada(self.cabeza)

def guardar_alumnos_en_archivo(self, ruta_archivo):
        """Guarda los datos de los alumnos en un archivo."""
        try:
            with open(ruta_archivo, "w") as archivo:
                for alumno in self:
                    archivo.write(f"{alumno}\n")
            print(f"Alumnos guardados en '{ruta_archivo}'")
        except Exception as e:
            print(f"Error al guardar los alumnos: {e}") 

    def mover_directorio(self, ruta_origen, ruta_destino):
        """Mueve un directorio."""
        try:
            os.rename(ruta_origen, ruta_destino)
            print(f"Directorio '{ruta_origen}' movido a '{ruta_destino}'")
        except Exception as e:
            print(f"Error al mover el directorio: {e}")

    def borrar_archivo_y_directorio(self, ruta_destino):
        """Borra un archivo y su directorio."""
        try:
            for filename in os.listdir(ruta_destino):
                filepath = os.path.join(ruta_destino, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)
            os.rmdir(ruta_destino)
            print(f"Directorio '{ruta_destino}' y sus archivos borrados")
        except Exception as e:
            print(f"Error al borrar el directorio: {e}")    

class IteradorListaDoblementeEnlazada:

    def __init__(self, cabeza):
        self.actual = cabeza

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato

# Ejemplo de uso:
lista_alumnos = ListaDoblementeEnlazada()
lista_alumnos.lista_ejemplo()

# Crear directorio si no existe
nombre_directorio = "Directorio"
if not os.path.exists(nombre_directorio):
    os.mkdir(nombre_directorio)

# Guardar alumnos en archivo
ruta_archivo = os.path.join(nombre_directorio, "lista_alumnos.txt")
lista_alumnos.guardar_alumnos_en_archivo(ruta_archivo)

# Mover directorio
ruta_origen = nombre_directorio
ruta_destino = "nuevo directorio"
os.mkdir(ruta_destino)  # Crea el nuevo directorio
lista_alumnos.mover_directorio(ruta_origen, ruta_destino)

# Borrar archivo y directorio
lista_alumnos.borrar_archivo_y_directorio(ruta_destino)



