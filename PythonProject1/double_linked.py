class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        self.prev=None
class double_linkedList:
    def __init__(self):
        self.head=None
    def print_forward(self,data_list):
        self.head=None
        for data in data_list:
            if self.head is None:
                self.head = Node(data,self.next)
                continue
            """initialize the current node"""
            current = self.head
            """iterate until the next node is None"""
            while current.next is not None:
                current = current.next
            """once the next node is none the loop will be exited and a new node will be created"""
            current.next = Node(data,None)
    def print_backward(self,data):
        self.head=None
        for datas in data:
            node = Node(datas,self.head)
            self.head = node
    def display(self):
        if self.head is None:
            print("Linked list is empty")
            return
        curr_node=self.head
        llstr=[]
        while curr_node is not None :
            llstr.append(curr_node.data +"----->")
            curr_node=curr_node.next
        print(llstr)
    def get_length(self):
        curr_node=self.head
        count=0
        while curr_node is not None:
            count+=1
            curr_node = curr_node.next
        return count
    def get_index(self,index):
        if index < 0 or index > self.get_length():
            raise Exception ("invalid Index")
        elif index==0:
            return self.head.data
        curr=self.head
        count=0
        while curr:
            if count==index:
                return curr.data
            curr=curr.next
            count+=1
        curr_node=self.head
    def delete_by_value(self,data):
        if self.head is None:
            raise Exception ("linked list is empty")
        """to check if value given is the first node"""
        if self.head.data==data:
            self.head=self.head.next
            return
        curr=self.head
        while curr.next:
            if curr.next.data==data:
                curr.next=curr.next.next
                break
            curr=curr.next
    def Enter_list(self,len_list):
        full_list=[]
        for i in range(len_list):
            list_item=input("Enter the item: ")
            full_list.append(list_item)
        return full_list
    def delete_by_index(self,index):
        if index <0 or index> self.get_length():
            raise Exception("invalid index")
        elif index==0:
            self.head=self.head.next
            return
        curr=self.head
        count=0
        while curr:
            if count==index-1:
                curr.next=curr.next.next
            curr=curr.next
            count+=1


ll=double_linkedList()
len_list=int(input("Enter the length of the list: "))
Full_list=ll.Enter_list(len_list)
ll.print_backward(Full_list)
length=ll.get_length()
print(length)
f=ll.get_index(2)
print(f)
ll.delete_by_index(2)
ll.display()