class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def build_food_menu_tree():
    root = TreeNode("Food Menu")

    appetizers = TreeNode("Appetizers")
    appetizers.add_child(TreeNode("Spring Rolls"))
    appetizers.add_child(TreeNode("Garlic Bread"))
    appetizers.add_child(TreeNode("Bruschetta"))

    main_course = TreeNode("Main Course")
    italian = TreeNode("Italian")
    italian.add_child(TreeNode("Lasagna"))
    italian.add_child(TreeNode("Spaghetti"))
    italian.add_child(TreeNode("Ravioli"))

    indian = TreeNode("Indian")
    indian.add_child(TreeNode("Butter Chicken"))
    indian.add_child(TreeNode("Palak Paneer"))
    indian.add_child(TreeNode("Biryani"))

    main_course.add_child(italian)
    main_course.add_child(indian)

    desserts = TreeNode("Desserts")
    desserts.add_child(TreeNode("Ice Cream"))
    desserts.add_child(TreeNode("Chocolate Cake"))
    desserts.add_child(TreeNode("Cheesecake"))

    root.add_child(appetizers)
    root.add_child(main_course)
    root.add_child(desserts)

    root.print_tree()


build_food_menu_tree()