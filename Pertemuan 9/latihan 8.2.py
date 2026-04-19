import re

def hitung_frekuensi(kalimat, kata_dicari):
    kalimat_lower = kalimat.lower()
    kata_lower = kata_dicari.lower()
    
    pola = r'\b' + re.escape(kata_lower) + r'\b'
    
    # findall mengembalikan semua string yang sesuai pola dalam bentuk list
    kemunculan = re.findall(pola, kalimat_lower)
    
    return len(kemunculan)

teks = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
target = "makan"

hasil = hitung_frekuensi(teks, target)
print(f"{target} ada {hasil} buah")
