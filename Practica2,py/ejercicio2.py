ventas = [
    {
        "fecha": "12-01-2023",
        "producto": "Producto_A",
        "cantidad": 50,
        "precio": 45.00,
        "promocion": True
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_AX",
        "cantidad": 160,
        "precio": 12.00,
        "promocion": False
    },
    {
        "fecha": "10-01-2023",
        "producto": "Producto_D",
        "cantidad": 20,
        "precio": 15.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_C",
        "cantidad": 10,
        "precio": 140.00,
        "promocion": False
    },
    {
        "fecha": "11-01-2023",
        "producto": "Producto_D",
        "cantidad": 1200,
        "precio": 1.00,
        "promocion": True
    }
]    

while True:
    print("\nBIENVENIDO AL MENU INTERACTIVO")
    print("""
    1. Mostrar el listado de ventas
    2. Añadir producto
    3. Calcular la suma total de las ventas
    4. Calcular el promedio de ventas
    5. Mostrar el producto con más unidades vendidas
    6. Mostrar el listado de productos
    7. Salir
    """)

    try:
        opcion = int(input("Ingrese la opción a elegir: "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue  

    match opcion:
        case 1:
            print("\nListado de Ventas:")
            for venta in ventas:
                print(f"Fecha: {venta['fecha']} | Producto: {venta['producto']} | Cantidad: {venta['cantidad']} | Precio: {venta['precio']} | Promoción: {'Sí' if venta['promocion'] else 'No'}")

        case 2:
            print("\nAñadiendo producto")

            fecha = input("Ingrese la fecha de la venta (dd-mm-yyyy): ")
            producto = input("Ingrese el nombre del producto: ").strip().capitalize()
            try:
                cantidad = int(input("Ingrese la cantidad vendida: "))
                precio = float(input("Ingrese el precio unitario: "))
                promocion = input("¿Hay promoción? (sí/no): ").strip().lower() == "sí"
            except ValueError:
                print("Error: Ingrese valores numéricos en cantidad y precio.")
                continue  

            ventas.append({"fecha": fecha, "producto": producto, "cantidad": cantidad, "precio": precio, "promocion": promocion})
            print("Producto añadido exitosamente.")

        case 3:
            total_ventas = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
            print(f"\nLa suma total de las ventas es: {total_ventas:.2f}")

        case 4:
            if len(ventas) == 0:
                print("No hay ventas registradas para calcular el promedio.")
            else:
                total_ventas = sum(venta['cantidad'] * venta['precio'] for venta in ventas)
                promedio = total_ventas / len(ventas)
                print(f"\nEl promedio de ventas por transacción es: {promedio:.2f}")

        case 5:
            if ventas:
                producto_max = max(ventas, key=lambda venta: venta["cantidad"])
                print(f"\nEl producto con más unidades vendidas es: {producto_max['producto']} con {producto_max['cantidad']} unidades.")
            else:
                print("No hay ventas registradas.")

        case 6:
            productos = set(venta['producto'] for venta in ventas)
            print("\nListado de productos:")
            for producto in productos:
                print(producto)

        case 7:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida, por favor intente nuevamente.")