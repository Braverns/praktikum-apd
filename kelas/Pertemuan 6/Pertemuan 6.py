s = {'nasi', 'goreng', 'ayam'}
s.add('rica')
for i  in s:
    print(f'makanan saya adalah {i}')
o = [1,2]
op = s.discard('apa')
print(op)
a = {6,5,4,1,8}
b = {1,3,2,9,5, 'a'}
c = {7,8,9,4,2}

Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Instagram" : "daffahrhap"}
}

print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Social Media']['Instagram']}")
print(f"nama saya adalah {Biodata.get("Nama")}")
print(Biodata.get('Nama'))

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,

"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}
# Tanpa menggunakan items()
for i in Nilai:
    print(i)
print("") # pemisah
# Menggunakan items()
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Musik = {
"The Chainsmoker" : ["All we Know", "The Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    for song in j:
        print(f"Musik milik {i} adalah : {song} ")
print("")