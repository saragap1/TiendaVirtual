# Sara Gabriela Ángel Pinzón @saragap1
# Proyecto: Simulador de tienda en línea


# CLASE DE PRODUCTO

class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        
        
# CLASE DE CATEGORIA Y TIPOS DE CATEGORIA
        
class Categoria:

    def __init__(self):
        pass

    def mostrar_productos_categoria(self):
        pass

class CategoriaMaquillaje(Categoria):

    def __init__(self):
        self.productos = maquillaje

    def mostrar_productos_categoria(self):
        print(f"\nLos productos de la categoria Maquillaje:\n")
        for idx, producto in enumerate(self.productos , start =1):
            print(f"{idx}. {producto.nombre}\n"
                  +f"Precio: ${producto.precio}\n"
                  +f"Descripción: {producto.descripcion}\n")
            
class CategoriaRopa(Categoria):

    def __init__(self):
        self.productos = ropa

    def mostrar_productos_categoria(self):
        print(f"\nLos productos de la categoria Ropa:\n")
        for idx, producto in enumerate(self.productos,start =1):
            print(f"{idx}. {producto.nombre}\n"
                  +f"Precio: ${producto.precio}\n"
                  +f"Descripción: {producto.descripcion}\n")
            
class CategoriaAccesorios(Categoria):

    def __init__(self):
        self.productos = accesorios

    def mostrar_productos_categoria(self):
        print(f"\nLos productos de la categoria Accesorios:\n")
        for idx, producto in enumerate(self.productos,start =1):
            print(f"{idx}. {producto.nombre}\n"
                  +f"Precio: ${producto.precio}\n"
                  +f"Descripción: {producto.descripcion}\n")
            

class CategoriaCosmeticos(Categoria):
    def __init__(self):
        self.productos = cosmeticos

    def mostrar_productos_categoria(self):
        print(f"\nLos productos de la categoria Cosmeticos:\n")
        for idx, producto in enumerate(self.productos,start =1):
            print(f"{idx}. {producto.nombre}\n"
                  +f"Precio: ${producto.precio}\n"
                  +f"Descripción: {producto.descripcion}\n")
            

# CREA LA CATEGORIA METODOS DE PAGO Y LOS DIFERENTES METODOS
            
class MetodoDePago:

    def procesar_total():
        pass

    def procesar_metodo_pago():
        pass

class MetodoTarjetaCredito(MetodoDePago):

    def procesar_total(self, total):
        print(f"\nProcesando pago con tarjeta. Total a pagar: ${total}")

    def procesar_metodo_pago(self):

        nombre_completo = input("Ingresa tu nombre completo: ")
        direccion = input("Escribe tu dirección: ")
        numero_tarjeta =input("Numero de su tarjeta: ")
        fecha_vencimiento =input("Fecha de vencimiento (MM/YY): ")
        cvv = input("CVV: ")
        print(f"\n 🛍️ Pago procesado con éxito, ¡Gracias por tu compra {nombre_completo}! 🛍️")

class MetodoPaypal(MetodoDePago):

    def procesar_total(self, total):
        print(f"\nProcesando pago a través de Paypal. Total a pagar: ${total}")

    def procesar_metodo_pago(self):

        print("Ingresa los siguientes datos")
        nombre_completo = input("Ingresa tu nombre completo: ")
        direccion = input("Escribe tu dirección: ")
        correo = input("Escribe tu dirección de correo electrónico: ")
        contraseña = input("Escribe tu contraseña: ")
        print(f"\n 🛍️ Pago procesado con éxito, ¡Gracias por tu compra {nombre_completo}! 🛍️")

# CLASE DE CARRITO DE COMPRAS

class CarritoDeCompras:

    def __init__(self):
        self.productos_carrito = []

    def total(self):
        total = sum(producto.precio for producto in self.productos_carrito)
        return total

    def visualizar_carrito(self):
               
        if not self.productos_carrito:
            print("\nTu carrito de compras está vacio. ¡Visita nuestros productos!")
        
        else:
            print("\n🛒🛍️  Este es tu carrito de compras:")
            for idx, producto in enumerate(set(self.productos_carrito), start=1):
                cantidad = self.productos_carrito.count(producto)
                print(f" {idx}. {producto.nombre} x {cantidad}  - ${producto.precio*cantidad}")
            print(f"\nTOTAL: ${self.total()}")

    def agregar_producto(self, producto, cantidad=1):
        for _ in range(cantidad):
            self.productos_carrito.append(producto)


# CLASE DE LA TIENDA

class Tienda:

    def vistaTienda():
        
        carrito = CarritoDeCompras()
        metodo_pago = None

        while True: 
            opcion = int(input("\n═══════ ⋆ ★ ⋆ ═══════\n"
            +"\nBienvenido a la Tienda en línea de Belleza\n"
            +"\n¿Qué acción desea realizar? \n"
            +"\n1. Revisar mi carrito de compras\n"
            +"2. Revisar los productos de nuestra tienda\n"
            +"3. Pagar el carrito\n"
            +"4. Salir de la tienda\n"
            +"Ingresa tu opción aquí: "))

            if opcion == 1:
                
                carrito.visualizar_carrito()

            elif opcion == 2: 
                print("\nEstas son nuestras categorias:\n"
                +"\n1. 💄 Maquillaje\n"
                +"2. 👚 Ropa\n"
                +"3. 👝 Accesorios\n"
                +"4. 🧴 Cosmeticos\n")
                
                opcion_categoria = int(input("¿Cuál categoría deseas ver? Ingresa aquí el número tu opción: "))
                
                if opcion_categoria == 1:
                    
                    CategoriaMaquillaje().mostrar_productos_categoria()
                    opcion_maquillaje = input("Selecciona el producto que quieras agregar a tu carrito, o presiona 'Enter' para volver al menú principal: ")
                    
                    if opcion_maquillaje: 
                        try:
                            opcion_maquillaje = int(opcion_maquillaje)
                            if opcion_maquillaje < 1 or opcion_maquillaje > len(CategoriaMaquillaje().productos):
                                raise ValueError
                            producto_eleccion = CategoriaMaquillaje().productos[opcion_maquillaje-1]
                            productos_cantidad = int(input("¿Cuantas unidades deseas agregar?: "))
                            carrito.agregar_producto(producto_eleccion,productos_cantidad)
                            print("\nProducto(s) agregado(s) correctamente a tu carrito de compras. ✅")
                        except ValueError:
                            print("Ingresa un número válido")
                        except IndexError:
                            print("El producto no existe") 
                    
                elif opcion_categoria == 2:
                    CategoriaRopa().mostrar_productos_categoria()
                    opcion_ropa = input("Selecciona el producto que quieras agregar, o presiona 'Enter' para volver: ")
                    
                    if opcion_ropa: 
                        try:
                            opcion_ropa = int(opcion_ropa)
                            if opcion_ropa < 1 or opcion_ropa > len(CategoriaRopa().productos):
                                raise ValueError
                            producto_eleccion = CategoriaRopa().productos[opcion_ropa-1]
                            productos_cantidad = int(input("¿Cuántas unidades deseas agregar?: "))
                            carrito.agregar_producto(producto_eleccion,productos_cantidad)
                            print("\nProducto(s) agregado(s) correctamente a tu carrito de compras. ✅")

                        except ValueError:
                            print("Ingresa un número válido")
                        except IndexError:
                            print("El producto no existe")

                elif opcion_categoria == 3:
                    CategoriaAccesorios().mostrar_productos_categoria()
                    opcion_accesorios = input("Selecciona el producto que quieras agregar, o presiona 'Enter' para volver: ")
                    
                    if opcion_accesorios: 
                        try:
                            opcion_accesorios = int(opcion_accesorios)
                            if opcion_accesorios < 1 or opcion_accesorios > len(CategoriaAccesorios().productos):
                                raise ValueError
                            producto_eleccion = CategoriaAccesorios().productos[opcion_accesorios-1]
                            productos_cantidad = int(input("¿Cuántas unidades deseas agregar?: "))
                            carrito.agregar_producto(producto_eleccion,productos_cantidad)
                            print("\nProducto(s) agregado(s) correctamente a tu carrito de compras. ✅")
                        except ValueError:
                            print("Ingresa un número válido")
                        except IndexError:
                            print("El producto no existe")

                elif opcion_categoria == 4:
                    CategoriaCosmeticos().mostrar_productos_categoria()
                    opcion_cosmeticos = input("Selecciona el producto que quieras agregar, o presiona 'Enter' para volver: ")
                    if opcion_cosmeticos: 
                        try:
                            opcion_cosmeticos = int(opcion_cosmeticos)
                            if opcion_cosmeticos < 1 or opcion_cosmeticos > len(CategoriaCosmeticos().productos):
                                raise ValueError
                            producto_eleccion = CategoriaCosmeticos().productos[opcion_cosmeticos-1]
                            productos_cantidad = int(input("¿Cuantas unidades deseas agregar?: "))
                            carrito.agregar_producto(producto_eleccion,productos_cantidad)
                            print("\nProducto(s)  agregado(s) correctamente a tu carrito de compras. ✅")
                        except ValueError:
                            print("Ingresa un número válido")
                        except IndexError:
                            print("El producto no existe")

            elif opcion ==3:
                if len(carrito.productos_carrito) <= 0:
                        print('\nTu carrito está vacío, añade productos para procesar el pago.\n')

                else:
                    opcion_comprar = int(input("\n¿Deseas confirmar el pedido de tu carrito? 🛒🚚\n"
                    +"1. Sí, quiero comprar los productos de mi carrito.\n"
                    +"2. No, quiero seguir navegando en la Tienda.\n"
                    +"Elige tu opción: "))

                    if opcion_comprar == 1:
                        opcion_metodo_de_pago = int(input("\n¿Cuál será tu método de pago?\n"
                        +"1. Tarjeta de Crédito o Visa\n"
                        +"2. Paypal\n"
                        +"Ingresa tu opción: "))
                        if opcion_metodo_de_pago == 1:
                            metodo_pago = MetodoTarjetaCredito()
                        elif opcion_metodo_de_pago == 2:
                            metodo_pago = MetodoPaypal()
                        else:
                            print("Opción inválida")
                            continue

                    elif opcion_comprar == 2:
                        continue
                    
                    metodo_pago.procesar_total(carrito.total())
                    metodo_pago.procesar_metodo_pago()
                    break

            elif opcion == 4:
                print("\n¡Gracias por visitar nuestra tienda, vuelve pronto :D !")
                break
            else: 
                print("Elección inválida. Por favor vuelve a elegir de nuevo ")

# PRODUCTOS DE LA TIENDA
                
maquillaje = [Producto("Base Luminous Finish", 25, "Una base de maquillaje de larga duración."), Producto("Mascara de pestañas", 15, "Una máscara de pestañas que proporciona volumen y longitud."), Producto("Lápiz Labial de Color Nude", 20, "Un lápiz labial en tono nude con una fórmula cremosa y de larga duración.") ]
ropa = [Producto("Vestido floral", 70, "Vestido de alta costura perfecto para primavera."), Producto("Pantalon cargo", 90, "Pantalón jean negro estilo cargo."),Producto("Camisa blanca", 40, "Camisa básica de algodon con estampado.") ]
accesorios = [Producto("Gafas de sol", 80, "Gafas de sol perfectas para el verano."), Producto("Bolso de cuero negro", 65, "Bolso con estilo elegante y atemporal."), Producto("Aretes de Oro", 120, "Aretes de estilo en forma de diseño clásico y sofisticado. ")]
cosmeticos = [Producto("Loción para cuerpo", 25, "Loción humectante para todo tipo de piel."),Producto("Perfume dulce", 100, "Perfume con notas de rosa y jazmín. "), Producto("Agua Micelar", 60, "Agua micelar con fórmula de aceite, desmaquillante y limpiadora.")]
 
#Ejecutar la función vistaTienda de la clase Tienda.

Tienda.vistaTienda()