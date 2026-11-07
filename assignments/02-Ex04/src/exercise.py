# Programa que lea números enteros y los vaya agregando a una lista, 
# dejará de leer cuando se introduzca un valor negativo. 
# Luego el programa debe contar la cantidad de valores pares e impares de la lista. 
# Considera al 0 como par.

def main():
    lista = []
    numero = int(input())

    pares = 0
    impares = 0

    while numero >= 0:
        lista.append(numero)

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

        numero = int(input())

    print(f'PARES={pares}')
    print(f'IMPARES={impares}')

if __name__=='__main__':
    main()
