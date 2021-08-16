import os
import time

def menu():
    opt = ''
    while opt != 'i' and opt != 'r':
        os.system('cls')
        print('#TABLAS DE MULTIPLICAR#'.center(43))
        print('\n\nTabla INDIVIDUAL "N" o RANGO de tablas hasta "N"')
        opt = input('\n\t·Individual(i)     ·Rango(r)'
                    '\n\n\t       >> SELECT -> ')
    num = ''
    while num.isdigit() == False:
        os.system('cls')
        print('#TABLAS DE MULTIPLICAR#'.center(43))
        if opt == 'i':
            print('\n\n\t     Tabla INDIVIDUAL')
        elif opt == 'r':
            print('\n\n\t     RANGO de tablas')
        num = input('\n\t       Numero N -> ')
        if num.isdigit() and (int(num) > 999 or int(num) == 1):
            if int(num) == 1:
                print('\n\n\t      1 no es un RANGO!!')
            else:
                print('\n\n\t   Numero demasiado grande!!')
            num = ''
            time.sleep(1.5)
    multiplos = ''
    while (multiplos.isdigit() == False or
           int(multiplos) < 0 or int(multiplos) > 25):
        os.system('cls')
        print('#TABLAS DE MULTIPLICAR#'.center(43))
        if opt == 'i':
            print('\n\n\t     Tabla INDIVIDUAL'.center(43))
        elif opt == 'r':
            print('\n\n\t     RANGO de tablas'.center(43))
        print('\n\t       Numero N ->', num)
        multiplos = input('\n\tCuantos multiplos? (max=25) -> ')

    return opt, int(num), int(multiplos)

def tablas(opt, num, multiplos):
    os.system('cls')
    print('#TABLAS DE MULTIPLICAR#'.center(43))
    if opt == 'i':
        print('\n\n\t\tTABLA del', num, '\n')
        for multiplo in range(1, multiplos + 1):
            print(f'\t\t{num} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                  f'= {num * multiplo}')
    elif opt == 'r':
        cont = 0
        for rango in range(1, num // 3 + 1):
            print('\nTABLA del', rango + cont, '\t\tTABLA del',
                  rango + cont + 1, '\t\tTABLA del', rango + cont + 2, '\n')
            for multiplo in range(1, multiplos + 1):
                print(f'{rango + cont} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                      f'= {(rango + cont) * multiplo}'
                      f'\t\t{rango + cont + 1} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                      f'= {(rango + cont + 1) * multiplo}'
                      f'\t\t{rango + cont + 2} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                      f'= {(rango + cont + 2) * multiplo}')
            cont += 2
        if num % 3 != 0:
            for rango in range(1):
                if num % 3 == 1:
                    print('\nTABLA del', num, '\n')
                elif num % 3 == 2:
                    print('\nTABLA del', num - 1, '\t\tTABLA del', num, '\n')    
                for multiplo in range(1, multiplos + 1):
                    if num % 3 == 1:
                        print(f'{num} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                              f'= {num * multiplo}')
                    elif num % 3 == 2:
                        print(f'{num - 1} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                              f'= {(num - 1) * multiplo}'
                              f'\t\t{num} x {multiplo}{" " * (3 - len(str(multiplo)))}'
                              f'= {num * multiplo}')

def main():
    while True:
        option, numero, num_multiplos = menu()
        tablas(option, numero, num_multiplos)
        print('\n\n\n')
        resp = ''
        while resp != 'y' and resp != 'n':
            resp = input('Ejecutar de nuevo?    y(SI)  n(NO)  ')
        if resp == 'n':
            break

if __name__ == '__main__':
    main()


     