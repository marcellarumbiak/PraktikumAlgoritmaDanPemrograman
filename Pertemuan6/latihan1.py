def perkalian (pengali, angka):
    hasil = 0
    deret = [ ]
    for i in range(pengali):
        hasil = hasil + angka
        deret.append(str(angka))
    format_deret = '+' . join(deret)
    print(pengali, 'x', angka, '=',format_deret, '=', hasil)


pengali = int(input('Masukkan bilangan (pengali): ')) 
angka = int(input('Masukkan bilangan yang ingin dikalikan: '))
perkalian (pengali, angka)
