class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ID de producto ya existe")
                return
        self.productos.append(producto)

    def eliminar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:
                self.productos.remove(producto)
                print("Producto eliminado")
                return
        print("Error: Producto no encontrado")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado")
                return
        print("Error: Producto no encontrado")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío")
        else:
            print("Productos en inventario:")
            for producto in self.productos:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos en el inventario")
    print("6. Salir")


if "name" == "_main_":
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto_nuevo = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto_nuevo)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            opcion_actualizacion = input("¿Desea actualizar cantidad (C) o precio (P)? ")
            if opcion_actualizacion.upper() == "C":
                cantidad = int(input("Ingrese la nueva cantidad: "))
                inventario.actualizar_producto(id, cantidad=cantidad)
            elif opcion_actualizacion.upper() == "P":
                precio = float(input("Ingrese el nuevo precio: "))
                inventario.actualizar_producto(id, precio=precio)
            else:
                print("Opción inválida")

        elif opcion == "4":
            nombre = input("Ingrese el nombre o parte del nombre del producto: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("Resultados de la búsqueda:")
                for producto in resultados:
                    print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")
            else:
                print("No se encontraron productos con ese nombre")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")