# KONSTRUKSI DASAR PHYTON
# SEQUENSTIAL : Eksekusi berurutan
print('Hello World')
print('by annas')
print('Tanggal 22 Agustus 2024')
print('-'*10)

# PERCABANGAN : Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print("Jalan lain")

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 -1 = 4
    print(f'Halo anak #{index_anak}')