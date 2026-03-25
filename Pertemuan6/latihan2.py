def ganjil (bawah, atas): 
    if bawah < atas:
        for i in range(bawah + 1, atas):
            if i % 2 != 0:
                print(i, end = ',')
        for i in range(bawah, atas, - 1): 
            if i % 2 != 0:
                print(i, end = ',')

bawah = int(input('masukkan batas bawah: ')) 
atas = int(input('masukkan batas atas: ')) 
ganjil (bawah, atas)
