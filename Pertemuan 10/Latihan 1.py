def bandingkan_file(file1, file2):
    try:
        # Membuka kedua file menggunakan fungsi open()
        handle1 = open(file1)
        handle2 = open(file2)

        
        # rstrip() untuk menghapus newline agar tidak double saat dibandingkan
        lines1 = [line.rstrip() for line in handle1]
        lines2 = [line.rstrip() for line in handle2]

        # Menentukan jumlah baris maksimal di antara kedua file
        max_lines = max(len(lines1), len(lines2))
        perbedaan_ditemukan = False

        print(f"Hasil perbandingan antara '{file1}' dan '{file2}':\n")

        for i in range(max_lines):
            content1 = lines1[i] if i < len(lines1) else "[Baris Kosong/Tidak Ada]"
            content2 = lines2[i] if i < len(lines2) else "[Baris Kosong/Tidak Ada]"

            # Membandingkan setiap baris 
            if content1 != content2:
                perbedaan_ditemukan = True
                print(f"Perbedaan pada Baris {i + 1}:")
                print(f"  File 1: {content1}")
                print(f"  File 2: {content2}")
                print("-" * 20)

        if not perbedaan_ditemukan:
            print("Kedua file identik. Tidak ditemukan perbedaan.")

        # Menutup file setelah selesai digunakan
        handle1.close()
        handle2.close()

    except FileNotFoundError:
        # Menangani error jika nama file tidak ditemukan
        print("Error: Salah satu atau kedua file tidak dapat ditemukan.")

nama_f1 = input("Masukkan nama file pertama: ")
nama_f2 = input("Masukkan nama file kedua: ")

bandingkan_file(nama_f1, nama_f2)
