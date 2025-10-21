import os
from random import randint, choice
from time import sleep

huruf_A = [
    '    /\\ ',
    '     /  \\ ',
    '     /    \\ ',
    '     /      \\ ',
    '     /--------\\ ',
    '     /          \\ ',
    '     /            \\ ',
    '     /              \\ '
]

huruf_B = [
    '|‾‾‾‾‾‾‾‾‾\\ ',
    '|          \\ ',
    '|          |',
    '|         / ',
    '|---------\\ ',
    '|          \\ ',
    '|           |',
    '|           |',
    '|__________/ '
]

huruf_C = [
    '      __________',
    '       /          \\ ',
    ' /         ',
    '|          ',
    '|          ',
    '|          ',
    ' \\         ',
    '     \\          /',
    '      ‾‾‾‾‾‾‾‾‾‾ '
]

huruf_D = [
    '|‾‾‾‾‾‾‾‾‾‾\\',
    '  |           \\ ',
    '   |            \\ ',
    '   |             |',
    '   |             |',
    '   |             |',
    '   |            / ',
    '  |           / ',
    '|__________/ '
]

huruf_dict = {
    'A': huruf_A,
    'B': huruf_B,
    'C': huruf_C,
    'D': huruf_D
}

panjang = f'|{' '*105}|'
tengah =  f'|{'_'*105}|'
atas = f'{'_'*107}'


senjata = {}
next_id_senjata = 1
next_id_senjata_m = 1

data_murid = {}

while True:
    os.system('cls || clear')
    print(atas)
    print(panjang)
    print(f'|{'THE BLACKSMITH':^{105}}|')
    print(tengah)
    print(f'|{'Through fire and hammer, the blacksmith shapes the world.':^{105}}|' + f'\n|{'Are You One Of Us?':^{105}}|')
    print(f'|{'1. Master':<{105}}|' + f'\n|{'2. Murid':<{105}}|' + f'\n|{'3. Daftar Sebagai Murid':<{105}}|' + f'\n|{'4. Log Out':<{105}}|')
    print(panjang)

    answer = input('|Ingin masuk sebagai apa, tentukan pilihan (1|2|3|4): ').strip()
    print('\033[F', end='')   
    print(f'|Ingin masuk sebagai apa, tentukan pilihan (1|2|3|4): {answer:<{52}}|')
    print(tengah)   
    sleep(1)

    if answer == '1':
        os.system('cls || clear')
        print(atas)      
        print(panjang)
        print(f'|{'GERBANG MASUK MASTER':^{105}}|')
        print(tengah)
        print(panjang)
        un = input('|Username anda: ').strip().lower().replace(' ', '')
        print('\033[F', end='')   
        print(f'|Username anda: {un:<{90}}|')
        pw = input('|Password anda: ').strip().lower().replace(' ', '')
        print('\033[F', end='')   
        print(f'|Password anda: {pw:<{90}}|')
        print(tengah)
        sleep(1)

        if un == 'admin' and pw == 'admin123':
            while True:
                os.system('cls || clear')
                print(atas)
                print(panjang)
                print(f'|{'SELAMAT DATANG MASTER':^{105}}|')
                print(f'|{'APA YANG INGIN ANDA LAKUKAN?':^{105}}|')
                print(tengah)
                print(f'|{'1. Membuat dan Menempa Senjata':<{105}}|' + f'\n|{'2. Daftar Senjata':<{105}}|' + f'\n|{'3. Memodifikasi Senjata':<{105}}|' + 
                      f'\n|{'4. Hancurkan Senjata':<{105}}|' + f'\n|{'5. Murid':<{105}}|' + f'\n|{'6. Keluar':<{105}}|')
                print(panjang)

                pilihan = input('|Tentukan pilihan (1|2|3|4|5|6): ').strip()
                print('\033[F', end='')   
                print(f'|Tentukan pilihan (1|2|3|4|5|6): {pilihan:<{73}}|')
                print(tengah)
                sleep(1)

                if pilihan == '1':
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'Blacksmith’s Table':^{105}}|')
                    print(tengah)
                    print(panjang)

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

                    if not atk.isdigit() or not aspd.isdigit() or not crit.isdigit() or int(crit) > 100 or int(atk) > 999 or int(aspd) > 999 or nama.strip() == '' or len(nama) > 70:
                        print(tengah)
                        print(panjang)
                        print(f'|{'PENAMBAHAN ATRIBUT GAGAL!':^{105}}|')
                        print(tengah)
                        print(panjang)
                        print(f'|{'Nama tidak boleh kosong atau melebihi 70 karakter!':^{105}}|')
                        print(f'|{'Atribut harus berupa angka bulat positif!':^{105}}|')
                        print(f'|{'Batas ATK & ASPD adalah 999 serta batas crit 100%!':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk mengulang ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk mengulang ...{reset:^{80}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        next_id_senjata = max(senjata.keys()) + 1 if senjata else 1
                        senjata[next_id_senjata] = {
                            'nama': nama, 'atk': int(atk), 'aspd': int(aspd), 'crit': int(crit)
                        }
                        print(panjang)
                        print(f'|{'Senjata berhasil dibuat!!':^{105}}|')
                        print(f'|{f'{nama} | ATK: {atk} | ASPD: {aspd} | CRIT: {crit}%':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilihan == '2':
                    if len(senjata) == 0:
                        print(panjang)
                        print(f'|{'Belum ada senjata':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        os.system('cls || clear')
                        print(atas)
                        print(panjang)
                        print(f'|{'DAFTAR SENJATA':^{105}}|')
                        print(tengah)
                        for i, (id, s) in enumerate(senjata.items(), start=1):
                            print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilihan == '3':
                    if len(senjata) == 0:
                        print(panjang)
                        print(f'|{'Belum ada senjata':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        os.system('cls || clear')
                        print(atas)
                        print(panjang)
                        print(f'|{'Blacksmith Table':^{105}}|')
                        print(panjang)
                        print(tengah)

                        for i, (id, s) in enumerate(senjata.items(), start=1):
                            print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
                        print(panjang)
                        
                        ubah = input('|Masukkan nomor senjata yang ingin diubah: ').strip()
                        print('\033[F', end='')   
                        print(f'|Masukkan nomor senjata yang ingin diubah: {ubah:<{63}}|')        
                        
                        if not ubah.isdigit() or int(ubah) <= 0 or int(ubah) > len(senjata):
                            print(tengah)
                            print(panjang)
                            print(f'|{'Pilihan tidak tersedia!':^{105}}|')
                            print(tengah)
                            reset = input('|Enter untuk kembali ke menu ...')
                            print('\033[F', end='')   
                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                            print(tengah)
                            sleep(1)
                            continue

                        else:
                            ubah = int(ubah)
                            print(tengah)
                            print(f'|{'1. Ubah nama':<{105}}|' + f'\n|{'2. Ubah ATK':<{105}}|' + f'\n|{'3. Ubah ASPD':<{105}}|' + f'\n|{'4. Ubah %CRIT':<{105}}|')
                            print(panjang)

                            ubah2 = input('|Apa yang ingin diubah (1|2|3|4): ').strip()
                            print('\033[F', end='')   
                            print(f'|Apa yang ingin diubah (1|2|3|4): {ubah2:<{72}}|')
                            print(tengah)
                            sleep(1)

                            if ubah2 not in ['1','2','3','4']:
                                os.system('cls || clear')
                                print(atas)
                                print(panjang)
                                print(f'|{'Pilihan tidak tersedia!':^{105}}|')
                                print(tengah)
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                            else:
                                if ubah2 == '1':
                                    print(tengah)
                                    print(panjang)
                                    nama_baru = input('|Nama baru: ').title()
                                    print('\033[F', end='')   
                                    print(f'|Nama baru: {nama_baru:<{94}}|')
                                    print(panjang)

                                    if nama_baru.strip() == '' or len(nama_baru) > 70:
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'GAGAL MENGUBAH NAMA!':^{105}}|')
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'Nama tidak boleh kosong dan tidak boleh melebihi 70 karakter!':^{105}}|')
                                        print(panjang)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                    else:
                                        senjata[ubah]['nama'] = nama_baru
                                        print(f'|{f'{nama} telah diubah menjadi {nama_baru}':^{105}}|')
                                        print(tengah)

                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                elif ubah2 == '2':
                                    print(tengah)
                                    print(panjang)
                                    nilai = input('|Masukkan nilai baru ATK: ').strip()
                                    print('\033[F', end='')   
                                    print(f'|Masukkan nilai baru ATK: {nilai:<{80}}|')
                                    print(panjang)
                                

                                    if not nilai.isdigit() or int(nilai) > 999:
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'GAGAL MENGUBAH ATK!':^{105}}|')
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'Atribut harus berupa angka bulat positif dan tidak boleh melebihi angka 999!':^{105}}|')
                                        print(panjang)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                    else:
                                        senjata[ubah]['atk'] = int(nilai)
                                        print(f'|{f'ATK : {atk} telah diubah menjadi {nilai}':^{105}}|')

                                        print(tengah)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue              

                                elif ubah2 == '3':
                                    print(tengah)
                                    print(panjang)
                                    nilai = input('|Masukkan nilai baru ASPD: ').strip()
                                    print('\033[F', end='')   
                                    print(f'|Masukkan nilai baru ASPD: {nilai:<{79}}|')
                                    print(panjang)

                                    if not nilai.isdigit() or int(nilai) > 999:
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'GAGAL MENGUBAH ASPD!':^{105}}|')
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'Atribut harus berupa angka bulat positif dan tidak boleh melebihi angka 999!':^{105}}|')
                                        print(panjang)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                    else:
                                        senjata[ubah]['aspd'] = int(nilai)
                                        print(f'|{f'ASPD : {aspd} telah diubah menjadi {nilai}':^{105}}|')
                                        print(tengah)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue 
                                    
                                else:
                                    print(tengah)
                                    print(panjang)
                                    nilai = input('|Masukkan nilai baru CRIT: ').strip()
                                    print('\033[F', end='')   
                                    print(f'|Masukkan nilai baru CRIT: {nilai:<{79}}|')
                                    print(panjang)

                                    if not nilai.isdigit() or int(nilai) > 100:
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'GAGAL MENGUBAH CRIT!':^{105}}|')
                                        print(tengah)
                                        print(panjang)
                                        print(f'|{'Atribut harus berupa angka bulat positif dan batas CRIT 100%!':^{105}}|')
                                        print(panjang)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                    else:
                                        senjata[ubah]['crit'] = int(nilai)
                                        print(f'|{f'CRIT : {crit}% telah diubah menjadi {nilai}%':^{105}}|')
                                        print(tengah)
                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue 

                elif pilihan == '4':
                        
                        if len(senjata) == 0:
                            print(panjang)
                            print(f'|{'Belum ada senjata':^{105}}|')
                            print(panjang)
                            reset = input('|Enter untuk kembali ke menu ...')
                            print('\033[F', end='')   
                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                            print(tengah)
                            sleep(1)
                            continue

                        else:
                            os.system('cls || clear')
                            print(atas)
                            print(panjang)
                            print(f'|{'HANCURKAN SENJATA':^{105}}|')
                            print(panjang)
                            print(tengah)

                            for i, (id, s) in enumerate(senjata.items(), start=1):
                                print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
                                
                            print(panjang)
                            hapus = input('|Masukkan nomor senjata yang ingin hancurkan: ').strip()
                            print('\033[F', end='')   
                            print(f'|Masukkan nomor senjata yang ingin hancurkan: {hapus:<{60}}|')
                            
                            if not hapus.isdigit() or int(hapus) == 0 or int(hapus) > len(senjata):
                                print(tengah)
                                print(panjang)
                                print(f'|{'Pilihan tidak tersedia!':^{105}}|')
                                print(tengah)
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                            else:
                                print(panjang)
                                print(f'|{f'Senjata {senjata[int(hapus)]['nama']} telah dihancurkan.':^{105}}|')
                                senjata.pop(int(hapus))

                                print(tengah)
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                elif pilihan == '5':
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'DAFTAR MURID':^{105}}|')
                    print(tengah)

                    if len(data_murid) == 0:
                        print(f'|{'Belum ada murid yang terdaftar!':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                   
                    for i, username in enumerate(data_murid.keys(), start=1):
                        print(f'|{f"{i}. {username}":<{105}}|')
                    print(panjang)

                    pilihanurid = input('|Pilih nomor murid untuk melihat senjatanya: ').strip()
                    print('\033[F', end='')   
                    print(f'|Pilih nomor murid untuk melihat senjatanya: {pilihanurid:<{61}}|')
                    print(tengah)
                    sleep(1)

                    if not pilihanurid.isdigit() or int(pilihanurid) <= 0 or int(pilihanurid) > len(data_murid):
                        print(panjang)
                        print(f'|{'Pilihan tidak tersedia!':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    pilihanurid = int(pilihanurid)
                    username_terpilih = list(data_murid.keys())[pilihanurid - 1]
                    murid = data_murid[username_terpilih]

                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{f"DAFTAR SENJATA MURID: {username_terpilih.upper()}":^{105}}|')
                    print(tengah)

                    if len(murid["senjata"]) == 0:
                        print(panjang)
                        print(f'|{'Murid ini belum membuat senjata apapun.':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    print(f'|{'IRON: ' + str(murid["iron"]) + ' | ORE: ' + str(murid["ore"]):<{105}}|')
                    print(panjang)
                    for i, (id, s) in enumerate(murid["senjata"].items(), start=1):
                        print(f'|{f"{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%":<{105}}|')
                    print(tengah)

                    print(panjang)
                    nilai = input('|Masukkan nilai murid (A | B | C | D): ').upper().strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan nilai murid (A | B | C | D): {nilai:<{67}}|')
                    print(panjang)

                    if nilai not in ['A', 'B', 'C', 'D']:
                        print(tengah)
                        print(f'|{'Nilai tidak sesuai!':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    murid['nilai'] = nilai
                    print(f'|{'Nilai berhasil diberikan':^{105}}|')
                    print(tengah)
                    print(panjang)
                    print(f'|{'Memberi murid bahan-bahan untuk menempa':^{105}}|' + f'\n|{'Masukkan angka "0" jika tidak mau':^{105}}|')
                    ore = input('|Berikan Ore ke murid: ').strip().replace(' ', '')
                    print('\033[F', end='')   
                    print(f'|Berikan Ore ke murid  : {ore:<{81}}|')
                    iron = input('|Berikan Iron ke murid : ').strip().replace(' ', '')
                    print('\033[F', end='')   
                    print(f'|Berikan Iron ke murid : {ore:<{81}}|')
                    print(panjang)

                    if not ore.isdigit or not iron.isdigit or int(iron) > 1000 or int(ore) > 1000:
                        print(tengah)
                        print(f'|{'Masukkan bilangan bulat positif!':^{105}}|' + f'\n|{'Batas Ore dan Iron yang dapat diberikan adalah 1000!':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    murid['iron'] += int(iron)
                    murid['ore'] += int(ore)
                    print(f'|{'Ore dan Iron berhasil diberikan':^{105}}|')
                    print(tengah)
                    reset = input('|Enter untuk kembali ke menu ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                    print(tengah)
                    sleep(1)
                    continue

                elif pilihan == '6':
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'Anda memutuskan keluar':^{105}}|')
                    print(panjang)
                    reset = input('|Enter untuk kembali ke menu ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                    print(tengah)
                    sleep(1)
                    break

                else:
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'PILIHAN TIDAK TERSEDIA!':^{105}}|')
                    print(tengah)
                    print(panjang)
                    print(f'|{'Pilih antara  | 1 | 2 | 3 | 4 | 5 | 6 |!':^{105}}|')
                    print(panjang)
                    reset = input('|Enter untuk kembali ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ...{reset:<{82}}|')
                    print(tengah)
                    sleep(1)
                    continue

        else:
            os.system('cls || clear')
            print(atas)
            print(panjang)
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(tengah)
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':^{105}}|')
            print(panjang)
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            sleep(1)
            continue

    elif answer == '2':
        os.system('cls || clear')
        print(atas)
        print(f'{panjang}')
        print(f'|{'GERBANG MASUK MURID':^{105}}|')
        print(tengah)
        print(panjang)
        uns = input('|Username anda: ').lower()
        print('\033[F', end='')   
        print(f'|Username anda: {uns:<{90}}|')
        pws = input('|Password anda: ').lower()
        print('\033[F', end='')   
        print(f'|Password anda: {pws:<{90}}|')
        print(tengah)
        sleep(1)

        if uns in data_murid and data_murid[uns]["password"] == pws:
            murid = data_murid[uns]
            while True:
                os.system('cls || clear')
                print(atas)
                print(panjang)
                print(f'|{'SELAMAT DATANG MURID ' + uns.upper() :^{105}}|' + f'\n|{'Apa yang ingin kau lakukan?':^{105}}|')
                print(tengah)
                print(f'|{'IRON: ' + str(murid['iron']) + ' | ORE: ' + str(murid['ore']):<{105}}|')
                print(tengah)
                print(f'|{'1. Membuat Senjata':<{105}}|' + f'\n|{'2. Menempa Senjata':<{105}}|' + f'\n|{'3. Melihat Daftar Senjata':<{105}}|' + f'\n|{'4. Nilai':<{105}}|' + f'\n|{'5. Keluar':<{105}}|')

                print(panjang)
                pilihan = input('|Tentukan pilihan (1|2|3|4|5): ').strip()
                print('\033[F', end='')   
                print(f'|Tentukan pilihan (1|2|3|4|5): {pilihan:<{75}}|')
                print(tengah)
                sleep(1)

                if pilihan == '1':
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'Blacksmith’s Table':^{105}}|')
                    print(tengah)
                    print(panjang)

                    if murid['iron'] < 50 or murid['ore'] < 50:
                        print(f'|{'Bahan tidak cukup untuk membuat senjata! (Butuh 50 Iron & 50 Ore)':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        nama = input('|Masukkan nama senjata: ').title()
                        print('\033[F', end='')   
                        print(f'|Masukkan nama senjata : {nama:<{81}}|')

                        if nama.strip() == '' or len(nama) > 70:
                            print(tengah)
                            print(panjang)
                            print(f'|{'PENAMBAHAN ATRIBUT GAGAL!':^{105}}|')
                            print(tengah)
                            print(panjang)
                            print(f'|{'Nama tidak boleh kosong atau melebihi 70 karakter!':^{105}}|')
                            print(panjang)
                            reset = input('|Enter untuk mengulang ...')
                            print('\033[F', end='')   
                            print(f'|Enter untuk mengulang ...{reset:^{80}}|')
                            print(tengah)
                            sleep(1)
                            continue

                        else:
                            senjata_murid = murid["senjata"]
                            next_id_senjata_m = max(senjata_murid.keys()) + 1 if senjata_murid else 1
                            senjata_murid[next_id_senjata_m] = {
                                'nama': nama,
                                'atk': 1,
                                'aspd': 1,
                                'crit': 1
                            }
                            murid['iron'] -= 50
                            murid['ore'] -= 50
                            print(panjang)
                            print(f'|{'Senjata berhasil dibuat!':^{105}}|')
                            print(f'|{f'{nama} | ATK: {senjata_murid[next_id_senjata_m]['atk']} | ASPD: {senjata_murid[next_id_senjata_m]['aspd']} | CRIT: {senjata_murid[next_id_senjata_m]['crit']}%':^{105}}|')
                            print(f'|{'Sisa bahan - Iron: ' + str(murid["iron"]) + ' | Ore: ' + str(murid["ore"]):^{105}}|')
                            print(tengah)
                            reset = input('|Enter untuk kembali ke menu ...')
                            print('\033[F', end='')   
                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                            print(tengah)
                            sleep(1)
                            continue

                elif pilihan == '2':
                    os.system('cls || clear')
                    if len(murid["senjata"]) == 0:
                        print(atas)
                        print(panjang)
                        print(f'|{'Belum ada senjata untuk ditempa!':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    
                    else:
                        print(atas)
                        print(panjang)
                        print(f'|{'Blacksmith Table':^{105}}|')
                        print(tengah)
                        for i, (id, s) in enumerate(murid["senjata"].items(), start=1):
                            print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
                        print(panjang)

                        pilih_t = input('|Masukkan nomor senjata yang ingin ditempa: ').strip()
                        print('\033[F', end='')   
                        print(f'|Masukkan nomor senjata yang ingin ditempa: {pilih_t:<{62}}|')
                        print(tengah)

                        if not pilih_t.isdigit() or int(pilih_t) <= 0 or int(pilih_t) > len(murid["senjata"]):
                            print(panjang)
                            print(f'|{'Pilihan tidak tersedia!':^{105}}|')
                            print(tengah)
                            reset = input('|Enter untuk kembali ke menu ...')
                            print('\033[F', end='')   
                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                            print(tengah)
                            sleep(1)
                            continue

                        else:
                            pilih_t = int(pilih_t)
                            print(panjang)
                            print(f'|{'1. Tempa ATK':<{105}}|' + f'\n|{'2. Tempa ASPD':<{105}}|' + f'\n|{'3. Tempa %CRIT':<{105}}|' + f'\n|{'4. Ubah Nama Senjata':<{105}}|')
                            print(panjang)
                            pilih_attr = input('|Atribut yang ingin ditempa (1|2|3|4): ').strip()
                            print('\033[F', end='')   
                            print(f'|Atribut yang ingin ditempa (1|2|3|4): {pilih_attr:<{67}}|')
                            print(tengah)

                            if pilih_attr not in ['1','2','3','4']:
                                print(panjang)
                                print(f'|{'Pilihan tidak tersedia!':<{105}}|')
                                print(tengah)
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                            elif pilih_attr == '4':
                                if murid["iron"] < 100 or murid["ore"] < 100:
                                    print(panjang)
                                    print(f'|{'Bahan tidak cukup untuk mengubah nama! (Butuh 100 Iron & 100 Ore)':^{105}}|')
                                    print(tengah)
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                                print(panjang)
                                nama_baru = input('|Masukkan nama baru senjata: ').title()
                                print('\033[F', end='')   
                                print(f'|Masukkan nama baru senjata: {nama_baru:<{77}}|')
                                print(panjang)

                                if nama_baru.strip() == '' or len(nama_baru) > 70:
                                    print(tengah)
                                    print(panjang)
                                    print(f'|{'GAGAL MENGUBAH NAMA!':^{105}}|')
                                    print(tengah)
                                    print(panjang)
                                    print(f'|{'Nama tidak boleh kosong dan tidak boleh melebihi 70 karakter!':^{105}}|')
                                    print(panjang)
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                                else:
                                    lama = murid["senjata"][pilih_t]['nama']
                                    murid["senjata"][pilih_t]['nama'] = nama_baru
                                    murid["iron"] -= 100
                                    murid["ore"] -= 100
                                    print(f'|{f'{lama} telah diubah menjadi {nama_baru}':^{105}}|')
                                    print(f'|{'Sisa bahan - Iron: ' + str(murid["iron"]) + ' | Ore: ' + str(murid["ore"]):^{105}}|')
                                    print(tengah)
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                            else:
                                if murid["ore"] < 50 or murid["iron"] < 50:
                                    print(panjang)
                                    print(f'|{'Bahan tidak cukup! (Butuh 50 Iron & 50 Ore)':<{105}}|')
                                    print(tengah)
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                                else:
                                    roll = randint(1,100)
                                    if roll <= 20:
                                        nilai = choice([9, 10])
                                    elif roll <= 40:
                                        nilai = choice([7, 8])
                                    elif roll <= 60:
                                        nilai = choice([5, 6])
                                    elif roll <= 80:
                                        nilai = choice([3, 4])
                                    else:
                                        nilai = choice([1, 2])

                                    teks = "Mulai menempa"
                                    print(f"|{teks:^{105}}|", end='', flush=True)
                                    for i in range(3):
                                        sleep(1.5)
                                        print('\b ', end='', flush=True)
                                        print('\r' + f"|{teks + '.' * (i + 1):^{105}}|", end='', flush=True)
                                    sleep(1)
                                    print(f'\n{panjang}')                         
                                    pilih_t = int(pilih_t)
                                    murid["ore"] -= 50
                                    murid["iron"] -= 50
                                    if pilih_attr == '1':
                                        murid["senjata"][pilih_t]['atk'] += nilai
                                        print(f'|{f'ATK bertambah +{nilai}! Sekarang {murid["senjata"][pilih_t]['atk']}':^{105}}|')
                                    elif pilih_attr == '2':
                                        murid["senjata"][pilih_t]['aspd'] += nilai
                                        print(f'|{f'ASPD bertambah +{nilai}! Sekarang {murid["senjata"][pilih_t]['aspd']}':^{105}}|')
                                    else:
                                        crit_baru = murid["senjata"][pilih_t]['crit'] + nilai
                                        if crit_baru > 100:
                                            crit_baru = 100
                                        murid["senjata"][pilih_t]['crit'] = crit_baru
                                        print(f'|{f'CRIT bertambah +{nilai}! Sekarang {murid["senjata"][pilih_t]['crit']}%':<{105}}|')

                                    print(f'|{'Sisa bahan - Iron: ' + str(murid['iron']) + ' | Ore: ' + str(murid['ore']):^{105}}|')
                                    print(tengah)
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                elif pilihan == '3':
                    os.system('cls || clear')
                    if len(murid["senjata"]) == 0:
                        print(atas)
                        print(panjang)
                        print(f'|{'Belum ada senjata yang dibuat!':^{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        print(atas)
                        print(panjang)
                        print(f'|{'DAFTAR SENJATA MURID':^{105}}|')
                        print(tengah)
                        for i, (id, s) in enumerate(murid["senjata"].items(), start=1):
                            print(f'|{f'{i}. {s['nama']} | ATK: {s['atk']} | ASPD: {s['aspd']} | CRIT: {s['crit']}%':<{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilihan == '4':
                    os.system('cls || clear')
                    if murid['nilai'] in huruf_dict:
                        print()
                        print(atas)
                        print(panjang)
                        print(f"|{'NILAI':^{105}}|")
                        print(tengah)
                        print(panjang)
                        for baris in huruf_dict[murid['nilai']]:
                            print(f"|{baris:^105}|")
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu utama ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu utama ...{reset:<{68}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    else:
                        print(atas)
                        print(panjang)
                        print(f'|{'NILAI':^{105}}|')
                        print(tengah)
                        print(panjang)
                        print(f'|{'Nilai belum diberikan':^{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk input kembali ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk input kembali ...{reset:<{76}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    
                elif pilihan == '5':
                    os.system('cls || clear')
                    print(atas)
                    print(panjang)
                    print(f'|{'ANDA KELUAR DARI BENGKEL MURID':^{105}}|')
                    print(tengah)
                    reset = input('|Enter untuk kembali ke menu utama ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu utama ...{reset:<{68}}|')
                    print(tengah)
                    sleep(1)
                    break
                else:
                    os.system('cls || clear')
                    print(panjang)
                    print(f'|{'PILIHAN TIDAK TERSEDIA!':^{105}}|')
                    print(tengah)
                    print(panjang)
                    print(f'|{'Pilih antara  | 1 | 2 | 3 | 4 | 5 |!':^{105}}|')
                    print(panjang)
                    reset = input('|Enter untuk input kembali ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk input kembali ...{reset:<{76}}|')
                    print(tengah)
                    sleep(1)
                    continue

        else:
            os.system('cls || clear')
            print(atas)
            print(panjang)
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(tengah)
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':^{105}}|')
            print(panjang)
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            sleep(1)
            continue

    elif answer == '3':
        os.system('cls || clear')
        print(atas)
        print(f'{panjang}')
        print(f'|{'GERBANG PENDAFTARAN MURID':^{105}}|')
        print(tengah)
        print(panjang)
        uns = input('|Buat username anda: ').lower()
        print('\033[F', end='')   
        print(f'|Buat username anda: {uns:<{85}}|')
        pws = input('|Buat password anda: ').lower()
        print('\033[F', end='')   
        print(f'|Buat username anda: {pws:<{85}}|')
        print(tengah)

        if uns.strip() == '' or pws.strip() == '' or uns == pws or len(uns) > 70 or len(pws) > 12 or ' ' in pws: 
            os.system('cls || clear')
            print(atas)
            print(panjang)
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(tengah)
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':^{105}}|' + f'\n|{'Username atau Password tidak boleh kosong atau sama!':^{105}}|' + f'\n|{'Password tidak boleh ada spasi!':^{105}}|')
            print(panjang)
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            sleep(1)
            continue

        else:
            print(panjang)
            print(f'|{'PENDAFTARAN BERHASIL':^{105}}|')
            print(tengah)
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            data_murid[uns] = {
                "password": pws,
                "iron": 1000,
                "ore": 1000,
                "senjata": {},
                'nilai' : ''
            }
            sleep(2)
            continue

    elif answer == '4':
        os.system('cls || clear')
        print(atas)
        print(panjang)
        print(f'|{'GOODBYE MY FRIEND':^{105}}|')
        print(panjang)
        print(f'|{'Remember, the finest steel is born from the fiercest fire.':^{105}}|')
        print(f'|{'If the world starts to burn you, it only means you’re being forged into something stronger.':^{105}}|')
        print(f'|{'Now go… and forge your own fate.':^{105}}|')
        print(panjang)
        print(tengah)
        break

    else:
        os.system('cls || clear')
        print(atas)
        print(panjang)
        print(f'|{'PILIHAN TIDAK TERSEDIA!':^{105}}|')
        print(tengah)
        print(panjang)
        print(f'|{'Pilih antara  | 1 | 2 | 3 | 4 |!':^{105}}|')
        print(panjang)
        reset = input('|Enter untuk kembali ...')
        print('\033[F', end='')   
        print(f'|Enter untuk kembali ...{reset:<{82}}|')
        print(tengah)
        sleep(1)
        continue