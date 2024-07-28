def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("5. Salir")

while True:
    menu()
    eleccion = input("Ingrese el número de la operación que desea realizar: ")

    if eleccion == '5':
        print("Saliendo...")
        break
    elif eleccion in ('1', '2'):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if eleccion == '1':
            print(f"Resultado: {sumar(num1, num2)}")
        elif eleccion == '2':
            print(f"Resultado: {restar(num1, num2)}")
    else:
        print("Opción no válida. Por favor, seleccione una opción entre 1 y 5.")
