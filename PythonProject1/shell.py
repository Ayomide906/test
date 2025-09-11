import insertion_sort as it
def shell_sort(arr,gap):
    size = len(arr)
    if gap==1:
        return it.insertion_sort(arr)
    for i in range(gap,size):
        anchor=arr[i]
        j = i
        while j>=gap and  arr[j-gap] > anchor:
            arr[j] = arr[j-gap]
            j-=gap
        arr[j]= anchor
        return shell_sort(arr,gap-1)
if __name__ =='__main__':
    elements= [21,100,56,75,90,10,23,4555,8798,0,19,10,655]
    gap=len(elements)//2
    shell_sort(elements,gap)
    print(elements)