celsius = [27, 33, 46, 55, 67, 92]  

suhu1_fahrenheit = (9/5) * celsius[0] + 32
suhu2_fahrenheit = (9/5) * celsius[1] + 32

suhu3_kelvin = celsius[2] + 273.15
suhu4_kelvin = celsius[3] + 273.15

suhu5_reamur = (4/5) * celsius[4] 
suhu6_reamur = (4/5) * celsius[5] 
jumlah = suhu1_fahrenheit + suhu2_fahrenheit + suhu3_kelvin + suhu4_kelvin + suhu5_reamur + suhu6_reamur
rata2 = jumlah / len(celsius)   

NIM = 59

Bolean = NIM < rata2

print(f'list suhu : {celsius}')
print(f'27°C ke Fahrenheit : {suhu1_fahrenheit}')
print(f'33°C ke Fahrenheit : {suhu2_fahrenheit}')
print(f'46°C ke Kelvin : {suhu3_kelvin}')
print(f'55°C ke Kelvin : {suhu4_kelvin}')
print(f'67°C ke Reamur : {suhu5_reamur}')
print(f'92°C ke Reamur : {suhu6_reamur}')
print(f'Jumlah : {jumlah}')
print(f'Rata-rata : {rata2}')
print(f'NIM : {NIM}')
print(f'Bolean : {Bolean}') 
print(f'Slice negatif : {celsius[-4:]}')
