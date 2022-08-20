import sys

try:
    nota_1 = float(sys.argv[1])
    nota_2 = float(sys.argv[2])
    if (nota_1 >= 0 and nota_1 <= 10)  and (nota_2 >= 0 and nota_2 <= 10):
        if (nota_1 >= 7)  and (nota_2 >= 7):
            print('Promocionado')
        elif (nota_1 >= 4)  and (nota_2 >= 4):
            print('Aprobado, debe rendir final')
        elif (nota_1 < 4) and (nota_2 < 4):
            print('Desaprobó ambos parciales, debe recursar')
        elif (nota_1 < 4) or (nota_2 < 4):
            if nota_1 < 4:
                print('Desaprobado, debe recuperar el primer parcial')
            else:
                print('Desaprobado, debe recuperar el segundo parcial')
    else:
        print('ERROR: Los argumentos deden ser números enteros entre 0 y 10')
except:
    print('Debe ingresar 2 notas')
