import re
import random
import string

def proses_email_dan_password(teks):
    # Regex untuk mencari email: [a-zA-Z0-9._%+-]+@ [a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
    # 1: ([a-zA-Z0-9._%+-]+) adalah bagian sebelum tanda @
    pola_email = r'([a-zA-Z0-9._%+-]+)@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # finditer digunakan untuk mendapatkan teks email lengkap dan username
    matches = re.finditer(pola_email, teks)
    
    print("Hasil:")
    for match in matches:
        email_lengkap = match.group(0) # Mengambil seluruh email
        username = match.group(1)      # Mengambil hanya bagian username 
        
        # Menghasilkan password random 8 karakter (huruf dan angka) 
        karakter = string.ascii_letters + string.digits
        password = ''.join(random.choice(karakter) for _ in range(8))
        
        print(f"{email_lengkap} username: {username} , password: {password}")

# Contoh input 
input_teks = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

proses_email_dan_password(input_teks)
