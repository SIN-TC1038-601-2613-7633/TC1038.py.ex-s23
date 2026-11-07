# programa que pregunte cuántos elementos se agregarán a una lista. 
# Se debe validar que el número sea mayor que cero, si no lo es, 
# se debe volver a pedir hasta que el usuario teclee un número positivo.
# Después debe leer esa cantidad de datos e ingresarlos a la lista.
# El programa debe desplegar los elementos ingresados en forma inversa, con indexamiento
# negativo y formato:
# lista[-x] = valor 

def main():
    lista = []
    cantidad = int(input())
                
    while cantidad <= 0:
        cantidad = int(input())

    for i in range(cantidad):
        elemento = int(input())
        lista.append(elemento)

    for i in range(-1, -cantidad - 1, -1):
        print(f'lista[{i}] = {lista[i]}')

if __name__=='__main__':
    main()
