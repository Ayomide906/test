class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent= None
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level =0
        """initialise the present instance parent"""
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level

    def print_tree(self):
        space=" " * self.get_level()* 3
        prefix= space + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def build_product_tree():
    root=TreeNode("Electronics")
    laptop=TreeNode("laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cell_phone=TreeNode("CellPhones")
    root.add_child(cell_phone)
    cell_phone.add_child(TreeNode("iPhone"))
    cell_phone.add_child(TreeNode("vivo"))
    cell_phone.add_child(TreeNode("Google Pixel"))

    tv=TreeNode("TV")
    root.add_child(tv)
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    return root
if __name__=='__main__':
    root=build_product_tree()
    root.print_tree()