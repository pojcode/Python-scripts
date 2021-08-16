import random
import os
import time


os.system("cls")
print('\n\n\t### GUESS THE NUMBER!!! ###\n\n\t\tMAN vs CPU'
        '\n\n\t  Will YOU be able to WIN')
time.sleep(5)
play = True
while play:
    user = ""
    while user == "":
        os.system("cls")
        print('######## GUESS THE NUMBER ########\n\n\n')
        user = input("Type your username -> ").strip().title()
    num = random.randint(1, 1000)
    min, max = 1, 1000
    resp = None
    cpu = None
    while resp != num and cpu != num:
        os.system("cls")
        cpu = random.randint(min, max)
        if cpu < num:
            cpu_play = f"CPU chooses number {cpu} but fails, it´s GREATER"
            min = cpu + 1
        elif cpu > num:
            cpu_play = f"CPU chooses number {cpu} but fails, it´s LOWER"
            max = cpu - 1
        else:
            cpu_play = f"CPU GUESSED the NUMBER FIRST, YOU have LOST "\
                       f"{user}, NEXT TIME..., NUMBER = {num}\n\n\n\n"
        print('######## GUESS THE NUMBER ########\n\n\n')
        print(cpu_play)

        if cpu != num:
            print("\n")
            resp = ''
            while resp.isdigit() == False:
                os.system('cls')
                print('######## GUESS THE NUMBER ########\n\n\n')
                print(cpu_play)
                resp = input(f"\n\n\n{user} between {min} and {max} "
                              "what´s the number -> ").strip()
                if resp.isdigit == False:
                    print("\n\nYOUR input is NOT a NUMBER\n")
            resp = int(resp)
            if resp < num:
                print("\n\nNO, the number is GREATER")
                if resp > min:
                    min = resp
            elif resp > num:
                print("\n\nNO, the number is LOWER")
                if resp < max:
                    max = resp
            else:
                print(f"\n\nThat´s RIGHT {user}, YOU have WON, NUMBER = {num}")
            input('\n\n\n\n\n\nPress ENTER to continue...')
    
    reset = ''
    while reset != "y" and reset != "n":
        reset = input("\nPlay again?      y(YES)   n(NO)").lower()
    if reset == "n":
        jugar = False




