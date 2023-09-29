import json

# Función para agregar un empleado a una empresa
def agregar_empleado(empresa, empleado):
    empresa["empleados"].append(empleado)

# Función para agregar un cliente a una empresa
def agregar_cliente(empresa, cliente):
    empresa["clientes"].append(cliente)

# Función para asignar empleados subordinados a un empleado directivo
def asignar_subordinados(empleado_directivo, subordinados):
    empleado_directivo["subordinados"] = subordinados

# Función para visualizar la información de empleados de una empresa
def visualizar_empleados(empresa):
    for empleado in empresa["empleados"]:
        print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Sueldo Bruto: {empleado['sueldo_bruto']}")

# Función para visualizar la información de clientes de una empresa
def visualizar_clientes(empresa):
    for cliente in empresa["clientes"]:
        print(f"Nombre: {cliente['nombre']}, Edad: {cliente['edad']}, Teléfono de Contacto: {cliente['telefono']}")

# Función principal
def main():
    empresas = []

    try:
        # Cargar datos desde el archivo JSON si existe
        with open("empresas.json", "r") as archivo:
            empresas = json.load(archivo)
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Agregar Empresa")
        print("2. Agregar Empleado a una Empresa")
        print("3. Agregar Cliente a una Empresa")
        print("4. Asignar Subordinados a Empleado Directivo")
        print("5. Visualizar Empleados de una Empresa")
        print("6. Visualizar Clientes de una Empresa")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            empresa = {
                "nombre": nombre_empresa,
                "empleados": [],
                "clientes": []
            }
            empresas.append(empresa)
        elif opcion == "2":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            for empresa in empresas:
                if empresa["nombre"] == nombre_empresa:
                    nombre_empleado = input("Nombre del empleado: ")
                    edad_empleado = input("Edad del empleado: ")
                    sueldo_bruto_empleado = input("Sueldo Bruto del empleado: ")
                    empleado = {
                        "nombre": nombre_empleado,
                        "edad": edad_empleado,
                        "sueldo_bruto": sueldo_bruto_empleado
                    }
                    agregar_empleado(empresa, empleado)
                    print("Empleado agregado con éxito.")
                    break
            else:
                print("Empresa no encontrada.")
        elif opcion == "3":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            for empresa in empresas:
                if empresa["nombre"] == nombre_empresa:
                    nombre_cliente = input("Nombre del cliente: ")
                    edad_cliente = input("Edad del cliente: ")
                    telefono_cliente = input("Teléfono de contacto del cliente: ")
                    cliente = {
                        "nombre": nombre_cliente,
                        "edad": edad_cliente,
                        "telefono": telefono_cliente
                    }
                    agregar_cliente(empresa, cliente)
                    print("Cliente agregado con éxito.")
                    break
            else:
                print("Empresa no encontrada.")
        elif opcion == "4":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            for empresa in empresas:
                if empresa["nombre"] == nombre_empresa:
                    nombre_empleado_directivo = input("Nombre del empleado directivo: ")
                    for empleado in empresa["empleados"]:
                        if empleado["nombre"] == nombre_empleado_directivo:
                            subordinados = input("Nombres de los subordinados (separados por comas): ").split(",")
                            asignar_subordinados(empleado, subordinados)
                            print("Subordinados asignados con éxito.")
                            break
                    else:
                        print("Empleado directivo no encontrado.")
                    break
            else:
                print("Empresa no encontrada.")
        elif opcion == "5":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            for empresa in empresas:
                if empresa["nombre"] == nombre_empresa:
                    print(f"Empleados de {empresa['nombre']}:\n")
                    visualizar_empleados(empresa)
                    break
            else:
                print("Empresa no encontrada.")
        elif opcion == "6":
            nombre_empresa = input("Ingrese el nombre de la empresa: ")
            for empresa in empresas:
                if empresa["nombre"] == nombre_empresa:
                    print(f"Clientes de {empresa['nombre']}:\n")
                    visualizar_clientes(empresa)
                    break
            else:
                print("Empresa no encontrada.")
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Guardar los datos en un archivo JSON al salir del programa
    with open("empresas.json", "w") as archivo:
        json.dump(empresas, archivo, indent=4)

if __name__ == "__main__":
    main()