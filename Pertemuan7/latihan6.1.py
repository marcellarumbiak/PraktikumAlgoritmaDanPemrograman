n = int(input("Masukkan nilai n: "))

for i in range(n-1, 1, -1):
    prima = True
    for j in range(2, i):
        if i % j == 0:
            prima = False
            break
    if prima:
        print("Bilangan prima terdekat dari n adalah:", i)
        break
