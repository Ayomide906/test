def swap_elements(a,b,arr):
    posit_1=0
    posit_2=0
    for i in range(len(arr)):
        if arr[i]==a:
            posit_1=i
        elif arr[i]==b:
            posit_2=i
        arr[posit_1]=b
        arr[posit_2]=a
def swap(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]
def partition(elements,start,end):
    pivot_index=end
    pivot=elements[pivot_index]
    p_index=0
    p_element=elements[p_index]
    for k in range(start,end) :
        while p_element < pivot :
            p_index += 1
            p_element=elements[p_index]
        counter = p_index
        counter_element = elements[counter]
        while counter_element > pivot:
            counter +=1
            counter_element=elements[counter]
        swap(p_index,counter,elements)
        p_element=elements[p_index] #updates the p_element
        pivot=elements[pivot_index] #updates the pivot



def quick_sort_lomuto(elements,start,end):
    if len(elements)==1:
        return elements
    if start <end: #prevents the code from running if start==end
        partition(elements, start, end)
        quick_sort_lomuto(elements,start,end-1)
if __name__=='__main__':
    elements=['MTE/2021/1025','MTE/2021/1011','MTE/2021/1078','MTE/2022/1092','MTE/2021/1001']
    quick_sort_lomuto(elements,0,len(elements)-1)
    print(elements)