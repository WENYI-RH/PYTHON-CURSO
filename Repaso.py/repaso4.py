#  DIccionario con las ventas
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]


# CREA UN MENU ITERACTIVO QUE CUENTE CON LOS SIGUIENTES OPCIONES
def menu():
    while True:
        print("\nBienvenido al menu iteractivo")
        print("1. Mostrar el listado de ventas")
        print("2. Añadir un producto")
        print("3. Calcular la suma total de las ventas")
        print("4. Calcular el promedio de ventas")
        print("5. Mostrar el producto con más unidades vendidas")
        print("6. Mostrar el listado de productos")
        print("7. Salir del menu")
        
        opcion = input("Seleccione una opción): ")
        
        if opcion == '1':
            mostrar_listado_ventas()
        elif opcion == '2':
            añadir_producto()
        elif opcion == '3':
            calcular_suma_ventas()
        elif opcion == '4':
            calcular_promedio_ventas()
        elif opcion == '5':
            mostrar_producto_mas_unidades()
        elif opcion == '6':
            mostrar_listado_productos()
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor ingrese otra opción.")

# Mostrar el listado de ventas
def mostrar_listado_ventas():
    print("\nListado de Ventas:")
    for venta in ventas:
        print(f"Fecha: {venta['fecha']}, Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Promoción: {venta['promocion']}")

# Añadir un producto
def añadir_producto():
    fecha = input("Indique la fecha de la venta (dd-mm-yyyy): ")
    producto = input("Indique el nombre del producto: ")
    cantidad = int(input("Indique la cantidad vendida: "))
    precio = float(input("Indique el precio unitario del producto: "))
    promocion = input("¿Hay promoción? (sí/no): ").strip().lower() == 'sí'
    
    nueva_venta = {
        "fecha": fecha,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
        "promocion": promocion
    }
    ventas.append(nueva_venta)
    print("El producto se ha añadido")

# Calcular la suma total de las ventas
def calcular_suma_ventas():
    total = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
    print(f"La suma de las ventas es: {total:.2f}")

# Calcular el promedio de ventas
def calcular_promedio_ventas():
    total_cantidad = 0
    total_ventas = 0

    for venta in ventas:
        total_cantidad += venta['cantidad']
        total_ventas += venta['cantidad'] * venta['precio']
   
    if total_cantidad > 0:
        promedio = total_ventas / total_cantidad
    else:
        promedio = 0
    print(f"\nEl promedio de ventas es {promedio:.2f}")

# Mostrar el producto con más unidades vendidas
def mostrar_producto_mas_unidades():
    if ventas:
        producto_max = max(ventas, key=lambda venta: venta["cantidad"])
        print(f"El producto con más unidades vendidas es: {producto_max['producto']} con {producto_max['cantidad']} unidades.")
    else:
        print("No hay ventas registradas.")

# Mostrar el listado de productos
def mostrar_listado_productos():
    productos = {venta['producto'] for venta in ventas}
    print("Listado de productos:")
    for producto in productos:
        print(producto)


menu()
