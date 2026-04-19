def cek_anagram(kata1, kata2):
    kata1 = kata1.lower()
    kata2 = kata2.lower()

    # Jika panjang kata tidak sama, bukan anagram
    if len(kata1) != len(kata2):
        return False

    # Jika hasil urutan hurufnya sama, maka  anagram
    return sorted(kata1) == sorted(kata2)

kata_a = input("Masukkan kata pertama: ")
kata_b = input("Masukkan kata kedua: ")

if cek_anagram(kata_a, kata_b):
    print(f"{kata_a} anagram dengan {kata_b}")
else:
    print(f"{kata_a} BUKAN anagram dengan {kata_b}")
