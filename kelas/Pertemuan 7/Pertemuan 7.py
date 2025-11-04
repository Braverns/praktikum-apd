import os

def pesan():
    print('Akademik')
    print('Indonesia')
    
panjang = f'|{' '*105}|'
tengah =  f'|{'_'*105}|'
atas = f'{'_'*107}'



os.system('cls || clear')
print(atas)
print(panjang)
print(f'|{'KALKULATOR SEDERHANA':^{105}}|')
print(f'|{'1. Kalkulator biasa':<{105}}|' + f'\n|{'2. Faktorial':<{105}}|')
print(tengah)



def operasi(op, a, b):
            if op == '+':
                hasil = a + b
                print(f'\nHasil operasi Pertambahan: {hasil}\n')
                return hasil          
            elif op == '-':
                hasil = a - b
                print(f'\nHasil operasi Pengurangan: {hasil}\n')
                return hasil
            
            elif op == '/':
                if b == 0:
                    print('\nPenyebut tidak boleh 0!\n')
                else: 
                    hasil = a / b
                    print(f'\nHasil operasi Pembagian: {hasil}\n')
                    return hasil
            else:
                hasil = a * b
                print(f'\nHasil operasi Perkalian: {hasil}\n')
                return hasil
def lanjut():
     while True:
        ok = input('\nMau lanjut (Y/N): ').upper().strip()
        if ok not in ['Y', 'N']:
            print('\nJawaban tidak valid!\n')
            continue
        elif ok == 'Y':
            break
        elif ok == 'N':
            print(f'{'Terimakasih telah menggunakan kalkulator sederhana ini\n' :^{105}}')
            exit()

def faktorial(n):
     if n == 1 or n == 0:
          return 1
     else:
          return n * faktorial(n-1)

while True:
    try:
        pilihan = int(input('\nMasukkan Nomor: '))
        if pilihan == 1:
            a = int(input('\nMasukkan angka pertama          : '))
            b = int(input('Masukkan angka kedua            : '))
            op = input('Pilih Operasi ( + | - | / | * ) : ')
            if op not in ['+', '-', '/', '*'] :
                    print('\nOperasi tidak sesuai!\n')
                    continue
            else:
                operasi(op, a, b)
                lanjut()
        elif pilihan == 2:
             try:
                a = int(input('\nMasukkan faktorial : '))
                if a > 100:
                     raise ValueError('\nAngka Tidak Boleh E')
                coma = f'{faktorial(a):,}'
                print('Hasil pemfaktoran  : ', str(coma).replace(',', "."))
                lanjut()
             except ValueError as e:
                  print(e)

        else:
             print('\nNomor tidak tersedia\n')

    except ValueError as e:
         print('Input Error: ', e)


