print("Binary Tree just like Decision Tree")


# you cant add duplicates in the BST
# Three tupes of BST are there : 1. In order Traversal- # 1st look at left then middle and then right
#                                2. Pre Order - Middle left and then right
#                                3. Post order - left right and middle

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:  # add data in left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:  # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:  # Value Might be in left sub tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        min = self.in_order_traversal()[0]
        return min

    def find_max(self):
        max = self.in_order_traversal()[-1]
        return max

    def cal_sum(self):
        sum = 0
        ele = self.in_order_traversal()
        for i in range(len(ele)):
            sum += ele[i]
        return sum

    def pre_order(self):
        elements = []
        # Visit base node first
        elements.append(self.data)

        if self.left:
            elements = elements + self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        return  elements

    def post_order(self):
        elements = []
        if self.left:
            elements = elements + self.left.pre_order()

        if self.right:
            elements += self.right.pre_order()

        elements.append(self.data)

        return  elements

    def in_order_traversal(self):  # 1st look at left then middle and then right
        elements = []
        # Visit left tree
        if self.left:
            elements = elements + self.left.in_order_traversal()

        # In middle Visit the base Node
        elements.append(self.data)

        # VIsit Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 18, 4, 34])
    print(numbers_tree)
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print("Pre-order traversal gives this sorted list:",numbers_tree.pre_order())
    print("Post-order traversal gives this sorted list:",numbers_tree.post_order())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.cal_sum())
