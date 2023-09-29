import json

# Función para agregar una reserva
def agregar_reserva(clientes, reservas, reserva):
    dni_cliente = reserva["dni_cliente"]
    if dni_cliente not in clientes:
        print("El cliente con ese DNI no existe.")
    else:
        reservas.append(reserva)
        print("Reserva agregada con éxito.")

# Función para entregar coches de una reserva
def entregar_coches(reservas, codigo_reserva):
    for reserva in reservas:
        if reserva["codigo"] == codigo_reserva:
            reserva["coches_entregados"] = True
            print("Coches entregados con éxito.")
            return
    print("No se encontró la reserva con ese código.")

# Función para visualizar las reservas de un cliente
def visualizar_reservas(clientes, reservas, dni_cliente):
    if dni_cliente not in clientes:
        print("El cliente con ese DNI no existe.")
        return

    print(f"Reservas del cliente con DNI {dni_cliente}:\n")
    for reserva in reservas:
        if reserva["dni_cliente"] == dni_cliente:
            print(f"Código de Reserva: {reserva['codigo']}")
            print(f"Fecha de Inicio: {reserva['fecha_inicio']}")
            print(f"Fecha de Finalización: {reserva['fecha_final']}")
            print(f"Precio Total de la Reserva: {reserva['precio_total']}")
            print(f"Coches Entregados: {'Sí' if reserva['coches_entregados'] else 'No'}")
            print("Coches Alquilados:")
            for coche in reserva["coches"]:
                print(f"  Matrícula: {coche['matricula']}, Modelo: {coche['modelo']}, Color: {coche['color']}, Marca: {coche['marca']}")
            print()

# Función principal
def main():
    clientes = {}
    reservas = []
    codigo_cliente = 1
    codigo_reserva = 1

    while True:
        print("\n1. Registrar Cliente")
        print("2. Registrar Reserva")
        print("3. Entregar Coches de una Reserva")
        print("4. Visualizar Reservas de un Cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni_cliente = input("Ingrese el DNI del cliente: ")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            direccion_cliente = input("Ingrese la dirección del cliente: ")
            clientes[dni_cliente] = {
                "codigo": codigo_cliente,
                "nombre": nombre_cliente,
                "direccion": direccion_cliente
            }
            codigo_cliente += 1
            print("Cliente registrado con éxito.")
        elif opcion == "2":
            dni_cliente = input("Ingrese el DNI del cliente: ")
            if dni_cliente not in clientes:
                print("El cliente con ese DNI no existe.")
                continue
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
            fecha_final = input("Ingrese la fecha de finalización (YYYY-MM-DD): ")
            precio_total = 0
            coches = []

            while True:
                matricula_coche = input("Ingrese la matrícula del coche: ")
                modelo_coche = input("Ingrese el modelo del coche: ")
                color_coche = input("Ingrese el color del coche: ")
                marca_coche = input("Ingrese la marca del coche: ")
                precio_alquiler = float(input("Ingrese el precio de alquiler del coche: "))
                litros_gasolina = float(input("Ingrese los litros de gasolina en el depósito: "))
                coches.append({
                    "matricula": matricula_coche,
                    "modelo": modelo_coche,
                    "color": color_coche,
                    "marca": marca_coche,
                    "precio_alquiler": precio_alquiler,
                    "litros_gasolina": litros_gasolina
                })
                precio_total += precio_alquiler
                continuar = input("¿Desea agregar otro coche a la reserva? (S/N): ")
                if continuar.upper() != "S":
                    break

            reserva = {
                "codigo": codigo_reserva,
                "dni_cliente": dni_cliente,
                "fecha_inicio": fecha_inicio,
                "fecha_final": fecha_final,
                "precio_total": precio_total,
                "coches": coches,
                "coches_entregados": False
            }
            agregar_reserva(clientes, reservas, reserva)
            codigo_reserva += 1
        elif opcion == "3":
            codigo_reserva_entrega = int(input("Ingrese el código de reserva para entregar los coches: "))
            entregar_coches(reservas, codigo_reserva_entrega)
        elif opcion == "4":
            dni_cliente_visualizar = input("Ingrese el DNI del cliente para visualizar sus reservas: ")
            visualizar_reservas(clientes, reservas, dni_cliente_visualizar)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    # Guardar los datos en un archivo JSON al salir del programa
    datos = {
        "clientes": clientes,
        "reservas": reservas
    }
    with open("reservas.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

if __name__ == "__main__":
    main()