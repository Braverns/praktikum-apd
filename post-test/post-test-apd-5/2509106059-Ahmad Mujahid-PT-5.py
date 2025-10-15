import os
from random import randint
from time import sleep


senjata = []
akun = []
senjata_m = []

panjang = f'|{' '*105}|'
tengah =  f'|{'_'*105}|'
atas = f'{'_'*107}'
keluar = False

iron = 1000
ore = 1000


while True:
    os.system('cls')
    print(atas)
    print(panjang)
    print(f'|{'THE BLACKSMITH':^{105}}|')
    print(tengah)
    print(f'|{'Through fire and hammer, the blacksmith shapes the world.':^{105}}|' + f'\n|{'Are You One Of Us?':^{105}}|')
    print(f'|{'1. Master':<{105}}|' + f'\n|{'2. Murid':<{105}}|' + f'\n|{'3. Daftar Sebagai Murid':<{105}}|' + f'\n|{'4. Keluar':<{105}}|')

    choice = input('|Ingin masuk sebagai apa, tentukan pilihan (1|2|3|4): ').strip()
    print('\033[F', end='')   
    print(f'|Ingin masuk sebagai apa, tentukan pilihan (1|2|3|4): {choice:<{52}}|')
    print(tengah)   
    

    if choice == '1':      
        print(panjang)
        print(f'|{'GERBANG MASUK MASTER':^{105}}|')
        print(tengah)
        un = input('|Username anda: ').strip().lower().replace(' ', '')
        print('\033[F', end='')   
        print(f'|Username anda: {un:<{90}}|')
        pw = input('|Password anda: ').strip().lower().replace(' ', '')
        print('\033[F', end='')   
        print(f'|Password anda: {pw:<{90}}|')
        print(tengah)
        sleep(1)

        if un == 'master' and pw == 'master123':
            while True:
                os.system('cls')
                print(atas)
                print(panjang)
                print(f'|{'SELAMAT DATANG MASTER':^{105}}|')
                print(f'|{'APA YANG INGIN ANDA LAKUKAN?':^{105}}|')
                print(tengah)
                print(f'|{'1. Membuat dan Menempa Senjata':<{105}}|' + f'\n|{'2. Daftar Senjata':<{105}}|' + f'\n|{'3. Memodifikasi Senjata':<{105}}|' + 
                      f'\n|{'4. Hancurkan Senjata':<{105}}|' + f'\n|{'5. Keluar':<{105}}|')
                pilihan = input('|Tentukan pilihan (1|2|3|4|5): ').strip()
                print('\033[F', end='')   
                print(f'|Tentukan pilihan (1|2|3|4|5): {pilihan:<{75}}|')
                print(tengah)

                if pilihan == '1':
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

                    if not atk.isdigit() or not aspd.isdigit() or not crit.isdigit() or int(crit) > 100 or nama == '':
                        print(tengah)
                        print(f'|{'PENAMBAHAN ATRIBUT GAGAL!':^{105}}|')
                        print(panjang)
                        print(f'|{'Atribut harus berupa angka bulat positif & Batas crit 100%!':<{105}}|')
                        reset = input('|Enter untuk login ulang ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk login ulang ...{reset:<{78}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    else:
                        senjata.append([nama, atk, aspd, crit])
                        print(panjang)
                        print(f'|{'Senjata berhasil dibuat!!':<{105}}|')
                        print(f'|{f'{nama} | ATK: {atk} | ASPD: {aspd} | CRIT: {crit}%':<{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilihan == '2':
                    if len(senjata) == 0:
                        print(f'|{'Belum ada senjata':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    else:
                        print(f'|{'DAFTAR SENJATA':^{105}}|')
                        print(panjang)
                        for i in range(len(senjata)):
                            s = senjata[i]
                            print(f'|{f'{i+1}. {s[0]} | ATK: {s[1]} | ASPD: {s[2]} | CRIT: {s[3]}%':<{105}}|')
                        print(panjang)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                elif pilihan == '3':
                    if len(senjata) == 0:
                        print(f'|{'Belum ada senjata':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    else:
                            os.system('cls')
                            print(atas)
                            print(panjang)
                            print(f'|{'DAFTAR SENJATA':^{105}}|')
                            print(panjang)
                            print(tengah)

                            for i in range(len(senjata)):
                                s = senjata[i]
                                print(f'|{f'{i+1}. {s[0]} | ATK: {s[1]} | ASPD: {s[2]} | CRIT: {s[3]}%':<{105}}|')
                            print(panjang)
                            
                            ubah = input('|Masukkan nomor senjata yang ingin diubah: ').strip()
                            print('\033[F', end='')   
                            print(f'|Masukkan nomor senjata yang ingin diubah: {ubah:<{63}}|')        
                            
                            if not ubah.isdigit() or int(ubah) <= 0 or int(ubah) > len(senjata):
                                print(panjang)
                                print(f'|{'Pilihan tidak tersedia':<{105}}|')
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                            else:
                                ubah = int(ubah) - 1
                                print(f'|{'1. Ubah nama':<{105}}|' + f'\n|{'2. Ubah ATK':<{105}}|' + f'\n|{'3. Ubah ASPD':<{105}}|' + f'\n|{'4. Ubah %CRIT':<{105}}|')
                                print(panjang)

                                ubah2 = input('|Apa yang ingin diubah (1|2|3|4): ').strip()
                                print('\033[F', end='')   
                                print(f'|Apa yang ingin diubah (1|2|3|4): {ubah2:<{72}}|')

                                if ubah2 not in ['1','2','3','4']:
                                    print(f'|{'Pilihan tidak tersedia':<{105}}|')
                                    reset = input('|Enter untuk kembali ke menu ...')
                                    print('\033[F', end='')   
                                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                    print(tengah)
                                    sleep(1)
                                    continue

                                else:
                                    if ubah2 == '1':
                                        print(panjang)
                                        nama_baru = input('|Nama baru: ').title()
                                        print('\033[F', end='')   
                                        print(f'|Nama baru: {nama_baru:<{94}}|')
                                        senjata[ubah][0] = nama_baru
                                        print(f'|{f'{nama} telah diubah menjadi {nama_baru}':<{105}}|')
                                        print(panjang)

                                        reset = input('|Enter untuk kembali ke menu ...')
                                        print('\033[F', end='')   
                                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                        print(tengah)
                                        sleep(1)
                                        continue

                                    elif ubah2 == '2':
                                        print(panjang)
                                        nilai = input('|Masukkan nilai baru ATK: ').strip()
                                        print('\033[F', end='')   
                                        print(f'|Masukkan nilai baru ATK: {nilai:<{80}}|')
                                        print(panjang)
                                    

                                        if not nilai.isdigit():
                                            print(tengah)
                                            print(f'|{'GAGAL MENGUBAH ATK!':^{105}}|')
                                            print(panjang)
                                            print(f'|{'Atribut harus berupa angka bulat positif!':<{105}}|')

                                            reset = input('|Enter untuk kembali ke menu ...')
                                            print('\033[F', end='')   
                                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                            print(tengah)
                                            sleep(1)
                                            continue

                                        else:
                                           senjata[ubah][1] = nilai
                                           print(f'|{f'ATK : {atk} telah diubah menjadi {nilai}':<{105}}|')

                                           reset = input('|Enter untuk kembali ke menu ...')
                                           print('\033[F', end='')   
                                           print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                           print(tengah)
                                           sleep(1)
                                           continue              

                                    elif ubah2 == '3':
                                        print(panjang)
                                        nilai = input('|Masukkan nilai baru ASPD: ').strip()
                                        print('\033[F', end='')   
                                        print(f'|Masukkan nilai baru ASPD: {nilai:<{80}}|')
                                        print(panjang)

                                        if not nilai.isdigit():
                                            print(tengah)
                                            print(f'|{'GAGAL MENGUBAH ASPD!':^{105}}|')
                                            print(panjang)
                                            print(f'|{'Atribut harus berupa angka bulat positif!':<{105}}|')
                                            reset = input('|Enter untuk kembali ke menu ...')
                                            print('\033[F', end='')   
                                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                            print(tengah)
                                            sleep(1)
                                            continue

                                        else:
                                           senjata[ubah][2] = nilai
                                           print(f'|{f'ASPD : {aspd} telah diubah menjadi {nilai}':<{105}}|')

                                           reset = input('|Enter untuk kembali ke menu ...')
                                           print('\033[F', end='')   
                                           print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                           print(tengah)
                                           sleep(1)
                                           continue 
                                        
                                    else:
                                        print(panjang)
                                        nilai = input('|Masukkan nilai baru CRIT: ').strip()
                                        print('\033[F', end='')   
                                        print(f'|Masukkan nilai baru CRIT: {nilai:<{80}}|')
                                        print(panjang)

                                        if not nilai.isdigit():
                                            print(tengah)
                                            print(f'|{'GAGAL MENGUBAH CRIT!':^{105}}|')
                                            print(panjang)
                                            print(f'|{'Atribut harus berupa angka bulat positif!':<{105}}|')
                                            reset = input('|Enter untuk kembali ke menu ...')
                                            print('\033[F', end='')   
                                            print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                            print(tengah)
                                            sleep(1)
                                            continue

                                        else:
                                           senjata[ubah][3] = nilai
                                           print(f'|{f'CRIT : {crit} telah diubah menjadi {nilai}':<{105}}|')

                                           reset = input('|Enter untuk kembali ke menu ...')
                                           print('\033[F', end='')   
                                           print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                           print(tengah)
                                           sleep(1)
                                           continue 

                elif pilihan == '4':
                        if len(senjata) == 0:
                            if len(senjata) == 0:
                                print(f'|{'Belum ada senjata':<{105}}|')
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                        else:
                            print(panjang)
                            print(f'|{'DAFTAR SENJATA':^{105}}|')
                            print(tengah)

                            for i in range(len(senjata)):
                                s = senjata[i]
                                print(f'|{f'{i+1}. {s[0]} | ATK: {s[1]} | ASPD: {s[2]} | CRIT: {s[3]}%':<{105}}|')
                                
                            print(panjang)
                            hapus = input('|Masukkan nomor senjata yang ingin dihapus: ').strip()
                            print('\033[F', end='') 
                            print(panjang)  
                            print(f'|Masukkan nomor senjata yang ingin dihapus: {hapus:<{62}}|')

                            if not hapus.isdigit() or int(hapus) <= 0 or int(hapus) > len(hapus):
                                print(panjang)
                                print(f'|{'Pilihan tidak tersedia':<{105}}|')
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                            else:
                                hapus = int(hapus) - 1
                                print(f'|{f'Senjata {senjata[hapus][0]} telah dihancurkan.':<{105}}|')
                                senjata.pop(hapus)

                                print(panjang)
                                reset = input('|Enter untuk kembali ke menu ...')
                                print('\033[F', end='')   
                                print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                                print(tengah)
                                sleep(1)
                                continue

                else:
                    print(f'|{'Anda memutuskan keluar':<{105}}|')
                    print(panjang)
                    reset = input('|Enter untuk kembali ke menu ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                    print(tengah)
                    sleep(1)
                    break

        else:
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':<{105}}|')
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            sleep(1)
            continue

    elif choice == '2':
        print(f'{panjang}')
        print(f'|{'GERBANG MASUK MURID':^{105}}|')
        print(tengah)
        uns = input('|Username anda: ').lower()
        print('\033[F', end='')   
        print(f'|Username anda: {uns:<{90}}|')
        pws = input('|Password anda: ').lower()
        print('\033[F', end='')   
        print(f'|Password anda: {pws:<{90}}|')

        if pws in akun and uns in akun:
            kuasa = False
            print(tengah)
            print(f'|{'SELAMAT DATANG ' + uns.upper() :^{105}}|')
            print(tengah)

            while True:
                os.system('cls')
                print(atas)
                print(panjang)
                print(f'|{'BENGKEL MURID ' + uns.upper():^{105}}|')
                print(tengah)
                print(f'|{'IRON: ' + str(iron) + ' | ORE: ' + str(ore):<{105}}|')
                print(tengah)
                print(f'|{'1. Membuat Senjata':<{105}}|' + f'\n|{'2. Menempa Senjata':<{105}}|' + f'\n|{'3. Melihat Daftar Senjata':<{105}}|' + f'\n|{'4. Keluar':<{105}}|')

                pilih_m = input('|Tentukan pilihan (1|2|3|4): ').strip()
                print('\033[F', end='')   
                print(f'|Tentukan pilihan (1|2|3|4): {pilih_m:<{77}}|')
                print(tengah)

                if pilih_m == '1':
                    if iron < 50 or ore < 50:
                        print(f'|{'Bahan tidak cukup untuk membuat senjata! (Butuh 50 Iron & 50 Ore)':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    nama = input('|Masukkan nama senjata: ').title()
                    print('\033[F', end='')   
                    print(f'|Masukkan nama senjata : {nama:<{81}}|')

                    atk = input('|Masukkan ATK          : ').strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan ATK          : {atk:<{81}}|')

                    aspd = input('|Masukkan ASPD         : ').strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan ASPD         : {aspd:<{81}}|')

                    crit = input('|Masukkan %CRIT        : ').strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan %CRIT        : {crit:<{81}}|')

                    if not atk.isdigit() or not aspd.isdigit() or not crit.isdigit() or int(crit) > 100 or nama == '':
                        print(tengah)
                        print(f'|{'PENAMBAHAN ATRIBUT GAGAL!':^{105}}|')
                        print(panjang)
                        print(f'|{'Atribut harus berupa angka bulat positif & Batas crit 100%!':<{105}}|')
                        reset = input('|Enter untuk kembali ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ...{reset:<{84}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    else:
                        senjata_m.append([nama, atk, aspd, crit])
                        iron -= 50
                        ore -= 50
                        print(panjang)
                        print(f'|{'Senjata berhasil dibuat!':<{105}}|')
                        print(f'|{f'{nama} | ATK: {atk} | ASPD: {aspd} | CRIT: {crit}%':<{105}}|')
                        print(f'|{'Sisa bahan - Iron: ' + str(iron) + ' | Ore: ' + str(ore):<{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilih_m == '2':
                    if len(senjata_m) == 0:
                        print(f'|{'Belum ada senjata untuk ditempa!':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    
                    print(panjang)
                    print(f'|{'DAFTAR SENJATA':^{105}}|')
                    print(tengah)
                    for i in range(len(senjata_m)):
                        s = senjata_m[i]
                        print(f'|{f'{i+1}. {s[0]} | ATK: {s[1]} | ASPD: {s[2]} | CRIT: {s[3]}%':<{105}}|')
                    print(panjang)

                    pilih_t = input('|Masukkan nomor senjata yang ingin ditempa: ').strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan nomor senjata yang ingin ditempa: {pilih_t:<{62}}|')

                    if not pilih_t.isdigit() or int(pilih_t) <= 0 or int(pilih_t) > len(senjata_m):
                        print(panjang)
                        print(f'|{'Pilihan tidak tersedia!':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    
                    if ore < 10:
                        print(f'|{'Ore tidak cukup! (Butuh 10 Ore)':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    pilih_t = int(pilih_t) - 1
                    print(panjang)
                    print(f'|{'1. Tempa ATK':<{105}}|' + f'\n|{'2. Tempa ASPD':<{105}}|' + f'\n|{'3. Tempa %CRIT':<{105}}|')
                    print(panjang)
                    pilih_attr = input('|Atribut yang ingin ditempa (1|2|3): ').strip()
                    print('\033[F', end='')   
                    print(f'|Atribut yang ingin ditempa (1|2|3): {pilih_attr:<{69}}|')

                    if pilih_attr not in ['1','2','3']:
                        print(f'|{'Pilihan tidak tersedia!':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    nilai = input('|Masukkan nilai tambahan: ').strip()
                    print('\033[F', end='')   
                    print(f'|Masukkan nilai tambahan: {nilai:<{83}}|')

                    if not nilai.isdigit():
                        print(tengah)
                        print(f'|{'GAGAL MENEMPA SENJATA!':^{105}}|')
                        print(panjang)
                        print(f'|{'Nilai tambahan harus berupa angka bulat positif!':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                    ore -= 10
                    nilai = int(nilai)
                    if pilih_attr == '1':
                        senjata_m[pilih_t][1] = str(int(senjata_m[pilih_t][1]) + nilai)
                        print(f'|{f'ATK bertambah +{nilai}! Sekarang {senjata_m[pilih_t][1]}':<{105}}|')
                    elif pilih_attr == '2':
                        senjata_m[pilih_t][2] = str(int(senjata_m[pilih_t][2]) + nilai)
                        print(f'|{f'ASPD bertambah +{nilai}! Sekarang {senjata_m[pilih_t][2]}':<{105}}|')
                    else:
                        crit_baru = int(senjata_m[pilih_t][3]) + nilai
                        if crit_baru > 100:
                            crit_baru = 100
                        senjata_m[pilih_t][3] = str(crit_baru)
                        print(f'|{f'CRIT bertambah +{nilai}! Sekarang {senjata_m[pilih_t][3]}%':<{105}}|')

                    print(f'|{'Sisa Ore: ' + str(ore):<{105}}|')
                    print(tengah)
                    reset = input('|Enter untuk kembali ke menu ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                    print(tengah)
                    sleep(1)
                    continue

                elif pilih_m == '3':
                    if len(senjata_m) == 0:
                        print(f'|{'Belum ada senjata yang dibuat!':<{105}}|')
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue
                    else:
                        print(panjang)
                        print(f'|{'DAFTAR SENJATA MURID':^{105}}|')
                        print(panjang)
                        for i in range(len(senjata_m)):
                            s = senjata_m[i]
                            print(f'|{f'{i+1}. {s[0]} | ATK: {s[1]} | ASPD: {s[2]} | CRIT: {s[3]}%':<{105}}|')
                        print(tengah)
                        reset = input('|Enter untuk kembali ke menu ...')
                        print('\033[F', end='')   
                        print(f'|Enter untuk kembali ke menu ...{reset:<{74}}|')
                        print(tengah)
                        sleep(1)
                        continue

                elif pilih_m == '4':
                    print(panjang)
                    print(f'|{'ANDA KELUAR DARI BENGKEL MURID':^{105}}|')
                    print(tengah)
                    reset = input('|Enter untuk kembali ke menu utama ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk kembali ke menu utama ...{reset:<{66}}|')
                    print(tengah)
                    sleep(1)
                    break
                else:
                    print(f'|{'PILIHAN TIDAK TERSEDIA!':^{105}}|')
                    print(panjang)
                    print(f'|{'Pilih antara  | 1 | 2 | 3 | 4|!':<{105}}|')
                    reset = input('|Enter untuk input kembali ...')
                    print('\033[F', end='')   
                    print(f'|Enter untuk input kembali ...{reset:<{76}}|')
                    print(tengah)
                    sleep(1)
                    continue

        else:
            print(tengah)
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':<{105}}|')
            reset = input('|Enter untuk login ulang ...')
            print('\033[F', end='')   
            print(f'|Enter untuk login ulang ...{reset:<{78}}|')
            print(tengah)
            sleep(1)
            continue

    elif choice == '3':
        print(f'{panjang}')
        print(f'|{'GERBANG PENDAFTARAN MURID':^{105}}|')
        print(tengah)
        uns = input('|Buat username anda: ').lower()
        print('\033[F', end='')   
        print(f'|Buat username anda: {uns:<{85}}|')
        pws = input('|Buat password anda: ').lower()
        print('\033[F', end='')   
        print(f'|Buat username anda: {pws:<{85}}|')
        print(tengah)

        if uns.strip() == '' or pws.strip() == '' or uns == pws: 
            print(f'|{'LOGIN GAGAL!':^{105}}|')
            print(panjang)
            print(f'|{'Username dan Password anda tidak sesuai!':<{105}}|' + f'\n|{'Username dan Password tidak boleh kosong atau sama!':<{105}}|')
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
            akun.append(uns)
            akun.append(pws)
            sleep(1)
            continue

    elif choice == '4':
        print(panjang)
        print(f'|{'SAMPAI JUMPA LAGI':^{105}}|')
        print(panjang)
        print(tengah)
        break

    else:
        print(f'|{'PILIHAN TIDAK TERSEDIA!':^{105}}|')
        print(panjang)
        print(f'|{'Pilih antara  | 1 | 2 | 3 |!':<{105}}|')
        reset = input('|Enter untuk login ulang ...')
        print('\033[F', end='')   
        print(f'|Enter untuk input kembali ...{reset:<{78}}|')
        print(tengah)
        sleep(1)
        continue







