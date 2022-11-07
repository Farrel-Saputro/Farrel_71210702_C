class Node:
    def __init__(self, data, priority):
        self._data = data
        self._priority = priority
    
class PriorityQueueSortedList:
    def __init__(self):
        self._data = []
        self.size = 0

    def peek(self):
        if self.size != 0:
            x = 9999
            data = ''
            ind = 0
            for i in range(len(self._data)):
                if self._data[i][1] > x:
                    pass
                else:
                    x = self._data[i][1]
                    data = self._data[i][0]
                    ind = i
            print(f"Data prioritas tertinggi: ('{data}', {x})")
        else:
            print("Priority Queue is Empty!")

    def add(self, data, priority):
        self._data.append((data, priority))
        self._data=sorted(self._data, key=lambda x:x[1])
        self.size += 1

    def update(self, prioBaru, dataBaru):
        if self.size != 0:
            ind = []
            for i in range(len(self._data)):
                if self._data[i][1] == prioBaru:
                    self._data[i] = (dataBaru, prioBaru)
        else:
            print("Priority Queue is Empty!")

    def remove(self):
        if self.size != 0:
            x = 9999 
            index = 0
            data = 0
            for i in range(len(self._data)):
                if self._data[i][1] > x: 
                    pass
                else:
                    x = self._data[i][1] 
                    index = i
                    data += 1
            del self._data[index]
        else:
            print("Priority Queue is Empty!")
        self.size -= 1

    def removePriority(self, priority):
        if self.size != 0:
            ind = []
            for i in range(len(self._data)):
                if self._data[i][1] == priority:
                    ind.append(self._data[i])
            for i in ind:
                self._data.remove(i)
        else:
            print("Priority Queue is Empty!")
        self.size -= 1

    def printIsiQueue(self):
        print("Isi Semua Queue:", end=' ')
        for i in range(len(self._data)):
            print(self._data[i], end=' ')
        print()

sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printIsiQueue()
