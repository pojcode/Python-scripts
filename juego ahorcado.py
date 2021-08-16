'''
Juego del ahorcado que consiste en acertar la palabra escondida mediante
las letras que la componen si fallar mas de 5 veces
'''
import random
import os

paises = ('Albania','Alemania','Andorra','Austria','Azerbaiyan','Belgica',
'Bielorrusia','Bosnia Herzegovina','Bulgaria','Chipre','Croacia','Dinamarca',
'España','Estonia','Finlandia','Francia','Grecia','Hungria','Irlanda',
'Islandia','Italia','Letonia','Liechtenstein','Lituania','Luxemburgo',
'Macedonia','Malta','Moldavia','Monaco','Montenegro','Noruega',
'Paises Bajos','Polonia','Portugal','Reino Unido','Rumania','Rusia','Serbia',
'Suecia','Suiza','Ucrania','Ciudad del Vaticano')

def choose_country():
    pais_original = random.choice(paises).upper()
    
    return pais_original

def guess_country(pais_original):
    pais_secreto = '#' * len(pais_original)
    fallos = 5
    while pais_secreto != pais_original and fallos > 0:
        os.system('cls')
        print('\n\nAdivina el siguiente PAIS ->   ', pais_secreto,
              '\t\tFALLOS Restantes ->', fallos)
        letra = input('\n\n\n\t>> LETRA a averiguar -> ').upper().strip()
        if letra in pais_original and len(letra) == 1:
            start_find = 0
            for i in range(pais_original.count(letra)):
                position = pais_original.find(letra, start_find)
                pais_secreto = (pais_secreto[:position] + letra +
                                pais_secreto[position + 1:])
                start_find = position + 1
            start_find = 0
            if ' ' in pais_original: # si letra ant y post != '#', pinta ' ' 
                for i in range(pais_original.count(' ')):
                    position = pais_original.find(' ', start_find)
                    if (pais_secreto[position - 1] != '#' and
                        pais_secreto[position + 1] != '#'):
                        pais_secreto = (pais_secreto[:position] + ' ' +
                                        pais_secreto[position + 1:])
                        start_find = position + 1
            print(f'\n\nAcertaste la letra {letra}'
                   ' se encuentra en el nombre del país\n\n\n\n')
        else:
            if letra.isalpha() and len(letra) == 1:
                print(f'\n\nERROR, la letra {letra} no se encuentra en'
                       ' el nombre del país\n\n\n\n')
                fallos -= 1
            else:
                print(f'\n\n{letra} no es un carácter válido\n\n\n\n')
        os.system('pause')

    return fallos

def main():
    os.system('cls')
    print('\n\n\n\n\t\t   BIENVENIDO AL JUEGO DEL AHORCADO\n\n\n')
    print('\tAcierta el nombre del pais europeo escondido tras "#".' 
          '\n\tTienes 5 fallos posibles a la hora de elegir la letra\n\n\n\n')
    os.system('pause')
    while True:
        pais = choose_country()
        resultado = guess_country(pais)
        resp = ''
        while resp != 'y' and resp != 'n':
            os.system('cls')
            if resultado > 0:
                print('\n\n\n\tENHORABUENA ACERTASTE EL PAIS!!!\n\n')
                print(f'\t·Pais -> {pais.lower().title()}'
                      f'      ·Errores -> {5 - resultado}')
            else:
                print(f'\n\n\n\tHAS FALLADO,'
                      f' el país era {pais.lower().title()}')
            
            resp = input('\n\n\n\nVolver a jugar?   y(SI)'
                         '   n(NO)   ').lower().strip()
        if resp == 'n':
            break

if __name__ == '__main__':
    main()