# Programa que pregunta cuántos elementos se agregarán a una lista. 
# Después debe leer esa cantidad de datos e ingresarlos a la lista.
# Luego debe crear dos listas, una con los valores pares de la lista original 
# y otra con los valores impares de la lista original.

def main():
    lista = []
    cantidad = int(input())

    for i in range(cantidad):
        numero = int(input())
        lista.append(numero)

    pares = []
    impares = []

    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    print('LISTA ORIGINAL')
    print(f'{lista}')

    print('PARES')
    print(f'{pares}')
    
    print('IMPARES')
    print(f'{impares}')

if __name__=='__main__':
    main()
