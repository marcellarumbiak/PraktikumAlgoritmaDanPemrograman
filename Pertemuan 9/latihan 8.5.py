import re
from datetime import datetime

def olah_tanggal(teks):
    # Pola Regex untuk YYYY-MM-DD
    # \d{4} = 4 digit tahun, \d{2} = 2 digit bulan/hari
    pola_tgl = r'(\d{4})-(\d{2})-(\d{2})' 
    
    # Mencari semua kecocokan dalam teks
    semua_tanggal = re.findall(pola_tgl, teks)
    
    # Tanggal sekarang (asumsi mengikuti waktu real-time)
    sekarang = datetime.now()
    
    for tgl in semua_tanggal:
        tahun, bulan, hari = tgl
        
        # Menyusun string tanggal 
        tgl_str = f"{tahun}-{bulan}-{hari}"
        obj_tgl = datetime.strptime(tgl_str, "%Y-%m-%d")
        
        # Menghitung selisih hari
        selisih = (sekarang - obj_tgl).days
        
        # Format output sesuai permintaan: DD-MM-YYYY dan selisih hari
        print(f"{hari}-{bulan}-{tahun} 00:00:00 selisih {abs(selisih)} hari")

# Contoh input
input_teks = ("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, "
              "seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan "
              "Ki Hajar Dewantara (1889-05-02).") 

print("Hasil:")
olah_tanggal(input_teks)
