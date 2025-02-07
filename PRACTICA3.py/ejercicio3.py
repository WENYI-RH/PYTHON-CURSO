# Lista de horas asignadas al conductor
class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  

    def agregar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False

    def __str__(self):
        return f"Conductor: {self.nombre}, Horarios: {self.horarios}"


class Buses:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horarios = []  # Lista de horarios del bus
        self.conductor_asignado = None  # Conductor asignado al bus

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def agregar_horario(self, horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
            return True
        return False

    def asignar_conductor(self, conductor):
        if self.conductor_asignado is None:
            self.conductor_asignado = conductor
            return True
        return False

    def __str__(self):
        return (f"Bus: {self.placa}, Ruta: {self.ruta}, "
                f"Horarios: {self.horarios}, Conductor: {self.conductor_asignado.nombre if self.conductor_asignado else 'Ninguno'}")


class Admin:
    def __init__(self):
        self.buses = []  # Lista de buses registrados
        self.conductores = []  # Lista de conductores registrados

    def agregar_bus(self, placa):
        bus = Buses(placa)
        self.buses.append(bus)
        print(f"Bus con placa {placa} agregado exitosamente.")

    def agregar_ruta_a_bus(self, placa, ruta):
        bus = self._buscar_bus(placa)
        if bus:
            bus.asignar_ruta(ruta)
            print(f"Ruta '{ruta}' asignada al bus con placa {placa}.")
        else:
            print(f"No se encontró un bus con placa {placa}.")

    def registrar_horario_a_bus(self, placa, horario):
        bus = self._buscar_bus(placa)
        if bus:
            if bus.agregar_horario(horario):
                print(f"Horario {horario} agregado al bus con placa {placa}.")
            else:
                print(f"El horario {horario} ya está registrado para este bus.")
        else:
            print(f"No se encontró un bus con placa {placa}.")

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado exitosamente.")

    def agregar_horario_a_conductor(self, nombre, hora):
        conductor = self._buscar_conductor(nombre)
        if conductor:
            if conductor.agregar_horario(hora):
                print(f"Horario {hora} agregado al conductor {nombre}.")
            else:
                print(f"El conductor {nombre} ya tiene asignado el horario {hora}.")
        else:
            print(f"No se encontró un conductor con nombre {nombre}.")

    def asignar_bus_a_conductor(self, placa, nombre_conductor):
        bus = self._buscar_bus(placa)
        conductor = self._buscar_conductor(nombre_conductor)

        if bus and conductor:

            
            # Verificar si el conductor ya tiene un bus asignado en ese horario
            for horario in bus.horarios:
                if horario in conductor.horarios:
                    print(f"El conductor {nombre_conductor} ya tiene un horario asignado en {horario}.")
                    return

            if bus.asignar_conductor(conductor):
                print(f"Conductor {nombre_conductor} asignado al bus con placa {placa}.")
            else:
                print(f"El bus con placa {placa} ya tiene un conductor asignado.")
        else:
            print("Bus o conductor no encontrado.")

    def _buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        return None

    def _buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        return None

    def mostrar_buses(self):
        if not self.buses:
            print("No hay buses registrados.")
        else:
            print("Buses registrados:")
            for bus in self.buses:
                print(bus)

    def mostrar_conductores(self):
        if not self.conductores:
            print("No hay conductores registrados.")
        else:
            print("Conductores registrados:")
            for conductor in self.conductores:
                print(conductor)


def menu():
    admin = Admin()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE BUSES ---")
        print("1. Agregar bus")
        print("2. Agregar ruta a bus")
        print("3. Registrar horario a bus")
        print("4. Agregar conductor")
        print("5. Agregar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Mostrar buses")
        print("8. Mostrar conductores")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                placa = input("Ingrese la placa del bus: ")
                admin.agregar_bus(placa)
            case "2":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta: ")
                admin.agregar_ruta_a_bus(placa, ruta)
            case "3":
                placa = input("Ingrese la placa del bus: ")
                horario = input("Ingrese el horario (formato HH:MM): ")
                admin.registrar_horario_a_bus(placa, horario)
            case "4":
                nombre = input("Ingrese el nombre del conductor: ")
                admin.agregar_conductor(nombre)
            case "5":
                nombre = input("Ingrese el nombre del conductor: ")
                hora = input("Ingrese el horario (formato HH:MM): ")
                admin.agregar_horario_a_conductor(nombre, hora)
            case "6":
                placa = input("Ingrese la placa del bus: ")
                nombre_conductor = input("Ingrese el nombre del conductor: ")
                admin.asignar_bus_a_conductor(placa, nombre_conductor)
            case "7":
                admin.mostrar_buses()
            case "8":
                admin.mostrar_conductores()
            case "9":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()