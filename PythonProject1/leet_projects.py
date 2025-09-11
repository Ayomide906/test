def remove_repeated_items(List=[],start=0,it=0):
    if start==len(List):
        return List
    it = start + 1
    while it<len(List):
        if List[it] == List[start]:
            List.pop(it)
        it += 1
    return remove_repeated_items(List,start+1)
print(remove_repeated_items(["MTE/2021/1025","MTE/2021/1025"]))

