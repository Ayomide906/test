class BinarySearchTreeNode:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left is not None:
                self.left.add_child(data)
            else:
                #create a new node at the left of the current self.data
                self.left=BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elements=[]
        #visit left then base then right
        if self.left:
            elements+=self.left.in_order_traversal() #this code will add previous elements to incoming one
        #visit base node
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    def search(self,data):
        if self.data==data: #checks the current node
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False
        if data > self.data:
            if self.right:
                return self.right.search(data)
            else:
                return False
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    def delete(self,val):
        if val< self.data:
            if self.left:
                self.left=self.left.delete(val)
            else:
                return None
        elif val> self.data:
            if self.right:
                self.right=self.right.delete(val) #goes to the right node and recursively calls delete function
            else:
                return None
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self
    def calculate_sum(self):
        my_list=self.in_order_traversal()
        sum=0
        for i in range(len(my_list)):
            sum+=my_list[i]
        return sum
    def post_order_traversal(self):
        element=[]
        #checks left node
        if self.left:
            element+=self.left.post_order_traversal()
        #checks right node
        if self.right:
            element+=self.right.post_order_traversal()
        #checks base
        element.append(self.data)
        return element
    def pre_order_traversal(self):
        element=[]
        element.append(self.data)
        if self.left:
            element+=self.left.pre_order_traversal()
        if self.right:
            element+=self.right.pre_order_traversal()
        return element
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
tt=BinarySearchTreeNode(57)
tt.add_child(43)
tt.add_child(34)

print(tt.in_order_traversal())
if __name__ =='__main__':
    numbers=[10,5,67,89,15,19,39,280]
    numbers_tree=build_tree(numbers)
    #since we already returned root as numbers_tree
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
    numbers_tree.delete(39)
    print(numbers_tree.in_order_traversal())
