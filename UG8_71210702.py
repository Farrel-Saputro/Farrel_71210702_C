class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru 

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        self._data = []
        self._cap = Kasir.DEFAULT_CAPACITY
       
    def __len__(self): #mengembalikan ukuran Queue
        return len(self._data)

    def is_empty(self): #mengecek apakah Queue kosong ?
        return len(self._data) == 0

    def dequeue(self): #menghapus data paling depan (front)
        data = self._data[0]
        self._data.remove(data)
        print(f"### Pelanggan {data} Selesai Membayar ### \n")
        return data

    def enqueue(self, namaPelanggan): #menambah data ke list
        self._data.append(namaPelanggan)

    def resize(self, cap): #mengubah ukuran queue pada list
        print(f"### Melakukan Resize ### \n")
        self._cap = self._cap * cap 
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        if len (self._data) > self._cap:
            self.resize(2)
        print("=== Kasir ===")
        p = len(self._data)-1
        n = 1
        for i in range(0, (self._cap)):
            if i <= p:
                print(f"{n}. {self._data[i]}")
            else:
                print(f"{n}. kosong")
            n+=1
        print()

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

