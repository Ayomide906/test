import time
start=time.time()
def binary_search_recursive(number,target_number,min_index,max_index):
    middle_index = (max_index + min_index) // 2
    if max_index<min_index or middle_index<0:
        return None
    if middle_index>=len(number):
        return None

    if number[middle_index]==target_number:
        return middle_index
    if target_number>number[middle_index]:
        min_index=middle_index+1
    else:
        max_index = middle_index-1
    return binary_search_recursive(number,target_number,min_index,max_index)
end=time.time()
def binary_search_multiple(number_list,needed_num):
    max_index=len(number_list)
    min_index=0
    index=binary_search_recursive(number_list,needed_num,min_index,max_index)
    indices=[index]
    prev=index-1
    while prev>=0:
        if number_list[prev]==needed_num:
            indices.append(prev)
        else:
            break
        prev-=1
    forw=index+1
    while forw<len(number_list):
        if number_list[forw]==needed_num:
            indices.append(forw)
        else:
            break
        forw+=1
    indices.sort()
    return indices

run_time=(end-start)*1000
numbers=[1,4,6,9,11,15,15,15,17,21,34,34,56]
gh=binary_search_multiple(numbers,15)
print(gh)