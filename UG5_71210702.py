class Mobil:
    _merk = ''
    _tipe = ''
    _jenisBahanBakar = None
    _kapasitasBBM = None

    def __init__(self,merk,tipe):
        self._merk = merk
        self._tipe = tipe
    
    def setkapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def setjenisBahanBakar(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar

    def getmerk(self):
        return self._merk

    def gettipe(self):
        return self._tipe

    def getkapasitasBBM(self):
        return self._kapasitasBBM

    def getjenisBahanBakar(self):
        return self._jenisBahanBakar

    def printInfo(self):
        print(f"{12*'='} INFO {12*'='}")
        print(f"Merk            : {self.getmerk()}")
        print(f"Tipe            : {self.gettipe()}")
        print(f"Bahan Bakar     : {self.getjenisBahanBakar()}")
        print(f"Kapasitas BBM   : {self.getkapasitasBBM()}")
  
    def isiBBM(self,harga):
        if self.getjenisBahanBakar() is None and self.getkapasitasBBM() is None:
            print(f"Error! Kapasitas BBM atau Jenis Bahan Bakar belum di inputkan")
        else:
            print(f"Mengisi {self.getkapasitasBBM()} Liter")
            print(f"Total Harga : Rp{self.getkapasitasBBM() * harga}")

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setjenisBahanBakar("Bensin")
    mobil2.setkapasitasBBM(20)
    mobil2.printInfo()
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)
