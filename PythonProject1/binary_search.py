import time
#decorator function
def time_calc(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        #the below will allow the decorator to take in the name of the function you call it with
        result =func(*args,**kwargs)
        end_time=time.time()
        print(func.__name__ +" took "+str(round((end_time-start_time)*1000,5)) +"mil sec")
        return result
    return wrapper

"""BINARY SEARCH ALGORITHM"""
if __name__=='__main__':
    @time_calc
    def SearchList(numbers, targetNumber):
        minIndex = 0
        maxIndex = len(numbers)
        while minIndex < maxIndex:
            State = ""
            if targetNumber not in numbers:
                State = "Not found in the list"
                break
            import math
            middleIndex = math.floor((minIndex + maxIndex) / 2)
            if targetNumber == numbers[middleIndex]:
                State = f"number found in index:{middleIndex}"
                break
            elif targetNumber > numbers[middleIndex]:
                minIndex = middleIndex
            elif targetNumber < numbers[middleIndex]:
                maxIndex = middleIndex
        return State


    def load_num():
        f = open("c://data//country2.txt", "r")
        numberss = []
        for line in f:
            each = line.split()
            '''THIS CODE CONVERTS A LIST OF STRINGS TO INT'''
            numberss += list(map(int, each))
        return numberss


    needed_number = load_num()
    print(needed_number)
    targetNumber = int(input("Enter the number you want to check in a list"))
    ryu = SearchList(needed_number, targetNumber)
    print(ryu)