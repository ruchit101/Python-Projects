print("General Tree Learning today is 29 January.")


# Begin
class Treenode:
    def __init__(self, data, desg):
        self.data = data
        self.desg = desg
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '|__'*self.get_level()*1
        print(spaces + self.data + "(" +self.desg+")")
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_desg(self):
        spaces = '|__'*self.get_level()*1
        print(spaces + self.desg)
        if self.children:
            for child in self.children:
                child.print_tree_desg()
    def print_tree_name(self):
        spaces = '|__'*self.get_level()*1
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print_tree_name()
def management_tree():
    root = Treenode("Nilupul","CEO")
    emp1 = Treenode("Chinmay", "CTO")
    emp2 = Treenode("Vishwa", "Infra Head")
    emp3 = Treenode("Dhaval", "Cloud Manager")
    emp4 = Treenode("Abhijit", "App Manager")
    emp5 = Treenode("Aamir","Application Head")
    emp6 = Treenode("Gels", "HR Head")
    emp7 = Treenode("Gels", "Recruitment Manager")
    emp8 = Treenode("Waqas","Policy Manager")

    root.add_child(emp1)
    emp1.add_child(emp2)
    emp2.add_child(emp3)
    emp2.add_child(emp4)
    emp1.add_child(emp5)
    root.add_child(emp6)
    emp6.add_child(emp7)
    emp6.add_child(emp8)

    #print(cell.get_level())
    return root


if __name__ == '__main__':
    root = management_tree()
    root.print_tree()
    print("___________________________________________________________________________")
    root.print_tree_name()
    print("___________________________________________________________________________")
    root.print_tree_desg()

    pass
