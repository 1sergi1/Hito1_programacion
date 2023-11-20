# Lista de productos con los precios y stock de cada producto.
productos_tienda = [
    {"nombre": "Gel", "stock": 10, "precio": 2.99},
    {"nombre": "Champú", "stock": 6, "precio": 2.50},
    {"nombre": "Peine", "stock": 5, "precio": 0.75},
    {"nombre": "Desodorante", "stock": 4, "precio": 1.99},
    {"nombre": "Calcetines", "stock": 9, "precio": 1.99},
    {"nombre": "Calzoncillos", "stock": 7, "precio": 5.49},
    {"nombre": "Camiseta", "stock": 0, "precio": 15.75},
    {"nombre": "Pantalón", "stock": 5, "precio": 19.99},
    {"nombre": "Pijama", "stock": 7, "precio": 22.95},
    {"nombre": "Gorra", "stock": 5, "precio": 10.50},
]

# Menú de opciones para que elija el usuario.
def menu():
    print("Menú de opciones:")
    print("1. Registrar cliente")
    print("2. Visualizar clientes")
    print("3. Buscar cliente")
    print("4. Realizar una compra")
    print("5. Seguimiento de la compra")
    print("6. Salir")

# Definimos la función Registro_cliente se pedirán sus datos personales.
def registro_cliente():
    nombre = input("Introduce un nombre: ")
    telefono = input("Introduce un número de teléfono: ")
    email = input("Introduce un email: ")
    direccion = input("Introduce una dirección: ")
    nacionalidad = input("Introduce una nacionalidad: ")

# Añadimos a la lista clientes txt los clientes registrados.
    with open("lista_clientes.txt", "a") as archivo:
        archivo.write(f"{nombre},{telefono},{email},{direccion},{nacionalidad}\n")
    print(f"Cliente {nombre} registrado correctamente")

# Función para visualizar_clientes registrados.
def visualizar_clientes():
    with open("lista_clientes.txt", "r") as archivo:
        for line in archivo:
            nombre, telefono, email, direccion, nacionalidad = line.strip().split(",")
            print(f"Nombre: {nombre}, Teléfono: {telefono}, Email: {email}, Dirección: {direccion}, Nacionalidad: {nacionalidad}")

# Función para realizar búsquedas de clientes.
def buscar_clientes():
    nombre_cliente = input("Dime el nombre del cliente que estás buscando: ")
    with open("lista_clientes.txt", "r") as archivo:
        for line in archivo:
            nombre, telefono, email, direccion, nacionalidad = line.strip().split(",")
            if nombre_cliente in nombre:
                print(f"Nombre: {nombre}, Teléfono: {telefono}, Email:{email} Dirección: {direccion}, Nacionalidad: {nacionalidad}")

# Función para realizar una compra
def realizar_compra():
    nombre_cliente = input("Introduce el nombre del cliente que realiza la compra: ")
    nacionalidad_cliente = input("Introduce la nacionalidad del cliente: ")

    # Esto sirve para mostrar la lista de productos en stock al usuario.
    print("Lista de productos disponibles:")
    for i, producto in enumerate(productos_tienda, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']}")

    # Solicitar al usuario que elija productos hasta que nos diga 'fin'.
    productos_elegidos = []
    while True:
        eleccion = input("Elige un producto por su número (o 'fin' para finalizar): ")
        if eleccion.lower() == 'fin':
            break
        elif eleccion.isdigit() and 1 <= int(eleccion) <= len(productos_tienda):
            producto_elegido = productos_tienda[int(eleccion) - 1]
            # Verificar si hay suficiente stock
            if producto_elegido['stock'] > 0:
                productos_elegidos.append(producto_elegido)
                producto_elegido['stock'] -= 1
                print(f"Producto agregado: {producto_elegido['nombre']} - ${producto_elegido['precio']}")
            else:
                print("¡Producto sin stock! Elige otro.")
        else:
            print("Número no válido. Inténtalo de nuevo.")

    # Calcular el total de la compra.
    total_compra = sum(producto['precio'] for producto in productos_elegidos)

    # Aplicar 21% de impuestos si la nacionalidad del cliente es española.
    if nacionalidad_cliente.lower() == 'española':
        impuestos = total_compra * 0.21
        total_compra += impuestos
        print(f"Se ha aplicado un 21% de impuestos. Total de la compra con impuestos: ${total_compra}")

    # Solicitar al usuario que ingrese su código de seguimiento.
    codigo_seguimiento = input("Introduce el código de seguimiento de la compra: ")

    # Mostrar detalles de la compra por pantalla.
    print("\nDetalles de la compra:")
    print(f"Cliente: {nombre_cliente}")
    print("Productos:")
    for producto in productos_elegidos:
        print(f"  - {producto['nombre']}: ${producto['precio']}")
    print(f"Total de la compra: ${total_compra}")
    print(f"Código de seguimiento: {codigo_seguimiento}\n")

    # Almacenar la información de la compra en el archivo "compras.txt".
    with open("compras.txt", "a") as archivo_compras:
        archivo_compras.write(f"Cliente: {nombre_cliente}, Productos: {productos_elegidos}, Total: {total_compra}, Código de seguimiento: {codigo_seguimiento}\n")
    print("Compra realizada con éxito.")

# Seguimiento de una compra: se enviará por SMS al teléfono móvil y al correo del cliente los datos del pedido y el código de seguimiento de su pedido.
def seguimiento_compra():
    while True:
        codigo_seguimiento = input("Introduce el código de seguimiento de la compra: ")

        # Verificar la existencia del código en el archivo "compras.txt"
        with open("compras.txt", "r") as archivo_compras:
            for line in archivo_compras:
                if f"Código de seguimiento: {codigo_seguimiento}" in line:
                    # Simulación de envío de SMS y correo (puedes adaptar esto según las bibliotecas que estés utilizando para enviar mensajes y correos electrónicos)
                    print(f"Enviando detalles de la compra por email y SMS al cliente con código de seguimiento {codigo_seguimiento}")
                    return  # Salir del bucle si el código existe

        # Si el código no existe, mostrar un mensaje y permitir al usuario volver a intentar
        print(f"El código de seguimiento {codigo_seguimiento} no existe. Inténtalo de nuevo.")

# Código principal
while True:
    menu()
    opcion = input("Selecciona una de las siguientes opciones: ")

    if opcion == "1":
        registro_cliente()
    elif opcion == "2":
        visualizar_clientes()
    elif opcion == "3":
        buscar_clientes()
    elif opcion == "4":
        realizar_compra()
    elif opcion == "5":
        seguimiento_compra()
    elif opcion == "6":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
