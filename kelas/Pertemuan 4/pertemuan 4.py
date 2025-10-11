for i in range(10):
    print(f'Perulangan ke {i}')
# f string, fungsi baguslah pokonya

for ulang in range(23):
    print(f'* yang ke {ulang}')

op = ['Meyshaa', 23, 4.00, True]
for i in op:
    print(i)
# perulangan terbatas
# tidak bisa kasih kondisi khusus

for i in range(5):
    print('*', end='')

for i in range(5):
    for j in range(i + 1):
        print(i, end='')
    print('')
for i in range(0, 4):
    for j in range(0, 5):
        print(f'{i} x {j} = {i * j} |', end='')
    print('') 

laporan = [
    200000, 100000, 300000
    -200000, -100000, -300000
]

pengeluaran, pemasukan = 0, 0
for dana in laporan:
    if dana > 0:
        pemasukan += dana
    else:
        pengeluaran += dana
pengeluaran *= -1
print(f'{pengeluaran:,}'.replace(',', '.'))
print(f'{pemasukan:,}'.replace(',', '.'))

i = 1
while i < 10:
    print(f'Bunuh {i} orang')
    i += 1

name = input('Masukkan nama anda: ')
while name == '':
    name = input('Masukkan nama anda: ')

print(name)

jawab = 'ya'
hitung = 0
while jawab == 'ya':
    hitung += 1
    jawab = input('Masukkan jawaban anda: ').lower()
print(f'Perulangan ke {hitung}')

angka = [2, 5, 7, 10, 12]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n % 2 == 0:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        continue
print("Program selesai.")


while True:
    nama = input('Masukkan nama: ')
    if nama == 'Mahdi':
        print('Sepuh OSN Matematika')
        break
print('Program selesai')
    