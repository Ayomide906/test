import insertion_sort as it
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge_two_sorted_lists(left,right)
def merge_sort_by_key(elements,key,descending=True):
    i=0
    arr=[]
    if key=='age':
        for item in elements:
            for ky, val in item.items():
                if ky == 'age':
                    arr.append(val)
        it.insertion_sort(arr)
    elif key=='name':
        for item in elements:
            for ky, val in item.items():
                if ky == 'name':
                    arr.append(val)
        it.insertion_sort(arr)
    elif key=='time_hours'and descending==True:
        for item in elements:
            for ky, val in item.items():
                if ky == 'time_hours':
                    arr.append(val)
        it.insertion_sort(arr)
        arr=arr[::-1]
    auth_element=[]
    for items in arr:
         for i in range(len(elements)):
             if elements[i][key]==items:
                 auth_element.append(elements[i])


    return auth_element

def merge_two_sorted_lists(a,b):
    sorted_list=[]
    len_a=len(a)
    len_b=len(b)
    i=j=0
    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1
    while i<len_a:
        #once b exited the first loop this will continue and append the rest since its sorted already
        sorted_list.append(a[i])
        i+=1
    while j<len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list
if __name__=='__main__':
    arr=[1]
    elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
    key=(input("the key item you want to sort:  ")).lower()
    print(merge_sort_by_key(elements,key,True))
    #done jorrrrr