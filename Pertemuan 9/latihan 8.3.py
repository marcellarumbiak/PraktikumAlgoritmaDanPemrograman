def bersihkan_spasi_standar(kalimat):
    # split() tanpa parameter memecah string berdasarkan semua whitespace 
    kata_kata = kalimat.split()
    
    # join() menggabungkan kembali list kata dengan satu spasi 
    return " ".join(kata_kata)

# Contoh penggunaan
input_teks = "saya    tidak   suka  memancing    ikan   "
output = bersihkan_spasi_standar(input_teks)
print(f"Output: '{output}'")
