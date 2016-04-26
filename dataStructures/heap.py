class MaxHeap:

    def __init__(self):
        self.keys = []
    

    def insert(self, i):
        self.keys.append(i)
        self.perc_up(len(self.keys)-1)

    def find_max(self):
        return self.keys[0]

    
    def del_max(self):
        self.keys[0] = self.keys[len(self.keys) - 1]
        self.keys.pop()
        self.perc_down(0)

        
    def is_empty(self):
        if not self.keys:
            return true
        else:
            return false

    
    def size(self):
        return len(self.keys)


    def build_heap(self, arr):
        self.keys = arr
        i = len(arr) // 2
        while (i >= 0):
            self.perc_down(i)
            i -= 1


    def perc_down(self, ind):
        while((ind*2) + 1 < len(self.keys)):
            mc = self.get_max_child(ind)
            if (self.keys[ind] < self.keys[mc]):
                tmp = self.keys[ind]
                self.keys[ind] = self.keys[mc]
                self.keys[mc] = tmp
            ind = mc

    
    def perc_up(self, ind):
        while ((ind-1)//2 >= 0):
            if (self.keys[ind] > self.keys[(ind-1)//2]):
                tmp = self.keys[ind]
                self.keys[ind] = self.keys[(ind-1)//2]
                self.keys[(ind-1)//2] = tmp
            ind = (ind-1)//2


    def get_max_child(self, ind):
        if (ind*2 + 2 > len(self.keys) - 1): 
            # has only one child
            return ind*2 + 1
        else:
            # has two children
            if (self.keys[ind*2 + 1] > self.keys[ind*2 + 2]):
                return ind*2 + 1
            else:
                return ind*2 + 2


