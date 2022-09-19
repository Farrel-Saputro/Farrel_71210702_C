import json

with open('mahasiswa.json', 'r') as file:
    mahasiswa = json.load(file)

    inputan = int(input('Masukan jumlah mahasiswa baru : '))

    for i in range(0, inputan):
        nama = input("Masukan nama Anda : ")
        listkosong = []
        kosong = {}
        hobi = int(input("Masukan Jumlah hobi : "))
        listhobi = []
        for j in range(1, hobi+1):
            input_hobi = input("Masukan Hobi ke-{index} : ".format(index=j))
            listhobi.append(input_hobi)

        prestasi = input("Masukan pretasi Anda : ")
        
        listkosong.append({'Biodata' : {'Hobi' : listhobi, 'Prestasi' : prestasi}})
        mahasiswa[nama] = listkosong

        print(f"=== Data berhasil ditambahkan ===\n")
        print()

with open('mahasiswa.json', 'w') as file:
    json.dump(mahasiswa, file)

