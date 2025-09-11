class HashTable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        sum=0
        for char in key:
            sum+=ord(char)
        return sum % self.MAX
    def __setitem__(self,key,value):
        sum=self.get_hash(key)
        found=False
        """check the index and element in that hashTable to see if smth is there already"""
        for idx,element in enumerate(self.arr[sum],0):
            """the next code checks if the element contains two items and if the first item is the key entered"""
            if len(element) ==2 and element[0]==key:
                """if true the next code reassign the key to the entered value"""
                self.arr[sum][idx] =(key, value)
                found=True
                break
                """if not found then input the item into the hashTable as a tuple"""
        if not found:
            self.arr[sum].append((key,value))
    def __getitem__(self,key):
        sum=self.get_hash(key)
        if self.arr[sum] is None:
            raise Exception('No value for: ',key)
        """to iterate through hashTable"""
        for idx,element in enumerate(self.arr[sum]):
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        sum=self.get_hash(key)
        for index,element in enumerate(self.arr[sum]):
            if element[0]==key:
                del self.arr[sum][index]
t=HashTable()
no_month=int(input("Enter the no of months needed: "))
for i in range(no_month):
    real_key = input("Enter the month and day: ")
    cost_value = int(input("Enter the cost for the month: "))
    t[real_key]=cost_value
print(t.arr)
p=t.get_hash('march 17')
print(p)
u=t['march 11']
del t['march 11']
t.__setitem__("march 11",5000)
print(u)
print(t.arr)