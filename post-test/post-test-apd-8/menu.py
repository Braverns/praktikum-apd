from time import sleep
import os
from data import *
from prettytable import PrettyTable


def pretable(judul, isi1, isi2,space, space2, isi3, isi4, isi5, isi6, warna1, warna2, warna3, bawah):
    os.system('cls || clear')  

    table = PrettyTable()
    table.field_names = [f"{BOLD}{REVERSE}{warna1}{judul}{RESET}"]
    table.add_row([f"{BOLD}{REVERSE}{warna2}{isi1}{RESET}"])
    table.add_row([f"{BOLD}{REVERSE}{warna2}{isi2}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{space}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{isi3}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{isi4}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{isi5}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{isi6}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{space2}{RESET}"])
    table.add_row([f"{REVERSE}{BOLD}{UNDERLINE}{warna3}{bawah}{RESET}"])
    col_width = 105

    for i, row in enumerate(table._rows):
        text = row[0]
        if i < 2:
            table._rows[i][0] = text.center(col_width)
        else:
            table._rows[i][0] = text.ljust(col_width)

    table.junction_char = f"{BOLD}{BORDER_COLOR}╬{RESET}"
    table.horizontal_char = f"{BOLD}{BORDER_COLOR}═{RESET}"
    table.vertical_char = f"{BOLD}{BORDER_COLOR}║{RESET}"
    table.left_junction_char = f"{BOLD}{BORDER_COLOR}╠{RESET}"
    table.right_junction_char = f"{BOLD}{BORDER_COLOR}╣{RESET}"
    table.top_junction_char = f"{BOLD}{BORDER_COLOR}╦{RESET}"
    table.bottom_junction_char = f"{BOLD}{BORDER_COLOR}╩{RESET}"
    table.top_left_junction_char = f"{BOLD}{BORDER_COLOR}╔{RESET}"
    table.top_right_junction_char = f"{BOLD}{BORDER_COLOR}╗{RESET}"
    table.bottom_left_junction_char = f"{BOLD}{BORDER_COLOR}╚{RESET}"
    table.bottom_right_junction_char = f"{BOLD}{BORDER_COLOR}╝{RESET}"
    table._max_width = {f"{judul}": col_width}
    table.align[f"{judul}"] = "c"

    return table



def menu(judul, subjudul, isi, isi2):
    os.system('cls || clear')
    print(atas)
    print(panjang)
    print(f'|{judul:^{105}}|', end = '')
    print(subjudul)
    print(tengah, end = '')
    print(isi, end = '')
    print(isi2)
    print(panjang)

def enter(isi):
    answer = input(isi).strip()
    print('\033[F', end='')   
    print(f'{isi}{answer:<{106 - len(isi)}}|')
    print(tengah)   
    sleep(1)
    return answer

def reset(kata1):
    ulang = input(kata1)
    print('\033[F', end='')   
    print(f'{kata1}{ulang:<{106-len(kata1)}}|')
    print(tengah)
    sleep(1)


def salah(kata):
    print(panjang)
    print(kata)
    print(panjang)

def lenerror(isi1, isi2):
                print(isi1)
                print(isi2)
                

            
