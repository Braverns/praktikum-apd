from time import sleep
from data import *

def rekursif(): 
    jawaban = input('|Mau keluar ( | Y / N | ): ').lower().strip() 
    print('\033[F', end='')   
    print(f'|Mau keluar ( | Y / N | ): {jawaban:<{79}}|')
    if jawaban == "y": 
        print(tengah)   
        sleep(1)
    elif jawaban == 'n':
        rekursif()
    else:
        print(panjang)
        print(f'|{'Jawaban anda tidak sesuai!':^{105}}|')
        print(panjang)
        rekursif()
    return jawaban
