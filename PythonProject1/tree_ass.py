class TreeNode:
    def __init__(self,data,designation):
        self.designation=designation
        self.data=data + "  "+f"({designation})"
        self.name_data=data
        self.designation_data=designation
        self.children=[]
        self.parent=None
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
    def print_tree(self,needed):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        try:
            if needed == "name":
                print(prefix + self.name_data)
                for child in self.children:
                    child.print_tree("name")
            if needed == "designation":
                print(prefix + self.designation_data)
                for child in self.children:
                    child.print_tree("designation")
            if needed == "both":
                print( prefix + self.data)
                for child in self.children:
                    child.print_tree("both")
        except Exception as e:
            print('Exception is',type(e).__name__)

def build_hierarchy():
    root=TreeNode("Nilupul","CEO")
    cto=TreeNode("Chinmay","CTO")
    ifr_head=TreeNode("Vishwa","Infrastructure Head")
    cl_man=TreeNode("Dhaval","Cloud Manager")
    app_man=TreeNode("Abhijit","App Manager")
    appl_head=TreeNode("Aamir","Application Head")
    hr_head=TreeNode("Gels","HR Head")
    recr_man=TreeNode("Peter","Recruitment Manager")
    pol_man=TreeNode("Waqas","Policy Manager")
    root.add_child(hr_head)
    root.add_child(cto)
    cto.add_child(ifr_head)
    cto.add_child(appl_head)
    ifr_head.add_child(cl_man)
    ifr_head.add_child(app_man)
    hr_head.add_child(recr_man)
    hr_head.add_child(pol_man)
    return root
if __name__ == '__main__':
    root=build_hierarchy()
    needed=input("Enter the needed command: ")
    root.print_tree(needed)