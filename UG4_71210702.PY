import json

with open('mahasiswa.json', 'r') as file:
    mahasiswa = json.load(file)
    inputan = int(input('Masukan jumlah mahasiswa baru : '))
    for i in range(inputan):
        mahasiswa = input("Masukan nama Anda : ")
        hobi = int(input("Masukan Jumlah hobi : "))
        for j in range(hobi):
            input_hobi = input(f"Masukan Hobi ke-{j+1} : ")
        prestasi = input("Masukan pretasi Anda : ")
        print(f"=== Data berhasil ditambahkan ===\n")

with open('masasiswa.json', 'a') as file:
    json.dump(mahasiswa, file)

