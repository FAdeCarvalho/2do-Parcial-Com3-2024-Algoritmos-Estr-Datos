from datetime import datetime, timedelta

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
