class HashTable:
    def __init__(self):
        self.MAX=20
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        sum=0
        for char in key:
            sum+=ord(char)
        return sum % self.MAX
    def __setitem__(self,key,value):
        sum=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[sum]):
            if len(element)==2 and element[0]==key:
                self.arr[sum][idx]=(key,value)
                found=True
                return
        """i.e if true"""
        if not found:
            self.arr[sum].append((key,value))
    def Average_temp(self):
        total=0
        average=0
        count=0
        for i in range(self.MAX):
            for idx, element in enumerate(self.arr[i]):
                if None:
                    continue
                total += element[1]
                count+=1
                average = total / count
        return average
    def max_temp(self):
        for i in range(self.MAX):
            previous_element=0
            for idx, element in enumerate(self.arr[i]):

                if None:
                    continue
                if element[1]> previous_element:
                    return element[0],element[1]
                previous_element=element[1]
t=HashTable()
no_month=int(input("Enter the no of months needed: "))
for i in range(no_month):
    real_key = input("Enter the month and day: ")
    cost_value=int(input("Enter the temp for the month: "))
    t[real_key]=cost_value
print(t.arr)
y=t.Average_temp()
k,p=t.max_temp()
print("Average temperature is :",y)
print(f"The maximum month is {k} :Temp({p})")
