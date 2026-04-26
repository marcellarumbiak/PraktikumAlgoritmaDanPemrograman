def jalankan_kuis(nama_file):
    try:
        handle = open(nama_file)
        
        print(f"nama file1: {nama_file}")
        
        for line in handle:
            # Membersihkan spasi atau newline di awal/akhir baris
            line = line.strip()
            # Melewati baris jika kosong
            if not line:
                continue
            # Memisahkan soal dan jawaban berdasarkan pemisah "  "
            if "  " in line:
                bagian = line.split(" || ")
                pertanyaan = bagian[0]
                jawaban_benar = bagian[1].strip()
                
                # Menampilkan pertanyaan ke pengguna
                print(pertanyaan)
                
                # Meminta input jawaban dari pengguna
                jawaban_user = input("Jawab: ")
                
                if jawaban_user.lower() == jawaban_benar.lower():
                    print("Jawaban benar!")
                else:
                    print("Jawaban salah!")
                    
        handle.close()
        
    except FileNotFoundError:
        print("File tidak ditemukan!")


jalankan_kuis("mbox.txt")
