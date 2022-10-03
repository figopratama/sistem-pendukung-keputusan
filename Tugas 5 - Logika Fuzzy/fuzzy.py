
x_temp = input('Masukkan nilai suhu (F) = ')
y_humid = input('Masukkan nilai tekanan udara (P) = ')
z_velo = input('Masukkan nilai kelembapan udara (RH) = ')


temp = int(x_temp)
humid = int(y_humid)
velo = int(z_velo)



# Rumus Hitung Temperatur
if temp <= 23 :
    value_dingin = 1
    value_sedang = 0
    value_panas = 0
if temp > 23 and temp < 26 :
    value_dingin = (26 - temp)/(26 - 23)
    value_sedang = (temp - 23)/(26 - 23)
    value_panas = 0
if temp == 26 :
    value_dingin = 0
    value_sedang = 1
    value_panas = 0
if temp > 26 and temp < 40 :
    value_dingin = 0
    value_sedang = (40 - temp)/(40 - 26)
    value_panas = (temp - 26)/(40 - 26)
if temp == 40 :
    value_dingin = 0
    value_sedang = 0
    value_panas = 1

print('\n')
print('Maka temperaturnya dalam variabel linguistik, derajat keanggotaan adalah')
print('Dingin', value_dingin)
print('Sedang', value_sedang)
print('Panas', value_panas)



# Rumus Hitung Tekanan
if humid <= 80 :
    value_lembab = 1
    value_sedang = 0
    value_tidaklembab = 0
if humid > 80 and humid < 88 :
    value_lembab = (88 - humid)/(88 - 80)
    value_sedang = (humid - 80)/(88 - 80)
    value_tidaklembab = 0
if humid == 88 :
    value_lembab = 0
    value_sedang = 1
    value_tidaklembab = 0
if humid > 88 and humid < 100 :
    value_lembab = 0
    value_sedang = (100 - humid)/(100 - 88)
    value_tidaklembab = (humid - 88)/(100 - 88)
if humid == 100 :
    value_lembab = 0
    value_sedang = 0
    value_tidaklembab = 1

print('\n')
print('Maka temperaturnya dalam variabel linguistik, derajat keanggotaan adalah')
print('Lembab', value_lembab)
print('Sedang', value_sedang)
print('Tidak lembab', value_tidaklembab)



# Rumus Hitung Kelembapan
if velo <= 3 :
    value_pelan = 1
    value_sedang = 0
    value_kencang = 0
if velo > 3 and velo < 6 :
    value_pelan = (6 - velo)/(6 - 3)
    value_sedang = (velo - 3)/(6 - 3)
    value_kencang = 0
if velo == 6 :
    value_pelan = 0
    value_sedang = 1
    value_kencang = 0
if velo > 6 and velo < 15 :
    value_pelan = 0
    value_sedang = (15 - velo)/(15 - 6)
    value_kencang = (velo - 6)/(15 - 6)
if velo == 15 :
    value_pelan = 0
    value_sedang = 0
    value_kencang = 1

print('\n')
print('Maka kelembapannya dalam variabel linguistik, derajat keanggotaan adalah')
print('Pelan', value_pelan)
print('Sedang', value_sedang)
print('Kencang', value_kencang)



# Pendefinisian fungsi Cerah, Berawan, dan Hujan
weather=[]
def cerah (var_temp, var_humid, var_velo):
    if var_temp != 0:
        if var_humid != 0:
            if var_velo != 0:
                hasil_output = min(var_temp, var_humid, var_velo)
                weather.append([hasil_output, 5])

def berawan (var_temp, var_humid, var_velo):
    if var_temp != 0:
        if var_humid != 0:
            if var_velo != 0:
                hasil_output = min(var_temp, var_humid, var_velo)
                weather.append([hasil_output, 20])

def hujan (var_temp, var_humid, var_velo):
    if var_temp != 0:
        if var_humid != 0:
            if var_velo != 0:
                hasil_output = min(var_temp, var_humid, var_velo)
                weather.append([hasil_output, 50])

# Value pada Fungsi Cerah
cerah(value_panas, value_lembab, value_pelan)
cerah(value_panas, value_sedang, value_pelan)
cerah(value_panas, value_sedang, value_sedang)
cerah(value_panas, value_sedang, value_kencang)
cerah(value_panas, value_tidaklembab, value_pelan)
cerah(value_panas, value_tidaklembab, value_sedang)
cerah(value_panas, value_tidaklembab, value_kencang)
cerah(value_sedang, value_tidaklembab, value_pelan)
cerah(value_sedang, value_tidaklembab, value_sedang)

# Value pada fungsi Berawan
berawan(value_sedang, value_lembab, value_pelan)
berawan(value_panas, value_lembab, value_sedang)
berawan(value_panas, value_lembab, value_kencang)
berawan(value_sedang, value_sedang, value_pelan)
berawan(value_sedang, value_sedang, value_sedang)
berawan(value_sedang, value_sedang, value_kencang)
berawan(value_sedang, value_tidaklembab, value_kencang)
berawan(value_dingin, value_tidaklembab, value_pelan)
berawan(value_dingin, value_tidaklembab, value_sedang)

# Value pada fungsi Hujan
hujan(value_dingin, value_lembab, value_pelan)
hujan(value_dingin, value_lembab, value_sedang)
hujan(value_dingin, value_lembab, value_kencang)
hujan(value_sedang, value_lembab, value_sedang)
hujan(value_sedang, value_lembab, value_kencang)
hujan(value_dingin, value_sedang, value_pelan)
hujan(value_dingin, value_sedang, value_sedang)
hujan(value_dingin, value_sedang, value_kencang)
hujan(value_dingin, value_tidaklembab, value_kencang)

print ('Value cuaca adalah = ', weather)


# Operasi hitung value cuaca
perkalian_new = 0
pembagian_new = 0

for j in range(0, len(weather)):
    perkalian = weather[j][0] * weather[j][1]
    pembagian = weather[j][0]
    perkalian_new = perkalian_new + perkalian
    pembagian_new = pembagian_new + pembagian
z = perkalian_new / pembagian_new

# Perkiraan cuaca
if z >= 0 and z <= 5 :
    print('Perkiraan cuaca adalah cerah')
if z > 5 and z <= 20 :
    print('Perkiraan cuaca adalah mendung')
if z > 20 and z <= 50 :
    print('Perkiraan cuaca adalah hujan')    



