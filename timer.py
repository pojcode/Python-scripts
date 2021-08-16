'''
Script that represents a timer you can set using hours, minutes and seconds.
You can use one, two or all of them to set it since time is converted 
previously to seconds. maximun time is 99h:59m:59s just to set a limit
'''
import time
import os

def convertion(hours, minutes, seconds):
    hours = hours * 3600
    minutes = minutes * 60
    time_to_convert = hours + minutes + seconds

    h = time_to_convert // 3600
    m = (time_to_convert - h*3600) // 60
    s = time_to_convert - h*3600 - m*60

    return h, m, s

def draw_crono(hours, minutes, seconds):
    for i in range(hours + 1):    # +1 to get into the loop when h = 0
        if minutes == 0 and seconds == 0:
            minutes = 60
            hours -= 1
        for j in range(minutes + 1):
            if seconds == 0:
                seconds = 60
                minutes -= 1
            for k in range(seconds):
                os.system('cls')
                seconds -= 1
                print('        ________________\n'
                      '        |# CRONOMETER #|\n'
                      '        """"""""""""""""\n'
                      '        |#  '
                     f'{str(hours).zfill(2)}:'
                     f'{str(minutes).zfill(2)}:'
                     f'{str(seconds).zfill(2)}'
                     # zfill() adding 0 on left side 08, 07 etc...
                      '  #|\n'
                      '        """"""""""""""""'
                     )
                time.sleep(1)

def set_time():
    while True:
        max_time = 99*3600 + 59*60 + 59  # maximun time supported 99h:59m:59s
        hrs = ''
        while hrs.isdigit() == False or int(hrs) < 0:
            os.system('cls')
            print('    ## CRONOMETER ##\n')   
            hrs = input('>> |SET the TIMER| --- HOURS: ')
        total_time = int(hrs)*3600
        if total_time > max_time:
            print('\nTIME SET IS TOO HIGH!!\n\n\n')
            os.system('pause')
            continue
        mins = ''
        while mins.isdigit() == False or int(mins) < 0:
            os.system('cls')
            print('    ## CRONOMETER ##\n')   
            print(f'|SET the TIMER| --- HOURS -> {hrs}')
            mins = input('>> |SET the TIMER| --- MINUTES: ')
        total_time = total_time + int(mins)*60
        if total_time > max_time:
            print('\nTIME SET IS TOO HIGH!!\n\n\n')
            os.system('pause')
            continue
        secs = ''
        while secs.isdigit() == False or int(secs) < 0:
            os.system('cls')
            print('    ## CRONOMETER ##\n')   
            print(f'|SET the TIMER| --- HOURS -> {hrs}')
            print(f'|SET the TIMER| --- MINUTES -> {mins}')
            secs = input('>> |SET the TIMER| --- SECONDS: ')
        total_time = total_time + int(secs)
        if total_time > max_time:
            print('\nTIME SET IS TOO HIGH!!\n\n\n')
            os.system('pause')
            continue
        else:
            return int(hrs), int(mins), int(secs)

def main():
    while True:
        os.system('mode con: cols=41 lines=13')
        # set the size for the script´s window
        hrs, mins, secs = set_time()
        h, m, s = convertion(hrs, mins, secs)
        draw_crono(h, m, s)
        resp = ""
        while resp != "y" and resp != "n":
            os.system('cls')
            print('        ________________\n'
                  '        |# CRONOMETER #|\n'
                  '        """"""""""""""""\n'
                  '        |#  '
                  '00:00:00'
                  '  #|\n'
                  '        """"""""""""""""'
                 )
            resp = input("\n\nSET TIMER AGAIN??  y(YES)   n(NO) ").lower()
        if resp == "n":
            break

if __name__ == '__main__':
    main()
        



    


    
    
    
