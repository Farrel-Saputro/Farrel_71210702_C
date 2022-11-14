def mergesort(data): # data = list
    if len(data) > 1:
        # cari titik tengahnya
        mid = len(data) // 2
        # berasarkan mid, bagi data menjadi dua bagian
        # pada python bisa menggunakan slicing
        left = data[:mid]
        right = data[mid:]

        # bagi lagi sampai bagian terkecil secara rekursif
        mergesort(left)
        mergesort(right)

        # merge kiri dan kanan sehingga hasilnya terurut
        # i => untuk index potongan kiri, j => untuk index potongan kanan
        i = 0
        j = 0
        # k => untuk index list hasil penggabungan kiri dan kanan
        k = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        # jika salah satu sudah habis, sisanya tinggal dimasukkan ke list hasil
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k]= right[j]
            j += 1
            k += 1

        return data

lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]
print(mergesort(lst1))
print(mergesort(lst2))
print(mergesort(lst3))
