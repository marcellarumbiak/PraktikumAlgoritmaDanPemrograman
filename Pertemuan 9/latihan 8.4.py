def cari_kata_ekstrim(kalimat):
    # Memecah kalimat menjadi list kata-kata berdasarkan spasi dan Menghapus spasi berlebih
    daftar_kata = kalimat.split()
    
    # Jika kalimat kosong, kembalikan pesan peringatan
    if not daftar_kata:
        return None, None


    terpendek = daftar_kata[0]
    terpanjang = daftar_kata[0]


    for kata in daftar_kata:
        kata_bersih = "".join([char for char in kata if char.isalnum()])
        
        if len(kata_bersih) > 0:
            # Update jika ditemukan kata yang lebih panjang
            if len(kata_bersih) > len(terpanjang):
                terpanjang = kata_bersih
            # Update jika ditemukan kata yang lebih pendek
            if len(kata_bersih) < len(terpendek):
                terpendek = kata_bersih

    return terpendek, terpanjang


input_user = "red snakes and a black frog in the pool"
pendek, panjang = cari_kata_ekstrim(input_user)

print(f"Kalimat: {input_user}")
print(f"Terpendek: {pendek}")
print(f"Terpanjang: {panjang}")
