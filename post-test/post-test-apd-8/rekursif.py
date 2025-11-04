from time import sleep
from data import *

def rekursif():
    jawaban = input('|Mau keluar ( | Y / N | ): ').lower().replace(' ','').strip()
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

print(f'{BOLD}{GREEN}{atas}{RESET}')
print(f'{BOLD}{GREEN}{panjang}{RESET}')
print(f'{BOLD}{GREEN}|{RESET}{'GOODBYE MY FRIEND':^{105}}{BOLD}{GREEN}|{RESET}')
print(f'{BOLD}{GREEN}{panjang}{RESET}')
print(f'{BOLD}{GREEN}|{RESET}{'Remember, the finest steel is born from the fiercest fire.':^{105}}{BOLD}{GREEN}|{RESET}')
print(f'{BOLD}{GREEN}|{RESET}{'If the world starts to burn you, it only means you’re being forged into something stronger.':^{105}}{BOLD}{GREEN}|{RESET}')
print(f'{BOLD}{GREEN}|{RESET}{'Now go… and forge your own fate.':^{105}}{BOLD}{GREEN}|{RESET}')
print(f'{BOLD}{GREEN}{panjang}{RESET}')
print(f'{BOLD}{GREEN}{tengah}{RESET}')


