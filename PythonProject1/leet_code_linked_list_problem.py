#You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linked_List:
    def __init__(self):
        self.head=None
        self.need=[]
    def print_backwards(self,input):
        self.head=None
        for data in input:
            node=Node(data,self.head)
            self.head=node
        curr=self.head
        llstr=[]
        while curr:
            llstr.append(curr.data)
            curr=curr.next
        self.need.append(llstr)
        return self.need
    def get_sum(self):
        arr=[]
        extra=0
        i=len(self.need[0])-1
        j=len(self.need[1])-1
        while i>=0 or j>=0:
            if i<0 and j>=0:
                sum=extra+self.need[1][j]
                if sum>=10 and j==0:
                    arr.append((sum) % 10)
                    arr.append(1)
                    return arr
                elif sum>=10:
                    arr.append((sum) % 10)
                    extra=1
                else:
                    arr.append(sum+extra)
                    extra=0
            elif j<0 and i>=0:
                sum=extra+self.need[0][i]
                if sum>=10 and i==0:
                    arr.append((sum) % 10)
                    arr.append(1)
                    return arr
                elif sum >=10:
                    arr.append((sum) % 10)
                    extra=1
                else:
                    arr.append(sum+extra)
                    extra=0
            elif i==0 and j==0 and self.need[0][i]+self.need[1][j] >=10:
                sum=self.need[0][i]+self.need[1][j]
                arr.append(sum%10)
                arr.append(1)
                return arr
            else:
                sum=self.need[0][i]+self.need[1][j]
                if sum >= 10:
                            arr.append((sum+extra) % 10)
                            extra = 1
                else:
                    arr.append(sum + extra)
                    extra = 0
            i-=1
            j-=1
        return arr
if __name__=='__main__':
    data=[[9,9,9,9,9,9,9],[9,9,9,9]]
    ll = Linked_List()
    for i in range(len(data)):
        ll.print_backwards(data[i])
    print(ll.get_sum())

