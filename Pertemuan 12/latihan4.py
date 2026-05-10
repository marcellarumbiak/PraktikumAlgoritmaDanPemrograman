# dictionary kosong untuk menyimpan hitungan domain
domain_counts = dict()

fname = input('Masukkan nama file: ')

try:
    fhand = open(fname)
except FileNotFoundError:
    print('File tidak dapat dibuka:', fname)
    exit()

for line in fhand:
    words = line.split()
    
    # Mencari baris yang diawali dengan 'From' (bukan 'From:')
    if len(words) < 2 or words[0] != 'From':
        continue
    
    # Ambil alamat email 
    email = words[1]
    # Memisahkan email berdasarkan tanda '@' 
    # email.split('@') menghasilkan list ['nama_user', 'domain.com']
    parts = email.split('@')
    domain = parts[1]
    
    # Menghitung jumlah domain menggunakan get()
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

print(domain_counts)
