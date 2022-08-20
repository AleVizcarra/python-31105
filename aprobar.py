import sys


try:
    nota1 = float(sys.argv[1])
    nota2 = float(sys.argv[2])
    print(f'La nota 1 es {nota1} y la nota 2 es {nota2}')
    print(f'El promedio es: {(nota1 + nota2)/2}')
except Exception as a:
    print(a)
    print('Es necesario que ingreses 2 notas')