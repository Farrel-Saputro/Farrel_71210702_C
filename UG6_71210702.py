class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self, no_rek, nama, saldo=0):
        self.no_rekening = no_rek
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def insert_head(self,no_rekening, nama, saldo):
        baru = NodeTabungan(no_rekening, nama, saldo)
        if self._head == None:
            self._head = baru
            self._tail = baru
        else:
            baru.next = self._head
            self._head = baru
        self._size += 1

    def delete_head(self):
        if self._size == 0:
            return False
        elif self._size == 1:
            helper = self.head
            self.head = None
            self.tail = None
            del helper
            self._size = self._size - 1
            return True
        else:
            helper = self.head
            self.head = self.head.next
            del helper
            self._size = self._size - 1
            return True

    def delete_tail(self):
        if self._size == 0:
            return False
        elif self._size == 1:
            delete = self.tail
            self.tail = None
            self.head = None
            del delete
            self._size = self._size - 1
        else:
            helper = self.head
            while helper.next != self.tail:
                helper = helper.next
            delete = self.tail
            self.tail = helper
            self.tail.next = None
            del delete
            self._size = self._size - 1

    def delete(self, position):
        if self._size == 0:
            return False
        elif position == 0:
            self.delete_head()
        elif position + 1 >= self._size:
            self.delete_tail()
        else:
            delete_node = self.head
            for i in range(position):
                delete_node = delete_node.next
            helper = self.head
            while helper.next != delete_node:
                helper = helper.next
            helper.next = delete_node.next
            del delete_node
            self._size = self._size - 1

    def print(self):
        bantu = self._head
        while bantu != None:
            print(f'Norek: {bantu.no_rekening}')
            print(f'Nama: {bantu.nama}')
            print(f'Saldo: {bantu.saldo}')
            bantu = bantu.next
        print()

    def filter(self, batas):
        bantu = self._head
        while bantu != None:
            jumlah = 0
            if bantu.saldo < batas:
                jumlah += 1 
                del bantu
            bantu = bantu.next
        print(f"Rekening yang berhasil di hapus sebanyak: {jumlah} buah")
        
slnc = SLNC()
slnc.insert_head(201, "Hanif", 250000)
slnc.insert_head(101, "Yudha", 150000)
slnc.print()
slnc.filter(100)
slnc.update(200)
slnc.update(50)
slnc.print()

