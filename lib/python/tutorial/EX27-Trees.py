class Node:
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)



left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)


#27.2
def total(tree):
    if tree is None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo


#27.3
tree2 = Tree("+", Tree(1), Tree("*", Tree(2), Tree(3)))


#27.4
def print_tree(tree):  #Prefix
    if tree is None: return
    print(tree.cargo, end=" ")
    print_tree(tree.left)
    print_tree(tree.right)

print_tree(tree2)

def print_tree_postorder(tree):  #Postfix
    if tree is None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print(tree.cargo, end=" ")

def print_tree_inorder(tree):  #Infix
    if tree is None: return
    print_tree_inorder(tree.left)
    print(tree.cargo, end=" ")
    print_tree_inorder(tree.right)

def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

print_tree_indented(tree2)


#27.5
def get_token(token_list, expected):
    if token_list[0] == expected:
        del token_list[0]
        return True
    return False

def get_number(token_list):
    if get_token(token_list, "("):
        x = get_sum(token_list)
        if not get_token(token_list, ")"):
            raise ValueError("Missing close parenthesis")
        return x
    else:
        x = token_list[0]
        if type(x) != type(0): return None
        del token_list[0]
        return Tree(x, None, None)

def get_product(token_list):
    a = get_number(token_list)
    if get_token(token_list, "*"):
        b = get_product(token_list)
        return Tree("*", a, b)
    return a
token_list = [2, "*", 3, "*", 5 , "*", 7, "end"]
tree3 = get_product(token_list)
print_tree_inorder(tree3)

def get_sum(token_list):
    a = get_product(token_list)
    if get_token(token_list, "+"):
        b = get_sum(token_list)
        return Tree("+",a,b)
    return a
token_list = [9, "*", 11, "+", 5, "*", 7, "end"]
tree = get_sum(token_list)
print_tree_postorder(tree)

token_list = [9, "*", "(", 11, "+", 5, ")", "*", 7, "end"]
tree4 = get_sum(token_list)
print_tree_postorder(tree4)

#27.7
def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)

animal()
