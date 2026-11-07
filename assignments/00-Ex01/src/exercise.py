# Programa que pregunta cuántos elementos se agregarán a una lista. 
# Se debe validar que el número sea mayor que cero, si no lo es, se debe volver a pedir hasta que el usuario teclee un número positivo.
# Después debe leer esa cantidad de datos e ingresarlos a la lista.
# Finalmente mostrar la lista elemento x elemento con el formato:
# lista[x] = valor

def main():
    lista = []
    cantidad = int(input())
                
    while cantidad <= 0:
        cantidad = int(input())

    for i in range(cantidad):
        elemento = int(input())
        lista.append(elemento)

    for i in range(cantidad):
        print(f'lista[{i}] = {lista[i]}')

if __name__=='__main__':
    main()
