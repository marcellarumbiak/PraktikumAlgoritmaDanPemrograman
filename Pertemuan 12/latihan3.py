# dictionary kosong untuk menyimpan histogram
counts = dict()

fname = input('Masukkan nama file: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    #jika file tidak ditemukan
    print('File tidak bisa dibuka:', fname)
    exit()

for line in fhand:
    # Memecah baris menjadi daftar kata
    words = line.split()   
    # Mencari baris yang diawali dengan 'From' dan memiliki minimal 2 kata
    if len(words) < 2 or words[0] != 'From':
        continue
    
    # Alamat email berada di indeks ke-1
    email = words[1]  
    # Menghitung frekuensi email menggunakan metode get()
    # Jika email belum ada, beri nilai default 0 lalu tambah 1
    counts[email] = counts.get(email, 0) + 1

print(counts)
