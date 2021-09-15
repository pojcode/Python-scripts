'''
Script which after a time given by user, send a chosen command to OS
timer is made using the Epoch time instead of time module to increase accuracy
'''
import time
import os
import keyboard

def set_time():
    # set the timer
    mode = ''
    while mode not in (1, 2, 3):
        os.system('cls')
        mode  = input("Set time in:   (1)hours   (2)minutes   (3)seconds" +
                "\n\n\t\t>> Select -> ").strip()
        mode = int(mode)
    modes = ('Hours', 'Minutes', 'Seconds')
    mode_selected = modes[mode-1]
    time_to_crono = ""
    while time_to_crono.replace('.', '').isdigit() == False:
        os.system('cls')
        print(f'Set a time in {mode_selected}\n')
        time_to_crono = input('\t>> TIME: ')
    value_to_crono = time_to_crono
    time_to_crono = float(time_to_crono)
    if mode == 1:
        time_to_crono = time_to_crono * 3600
    elif mode == 2:
        time_to_crono = time_to_crono * 60
    
    return time_to_crono, value_to_crono, mode_selected

def draw_timer(time_to_crono, value_to_crono, mode_selected):
    # print the timer
    time_total = time.time() + time_to_crono
    time_now = time.time()
    while int(time_total) >= int(time_now):
        os.system('cls')
        time_now = time.time()
        diff = int(time_to_crono - (time_total - time_now))
        print(f'TIMING {value_to_crono} {mode_selected}')
        print(f'\nTIME REMAINING >> {int(time_total - time_now) // 60} mins '
            f'{int(time_total - time_now) % 60} secs\n')
        print(f'PROGRESS '
            f'{int(((diff * 100)) // int(time_to_crono) * 0.2) * "#"} '
            f'{(diff * 100) // int(time_to_crono)}%')
        time.sleep(0.1)
    print('\nTIME FINISHED\n\n\n')

def send_command(command):
    # command must be a string (ctrl+v, alt+tab, esc...)
    keyboard.send(command, do_release=False)
    time.sleep(1.2)
    # ensure command is taken by the OS
    keyboard.send(command, do_press=False)

def main():
    while True:
        time, value, mode = set_time()
        draw_timer(time, value, mode)
        send_command('windows')
        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('Execute again?     y(YES)   n(NO)').lower()
        if answer == "n":
            break

if __name__ == '__main__':
    main()
