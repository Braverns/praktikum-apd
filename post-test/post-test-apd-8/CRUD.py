from time import sleep
import os
from data import *
from menu import *

def create_m():
    menu('Blacksmith’s Table', '', '', '')
    nama = input('|Masukkan nama senjata: ').title()
    print('\033[F', end='')   
    print(f'|Masukkan nama senjata : {nama:<{81}}|')

    atk = input('|Memperkuat ATK        : ').strip()
    print('\033[F', end='')   
    print(f'|Memperkuat ATK        : {atk:<{81}}|')

    aspd = input('|Memperkuat ASPD       : ').strip()
    print('\033[F', end='')   
    print(f'|Memperkuat ASPD       : {aspd:<{81}}|')

    crit = input('|Memperkuat %CRIT      : ').strip()
    print('\033[F', end='')   
    print(f'|Memperkuat %CRIT      : {crit:<{81}}|')
    print(tengah)
    sleep(1)

    if not atk.isdigit() or not aspd.isdigit() or not crit.isdigit() or int(crit) > 100 or int(atk) > 999 or int(aspd) > 999 or nama.strip() == '' or len(nama) > 70:
        menu('PENAMBAHAN ATRIBUT GAGAL!', '', f'\n{panjang}', f'\n|{'Nama tidak boleh kosong atau melebihi 70 karakter!':^{105}}|' + 
                f'\n|{'Atribut harus berupa angka bulat positif!':^{105}}|' +
                f'\n|{'Batas ATK & ASPD adalah 999 serta batas crit 100%!':^{105}}|')
        reset('|Enter untuk mengulang ...')       

    else:
        next_id_senjata = max(senjata.keys()) + 1 if senjata else 1
        senjata[next_id_senjata] = {
            'nama': nama, 'atk': int(atk), 'aspd': int(aspd), 'crit': int(crit)
        }
        salah(f'|{'Senjata berhasil dibuat!!':^{105}}|' + f'\n|{f'{nama} | ATK: {atk} | ASPD: {aspd} | CRIT: {crit}%':^{105}}|')
        reset('|Enter untuk kembali ke menu ...')
        return senjata[next_id_senjata]
    
def daftar(data, tutup):
        for i, (id, s) in enumerate(data, start=1):
                                print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
        print(tutup)