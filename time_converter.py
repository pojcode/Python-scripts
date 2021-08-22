""" 
Script that makes the following time conversions:
- seconds to minutes - get seconds -> return minutes and seconds
- seconds to hours - get seconds -> return hours, minutes and seconds
- minutes to seconds - get minutes, seconds -> return seconds
- minutes to hours - get minutes, seconds -> return hours, minutes, seconds
- hours to minutes - get hours, minutes, seconds -> return minutes, seconds
- hours to seconds - get hours, minutes, seconds -> return seconds
"""
import os
import time

# Constants
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

# Posible conversions MENU
options = (
    'seconds -> minutes', 'seconds -> hours', 'minutes -> seconds',
    'minutes -> hours', 'hours -> minutes', 'hours -> seconds'
    ) 

# Functions
def seconds_a_minutes(seconds):
    mins = seconds // SECONDS_IN_MINUTE
    segs = seconds % SECONDS_IN_MINUTE

    return mins, segs

def minutes_a_seconds(minutes, seconds):
    segs = minutes * SECONDS_IN_MINUTE + seconds

    return segs

def minutes_a_hours(minutes, seconds):
    hrs = minutes // MINUTES_IN_HOUR
    mins = minutes % MINUTES_IN_HOUR
    segs = seconds

    return hrs, mins, segs

def seconds_a_hours(seconds):
    mins, segs = seconds_a_minutes(seconds)
    hrs, mins, segs = minutes_a_hours(mins, segs)

    return hrs, mins, segs

def hours_a_minutes(hours, minutes, seconds):
    mins = hours * MINUTES_IN_HOUR + minutes
    segs = seconds

    return mins, segs

def hours_a_seconds(hours, minutes, seconds):
    mins, segs = hours_a_minutes(hours, minutes, seconds)
    segs = minutes_a_seconds(mins, segs)

    return segs


def menu():
    print('    ·CONVERSIONS·\n')
    for i in range(len(options)):
        print(f'({i + 1}) {options[i].title()}')
    print('(0) Exit')

def main():
    run = True
    while run:
        os.system('cls')
        menu()
        opt = ''
        while opt.isdigit() == False or 0 > int(opt) > len(options):
            os.system('cls')
            menu()
            opt = input('\n>> SELECT: ')
            # Option 0 Salir
            if opt == '0':    
                os.system('cls')
                print('\n\nThank you, see you soon...')
                input()
                run = False
            # Option 1 seconds a minutes
            elif opt == '1': 
                s = ''
                while s.isdigit() == False or 0 > int(s):
                    # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVERTING {options[0].title()} #\n\n')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                mins, segs = seconds_a_minutes(s)
                print(f'\nConversion ->    {mins} m : {segs} s'
                       '\n\n\n\n\n')
                input('Press ENTER to continue...')
            # Option 2 seconds a hours
            elif opt == '2':
                s = ''
                while s.isdigit() == False or 0 > int(s):
                    # Evita los tiempos negativos y si no es numero
                    os.system('cls')
                    print(f'# CONVERTING {options[1].title()} #\n\n')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                hrs, mins, segs = seconds_a_hours(s)
                print(f'\nConversion ->    {hrs} h : {mins} m : {segs} s'
                       '\n\n\n\n\n')
                input('Press ENTER to continue...')
            # Option 3 minutes a seconds
            elif opt == '3':
                m = ''
                while m.isdigit() == False or 0 > int(m):
                    os.system('cls')
                    print(f'# CONVERTING {options[2].title()} #\n\n')
                    m = input('Amount of minutes to convert -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # Evita los tiempos negativos y si no es numero 
                       # o es mayor de 60
                    os.system('cls')
                    print(f'# CONVERTING {options[2].title()} #\n\n')
                    print(f'Amount of minutes to convert -> {m}')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                segs = minutes_a_seconds(m, s)
                print(f'\nConversion ->    {segs} s\n\n\n\n\n')
                input('Press ENTER to continue...')
            # Option 4 minutes a hours
            elif opt == '4':
                m = ''
                while m.isdigit() == False or 0 > int(m):
                    os.system('cls')
                    print(f'# CONVERTING {options[3].title()} #\n\n')
                    m = input('Amount of minutes to convert -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                    # Evita los tiempos negativos y si no es numero
                    # o por encima de 60 segs
                    os.system('cls')
                    print(f'# CONVERTING {options[3].title()} #\n\n')
                    print(f'Amount of minutes to convert -> {m}')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                hrs, mins, segs = minutes_a_hours(m, s)
                print(f'\nConversion ->    {hrs} h : {mins} m : {segs} s'
                       '\n\n\n\n\n')
                input('Press ENTER to continue...')
            # Option 5 hours a minutes
            elif opt == '5':
                h = ''
                while h.isdigit() == False or 0 > int(h):
                    os.system('cls')
                    print(f'# CONVERTING {options[4].title()} #\n\n')
                    h = input('Amount of hours to convert -> ')
                h = int(h)
                m = ''
                while (m.isdigit() == False or 0 > int(m) or
                       int(m) >= MINUTES_IN_HOUR):
                    os.system('cls')
                    print(f'# CONVERTING {options[4].title()} #\n\n')
                    print(f'Amount of hours to convert -> {h}')
                    m = input('Amount of minutes to convert -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # all while's Avoid negative and non digits inputs
                    os.system('cls')
                    print(f'# CONVERTING {options[4].title()} #\n\n')
                    print(f'Amount of hours to convert -> {h}')
                    print(f'Amount of minutes to convert -> {m}')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                mins, segs = hours_a_minutes(h, m, s)
                print(f'\nConversion ->    {mins} m : {segs} s'
                       '\n\n\n\n\n')
                input('Press ENTER to continue...')
            # Option 6 hours a seconds
            elif opt == '6':
                h = ''
                while h.isdigit() == False or 0 > int(h):
                    os.system('cls')
                    print(f'# CONVERTING {options[5].title()} #\n\n')
                    h = input('Amount of hours to convert -> ')
                h = int(h)
                m = ''
                while (m.isdigit() == False or 0 > int(m) or
                       int(m) >= MINUTES_IN_HOUR):
                    os.system('cls')
                    print(f'# CONVERTING {options[5].title()} #\n\n')
                    print(f'Amount of hours to convert -> {h}')
                    m = input('Amount of minutes to convert -> ')
                m = int(m)
                s = ''
                while (s.isdigit() == False or 0 > int(s) or
                       int(s) >= SECONDS_IN_MINUTE):
                       # all while's Avoid negative and non digits inputs
                    os.system('cls')
                    print(f'# CONVERTING {options[5].title()} #\n\n')
                    print(f'Amount of hours to convert -> {h}')
                    print(f'Amount of minutes to convert -> {m}')
                    s = input('Amount of seconds to convert -> ')
                s = int(s)
                segs = hours_a_seconds(h, m, s)
                print(f'\nConversion ->    {segs} s\n\n\n\n\n')
                input('Press ENTER to continue...')
            else:
                print('\n\t\tInvalid option!!!')
                time.sleep(1.2)

if __name__ == '__main__':
    main()
                



