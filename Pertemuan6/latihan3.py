def hitung_IPS(jumlah_mk):
    sks = 3
    total_bobot = 0
    total_sks = 0

    for i in range(1, jumlah_mk + 1):
        nilai = input('Nilai Mata Kuliah ' + str(i) + ': ').upper()
        
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B': 
            bobot = 3 
        elif nilai == "C":
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            bobot = 0
            
        total_bobot = total_bobot + (bobot * sks)
        total_sks = total_sks + sks
        
    ips = total_bobot / total_sks
    return ips

jumlah_mk = int(input('Berapa jumlah mata kuliah? ')) 
hasil_ips = hitung_IPS(jumlah_mk)
print('Nilai IPS anda', round(hasil_ips, 2))
