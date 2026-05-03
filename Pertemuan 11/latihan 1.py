def bilangan_terbaik(data):
    unik = list(set(data))
    
    unik.sort(reverse=True)
    
    return unik[:3]

angka = [10, 5, 8, 20, 20, 4, 15, 30]
hasil = bilangan_terbaik(angka)
print("3 Bilangan terbaik adalah:", hasil) 
