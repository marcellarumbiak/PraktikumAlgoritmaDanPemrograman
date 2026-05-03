def kata_unik_artikel(nama_file):
    try:
        with open(nama_file, 'r') as file:
            isi_teks = file.read()
            
            # Mengubah ke huruf kecil
            isi_teks = isi_teks.lower()
            
            # Memecah teks menjadi list kata-kata menggunakan split()
            daftar_kata = isi_teks.split()
            
            # Mencari kata unik menggunakan set(). Set menghapus duplikat
            set_kata_unik = set(daftar_kata)
            
            # Mengubah kembali ke list agar bisa diurutkan
            list_hasil = list(set_kata_unik)
            list_hasil.sort() # Mengurutkan secara ascending
            

            print(f"--- Hasil Analisis File: {nama_file} ---")
            print(f"Total kata unik ditemukan: {len(list_hasil)}") 
            print("-" * 40)
            print(list_hasil)
            
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


kata_unik_artikel('berita.txt')
