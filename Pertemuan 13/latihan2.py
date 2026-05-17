data_diri = ('Marcella Lince', '71220961', 'Klitren, Yogyakarta')

nama, nim, alamat = data_diri

print(f"Data: {data_diri}")
print(f"NIM: {nim}")
print(f"Nama: {nama}")
print(f"Alamat: {alamat}")

nim_tuple = tuple(nim)

nama_split = nama.split()
nama_depan_sisa = tuple(nama_split[0][1:])

nama_terbalik = tuple(nama_split[::-1])

print(f"NIM: {nim_tuple}")
print(f"Nama Depan: {nama_depan_sisa}")
print(f"Nama Terbalik: {nama_terbalik}")


print(f"NIM: {nim_tuple}")
print(f"Nama Depan: {nama_depan_sisa}")
print(f"Nama Terbalik: {nama_terbalik}")
