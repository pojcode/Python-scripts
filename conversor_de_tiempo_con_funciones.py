""" 
Programa que realiza las siguientess conversiones de tiempo
- segundos a minutos - recibe segundos y lo convierte a minutos y segundos
- segundos a horas - recibe segundos y devuelve horas, minutos y segundos
- minutos a segundos - recibe minutos y segundos y devuelve segundos
- minutos a horas - recibe minutos y segundos y devuelve
  horas, minutos y segundos
Además debera implementarse un metodo para imprimir el menu de opciones y 
la ejecucion del programa debe comenzar desde el procemiento "main"
"""

import os
import time

# Constantes

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

# Posibles conversiones MENU

options = (
    'segundos -> minutos', 'segundos -> horas', 'minutos -> segundos',
    'minutos -> horas', 'horas -> minutos', 'horas -> segundos'
    ) 

# Funciones

def segundos_a_minutos(segundos):
    mins = segundos // SECONDS_IN_MINUTE  # constante que vale 60
    segs = segundos % SECONDS_IN_MINUTE

    return mins, segs

def minutos_a_segundos(minutos, segundos):
    segs = minutos * SECONDS_IN_MINUTE + segundos

    return segs

def minutos_a_horas(minutos, segundos):
    hrs = minutos // MINUTES_IN_HOUR
    mins = minutos % MINUTES_IN_HOUR
    segs = segundos

    return hrs, mins, segs

def segundos_a_horas(segundos):
    mins, segs = segundos_a_minutos(segundos)
    hrs, mins, segs = minutos_a_horas(mins, segs)

    return hrs, mins, segs

def horas_a_minutos(horas, minutos, segundos):
    mins = horas * MINUTES_IN_HOUR + minutos
    segs = segundos

    return mins, segs

def horas_a_segundos(horas, minutos, segundos):
    mins, segs = horas_a_minutos(horas, minutos, segundos)
    segs = minutos_a_segundos(mins, segs)

    return segs


def menu():
    print('    ·CONVERSIONES·\n')
    for i in range(len(options)):
        print(f'({i + 1}) {options[i].title()}')
    print('(0) Exit')

def main():
    ejecutar = True
    while ejecutar:
        os.system('cls')
        menu()
        opt = ''
        while opt.isdigit() == False or 0 > int(opt) > len(options):
            os.system('cls')
            menu()
            opt = input('\nSelecciona una opción -> ')
            # Opcion 0 Salir
            if opt == '0':    
                os.system('cls')
                print('Gracias por utilizarme, nos vemos...')
                ejecutar = False
            # Opcion 1 Segundos a Minutos
            elif opt == '1': 
                s = ''
                while s.isdigit() == False or 0 > int(s):
                    # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[0].title()} #\n\n')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                mins, segs = segundos_a_minutos(s)
                print(f'\nEl resultado es ->    {mins} m : {segs} s'
                       '\n\n\n\n\n')
                os.system('pause')
            # Opción 2 Segundos a Horas
            elif opt == '2':
                s = ''
                while s.isdigit() == False or 0 > int(s):
                    # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[1].title()} #\n\n')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                hrs, mins, segs = segundos_a_horas(s)
                print(f'\nEl resultado es ->    {hrs} h : {mins} m : {segs} s'
                       '\n\n\n\n\n')
                os.system('pause')
            # Opción 3 Minutos a Segundos
            elif opt == '3':
                m = ''
                while m.isdigit() == False or 0 > int(m):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[2].title()} #\n\n')
                    m = input('Cantidad de minutos a convertir -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # Evita los tiempos negativos y si no es numero 
                       # o es mayor de 60
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[2].title()} #\n\n')
                    print(f'Cantidad de minutos a convertir -> {m}')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                segs = minutos_a_segundos(m, s)
                print(f'\nEl resultado es ->    {segs} s\n\n\n\n\n')
                os.system('pause')
            # Opción 4 Minutos a Horas
            elif opt == '4':
                m = ''
                while m.isdigit() == False or 0 > int(m):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[3].title()} #\n\n')
                    m = input('Cantidad de minutos a convertir -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                    # Evita los tiempos negativos y si no es numero
                    # o por encima de 60 segs
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[3].title()} #\n\n')
                    print(f'Cantidad de minutos a convertir -> {m}')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                hrs, mins, segs = minutos_a_horas(m, s)
                print(f'\nEl resultado es ->    {hrs} h : {mins} m : {segs} s'
                       '\n\n\n\n\n')
                os.system('pause')
            # Opción 5 Horas a Minutos
            elif opt == '5':
                h = ''
                while h.isdigit() == False or 0 > int(h):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[4].title()} #\n\n')
                    h = input('Cantidad de horas a convertir -> ')
                h = int(h)
                m = ''
                while (m.isdigit() == False or 0 > int(m) or
                       int(m) >= MINUTES_IN_HOUR):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[4].title()} #\n\n')
                    print(f'Cantidad de horas a convertir -> {h}')
                    m = input('Cantidad de minutos a convertir -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[4].title()} #\n\n')
                    print(f'Cantidad de horas a convertir -> {h}')
                    print(f'Cantidad de minutos a convertir -> {m}')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                mins, segs = horas_a_minutos(h, m, s)
                print(f'\nEl resultado es ->    {mins} m : {segs} s'
                       '\n\n\n\n\n')
                os.system('pause')
            # Opción 6 Horas a Segundos
            elif opt == '6':
                h = ''
                while h.isdigit() == False or 0 > int(h):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[5].title()} #\n\n')
                    h = input('Cantidad de horas a convertir -> ')
                h = int(h)
                m = ''
                while (m.isdigit() == False or 0 > int(m) or
                       int(m) >= MINUTES_IN_HOUR):
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[5].title()} #\n\n')
                    print(f'Cantidad de horas a convertir -> {h}')
                    m = input('Cantidad de minutos a convertir -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVIRTIENDO {options[5].title()} #\n\n')
                    print(f'Cantidad de horas a convertir -> {h}')
                    print(f'Cantidad de minutos a convertir -> {m}')
                    s = input('Cantidad de segundos a convertir -> ')
                s = int(s)
                segs = horas_a_segundos(h, m, s)
                print(f'\nEl resultado es ->    {segs} s\n\n\n\n\n')
                os.system('pause')
            else:
                print('\n               Opción no válida!!!')
                time.sleep(1.2)

if __name__ == '__main__':
    main()
                



