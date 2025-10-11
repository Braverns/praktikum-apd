print(f'{'_'*19}')
print(f'|{' '*17}|')
print('|  HALAMAN LOGIN  |')
print(f'|{'_'*17}|\n')

username = 'Muja'
password = '059'
keluar = False

a_pos = 0
a_neg = 0
b_pos = 0
b_neg = 0
ab_pos = 0
ab_neg = 0
o_pos = 0
o_neg = 0

while True:
    u = input('Masukkan Username: ').strip().capitalize()
    p = input('Masukkan Password: ').strip()

    if u == username and p == password:
        print(f'\nLogin berhasil, selamat datang baginda {u}')
        break

    elif u != username and p != password:
        print('Username dan Password salah!\n')

    elif u != username:
        print('Username salah!\n')

    else:
        print('Password salah!\n')

while True:
    print(f'\n{'_'*31}')
    print(f'|{' '*29}|')
    print('|  SEDOT DARAH DENIS (* 3 *)  |')
    print(f'|{'_'*29}|')
    golongan = input('Masukkan golongan darah (A/B/AB/O): ').upper().strip()
    
    if golongan != 'A' and golongan != 'B' and golongan != 'AB' and golongan != 'O':
        print('\nDarah jenis baru? NO NO NO YA\n')
        continue
    else:
        print('_'*85)
        print('|Faktor Rhesus(Rh) ini merupakan protein turunan yang ditemukan pada permukan darah!|')
        print('|Jika darah mengandung protein, berarti denis Rh positif!                           |')
        print('|Sementara jika darah kekurangan protein, maka kandungan Rh negatif!                |')
        print(f'|{'_'*83}|')

        rhesus = input('\nMasukkan Faktor Rhesus (+ atau -): ').strip()
        kantong = input('Masukkan jumlah kantong darah(bilangan bulat positif): ').strip()
    
        if kantong == '0':
            print('Masukkan angka bulat lebih dari 0!\n')
            continue
        elif not kantong.isdigit() or rhesus != '+' and rhesus != '-':
            print('Input anda salah! Ikuti intruksi!\n')
            continue

        elif golongan == 'A':
            kantong = int(kantong)

            if rhesus == '+':
                a_pos += kantong * 500
                print(f'Darah A+ sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')

            else:
                a_neg += kantong * 500
                print(f'Darah A- sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')

        elif golongan == 'B':
            kantong = int(kantong)

            if rhesus == '+':
                b_pos += kantong * 500
                print(f'darah B+ sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')
            else:
                b_neg += kantong * 500
                print(f'darah B- sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')

        elif golongan == 'AB':
            kantong = int(kantong)

            if rhesus == '+':
                ab_pos += kantong * 500
                print(f'darah AB+ sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')
            else:
                ab_neg += kantong * 500
                print(f'darah AB- sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')

        else:
            kantong = int(kantong)

            if rhesus == '+':
                o_pos += kantong * 500
                print(f'darah O+ sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')
            else:
                o_neg += kantong * 500
                print(f'darah O- sebanyak {kantong} kantong ({kantong*500} ml) disimpan!')

    while True:
        ulang = input('\nApakah ingin input lagi? (Y/T): ').upper().strip()
        if ulang == 'T':
            keluar = True
            break
        elif ulang == 'Y':
            break
        else:
            print('Inputan anda salah! harus Y atau T!\n')

    if keluar == True:
        break
    else:
        continue

total_ml = a_pos + a_neg + b_pos + b_neg + ab_pos + ab_neg + o_pos + o_neg
total_kantong = total_ml // 500

ringkasan = f'|TOTAL: {total_kantong} kantong ({total_ml} ml)|'
total = len(ringkasan)

print(f'_{'_'*total}_')
print(f'|{f'RINGKASAN TOTAL DARAH DENIS':<{total}}|')
print(f'|{'_' * total}|')
print(f"|{f'Golongan A+ : {a_pos} ml':<{total}}|")
print(f'|{f'Golongan A- : {a_neg} ml':<{total}}|')
print(f'|{f'Golongan B+ : {b_pos} ml':<{total}}|')
print(f'|{f'Golongan B- : {b_neg} ml':<{total}}|')
print(f'|{f'Golongan AB+: {ab_pos} ml':<{total}}|')
print(f'|{f'Golongan AB-: {ab_neg} ml':<{total}}|')
print(f'|{f'Golongan O+ : {o_pos} ml':<{total}}|')
print(f'|{f'Golongan O- : {o_neg} ml':<{total}}|')
print(f'|{'_'*total}|')
print(f'|{f'TOTAL: {total_kantong} kantong ({total_ml} ml)':<{total}}|')
print(f'|{'_' * total}|')
