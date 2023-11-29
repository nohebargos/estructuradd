#Menu que se presentara por pantalla

def mostrar_menu_principal():
    print("               Menú de Opciones")
    print("1.Arreglo                         2.Registros")
    print("3.Cadenas                         4.Punteros")
    print("5.Lista")
    print("7.Arboles                         8.Tabla Hash")
    print("9.Recursividad                    12.Salir")

    opcion = input("Ingrese una Opción: ")
    return opcion

#Menu de arreglos

def submenu_Arreglos():
    mi_arreglo = []
    while True:
        print("\nMenu de operaciones con Arreglos")
        print("1.Crear un arreglo")
        print("2.Mostrar el Arreglo")
        print("3.Agregar un elemento al Arreglo")
        print("4.Eliminar un elemento del arreglo")
        print("5.Regresar")
        opcion = input("Ingrese una Opcion: ")

        if opcion == '1':
            mi_arreglo = []
            print("Nuevo arreglo Creado")

        elif opcion == '2':
            print("Arreglo actual:", mi_arreglo)

        elif opcion == '3':
            elemento = input("Ingrese el elemento a Agregar: ")
            mi_arreglo.append(elemento)
            print("Elemento Agregado al Arreglo")

        elif opcion == '4':
            if not mi_arreglo:
                print("El arreglo está vacío.")
            else:
                print("Arreglo actual:", mi_arreglo)
                indice = int(input("Ingrese 0 para eliminar un arreglo: "))
                if 0 <= indice < len(mi_arreglo):
                    elemento_eliminado = mi_arreglo.pop(indice)
                    print(f"Elemento {elemento_eliminado} eliminado del arreglo.")
                else:
                    print("Índice inválido.")

        elif opcion == '5':
            break

#Submenu de Registros
def submenu_Registros():
    registros = {}
    while True:
        print("\nMenú:")
        print("1. Mostrar todos los registros")
        print("2. Agregar un nuevo registro")
        print("3. Buscar un registro por clave")
        print("4. Eliminar un registro por clave")
        print("5. Regresar")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
        # Mostrar todos los registros
            print("Registros actuales:")
            for clave, valor in registros.items():
                print(f"{clave}: {valor}")

        elif opcion == "2":
        # Agregar un nuevo registro
            clave = input("Ingrese la clave del registro: ")
            valor = input("Ingrese el valor del registro: ")
            registros[clave] = valor
            print("Registro agregado.")

        elif opcion == "3":
        # Buscar un registro por clave
            clave_buscar = input("Ingrese la clave a buscar: ")
            valor_encontrado = registros.get(clave_buscar, "Clave no encontrada")
            print(f"Valor encontrado: {valor_encontrado}")

        elif opcion == "4":
        # Eliminar un registro por clave
                clave_eliminar = input("Ingrese la clave a eliminar: ")
                if clave_eliminar in registros:
                    del registros[clave_eliminar]
                    print("Registro eliminado.")
                else:
                    print("Clave no encontrada.")

        elif opcion == "5":
        # Salir del programa
            break


#Submenu de cadenas
def submenu_Cadenas():
    while True:
        print("Menu de Cadenas")
        print("1.Ingresar cadenas 1 y 2")
        print("2.Mostrar cadenas")
        print("3.Concatenar cadenas")
        print("4.Regresar")
        opcion = input("Ingrese una Opcion: ")
        if opcion == '1':
            cadena1 = input("Ingrese cadena 1: ")
            cadena2 = input("Ingrese cadena 2:" )
        elif opcion == '2':
            print("Las cadenas son:")
            print("Cadena1:", cadena1)
            print("Cadena2:", cadena2)
        elif opcion == '3':
            print("Concatenar cadenas")
            resultado = cadena1 + cadena2
            print("Resultado de la concatenacion:", resultado)
        elif opcion == '4':
            break

#Submenu listas
def submenu_Listas():
    mi_lista = []

    while True:
        print("\nMenú:")
        print("1. Crear una lista vacía")
        print("2. Agregar elemento a la lista")
        print("3. Mostrar la lista")
        print("4. Eliminar elemento de la lista por valor")
        print("5. Regresar")
        opcion = input("Ingrese el número de la opción deseada: ")
# Inicializar una lista vacía

        if opcion == "1":
        # Crear una lista vacía
            mi_lista = []
            print("Lista vacía creada.")

        elif opcion == "2":
        # Agregar elemento a la lista
            elemento = input("Ingrese el elemento a agregar: ")
            mi_lista.append(elemento)
            print(f"Elemento '{elemento}' agregado a la lista.")

        elif opcion == "3":
        # Mostrar la lista
            print("Lista actual:", mi_lista)

        elif opcion == "4":
        # Eliminar elemento de la lista por valor
            valor = input("Ingrese el elemento a eliminar: ")
            if valor in mi_lista:
                mi_lista.remove(valor)
                print(f"Elemento '{valor}' eliminado de la lista.")
            else:
                print(f"Elemento '{valor}' no encontrado en la lista.")

        elif opcion == "5":
            break
        # Salir del programa


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
            else:
                nodo_actual.izquierda = Nodo(valor)
        else:
            if nodo_actual.derecha:
                self._insertar_recursivo(valor, nodo_actual.derecha)
            else:
                nodo_actual.derecha = Nodo(valor)

    def imprimir_inorden(self, nodo_actual):
        if nodo_actual:
            self.imprimir_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self.imprimir_inorden(nodo_actual.derecha)

# Función para mostrar el menú
def Submenu_Arbol():
    arbol = ArbolBinario()
    while True:
        print("\nMenú:")
        print("1. Insertar elemento en el árbol")
        print("2. Mostrar recorrido inorden")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")
# Ejemplo de uso

        if opcion == "1":
            valor = int(input("Ingrese el valor a insertar: "))
            arbol.insertar(valor)
            print(f"Valor {valor} insertado en el árbol.")

        elif opcion == "2":
            print("Recorrido inorden del árbol:")
            arbol.imprimir_inorden(arbol.raiz)

        elif opcion == "3":
            break

#SUBMENU TABLA HASH
class TablaHash:
    def __init__(self, tamano):
        self.tamano = tamano
        self.tabla = {}

    def hash_funcion(self, clave):
        return hash(clave) % self.tamano

    def insertar(self, clave, valor):
        indice = self.hash_funcion(clave)
        if indice not in self.tabla:
            self.tabla[indice] = {}
        self.tabla[indice][clave] = valor

    def buscar(self, clave):
        indice = self.hash_funcion(clave)
        if indice in self.tabla and clave in self.tabla[indice]:
            return self.tabla[indice][clave]
        return None

    def imprimir_tabla(self):
        for indice, elementos in self.tabla.items():
            print(f"Índice {indice}:", elementos)

# Función para mostrar el menú
def menu_tabla_hash():
    tamano_tabla = int(input("Ingrese el tamaño de la tabla hash: "))
    tabla = TablaHash(tamano=tamano_tabla)

    while True:
        print("\nMenú de Tabla Hash:")
        print("1. Insertar elemento")
        print("2. Buscar elemento")
        print("3. Mostrar tabla")
        print("4. Regresar")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            clave = input("Ingrese la clave: ")
            valor = input("Ingrese el valor: ")
            tabla.insertar(clave, valor)
            print(f"Elemento ({clave}, {valor}) insertado en la tabla.")

        elif opcion == "2":
            clave_buscar = input("Ingrese la clave a buscar: ")
            valor_encontrado = tabla.buscar(clave_buscar)
            if valor_encontrado is not None:
                print(f"Valor encontrado para la clave '{clave_buscar}': {valor_encontrado}")
            else:
                print(f"Clave '{clave_buscar}' no encontrada en la tabla.")

        elif opcion == "3":
            tabla.imprimir_tabla()

        elif opcion == "4":
            break

#Submenu Recursividad
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def Submenu_RECURSIVIDAD():
    while True:
        print("Menú:")
        print("1. Calcular Factorial")
        print("2. Calcular Serie Fibonacci")
        print("3. Salir")

def SUB_SUBMENU():

        Submenu_RECURSIVIDAD()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            num_factorial = int(input("Ingrese el número para calcular el factorial: "))
            resultado_factorial = factorial(num_factorial)
            print(f"El factorial de {num_factorial} es {resultado_factorial}")

        elif opcion == "2":
            num_fibonacci = int(input("Ingrese la posición para calcular la serie Fibonacci: "))
            resultado_fibonacci = fibonacci(num_fibonacci)
            print(f"El número en la posición {num_fibonacci} de la serie Fibonacci es {resultado_fibonacci}")

        elif opcion == "3":
            break

#SUBMENU PUNTEROS
class Puntero:
    def __init__(self, valor):
        self.valor = valor

def mostrar_menu_punteros():
    variable = Puntero(None)

    while True:
        print("\nMenú de Punteros:")
        print("1. Crear variable")
        print("2. Mostrar valor")
        print("3. Modificar valor")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            valor = input("Ingrese el valor de la variable: ")
            variable = Puntero(valor)
            print("Variable creada.")

        elif opcion == "2":
            if variable.valor is not None:
                print(f"Valor actual de la variable: {variable.valor}")
            else:
                print("La variable no ha sido creada.")

        elif opcion == "3":
            if variable.valor is not None:
                nuevo_valor = input("Ingrese el nuevo valor: ")
                variable.valor = nuevo_valor
                print("Valor modificado.")
            else:
                print("La variable no ha sido creada.")

        elif opcion == "4":
            break

#Control del menu principal
def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1':
            submenu_Arreglos()
        elif opcion == '2':
            submenu_Registros()
        elif opcion == '3':
            submenu_Cadenas()
        elif opcion == '5':
            submenu_Listas()
        elif opcion == '7':
            Submenu_Arbol()
        elif opcion == '8':
            menu_tabla_hash()
        elif opcion == '9':
            Submenu_RECURSIVIDAD()
        elif opcion == '4':
            mostrar_menu_punteros()
        elif opcion =='12':
            print("Cerrando sistema")
            break

if __name__ == "__main__":
    main()