def hitung_rata_rata():
    daftar_angka = [] 

    while True:
        input_user = input("Masukkan angka (atau ketik 'done' untuk selesai): ")

        if input_user.lower() == 'done': #cek jika ingin berhenti
            break

        try:
            angka = float(input_user)
            daftar_angka.append(angka)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka atau 'done'.")

    if len(daftar_angka) > 0:
        total = sum(daftar_angka)
        jumlah_data = len(daftar_angka)
        rata_rata = total / jumlah_data
        
        print(f"\nTotal bilangan: {daftar_angka}")
        print(f"Rata-rata: {rata_rata}")
    else:
        print("Tidak ada angka yang dimasukkan.")

hitung_rata_rata()
