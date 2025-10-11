angka = int(input('Masukkan angka: '))

if angka < 6 and angka > 3:
    print('angka ini lebih kecil dari 5')
    if angka == 3:
        print('angka ini adalah 3')
    elif angka == 4:
        print('angka ini adalah 4')
        if angka == 2:
            print('Angka ini adalah 2')
        else:
            print('angka ini bukan 2')

elif angka > 6 and angka < 10:
    print('angka ini lebih besar dari 6 dan lebih kecil dari 10')

else:
    print('angka ini adalah 6 atau lebih besar')

if angka > 2:
    print('Angka ini lebih besar dari 2')

nilai = int(input('Nilai: '))

if nilai > 80 and nilai <= 100:
    print('A+')
elif 80 <= nilai > 70:
    print('B')
else:
    print('C')

nilai = 70
masuk = 'lulus' if nilai > 60 else 'Tidak lulus'
print(masuk)

usia = 30
hasil = 'Jompo' if usia > 30 else 'Dewasa atau orang tua'
print(hasil)

a = 10
b = 6

if a >= 10:
    if b > 5:
        print(a + b) 

elif a <= 10:
    if b > 6:
        print(a - b) 

else:
    print('ga tau bang')
    
