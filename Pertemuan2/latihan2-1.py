#RUMUS BMI
#bmi = berat / tinggi**2

tinggi = float(input('masukkan tinggi badan (dalam meter): '))
bmi = float(input('masukkan nilai BMI yang diinginkan: '))

#menghitung berat
berat = bmi * (tinggi **2)
print("berat badan yang diperlukan yaitu %.2f kg" % berat)
