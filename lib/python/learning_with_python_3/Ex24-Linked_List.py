class Node:
    def __init__(self,cargo=None,next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


#24.3
def print_list(node):
    while node is not None:
        print(node, end= " ")
        node = node.next
    print()

print_list(node1)


#24.4
def print_backward(list):
    l = []
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end= " ")

print_backward(node1)


#24.7
def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    first.next = second.next
    second.next = None
    return second

#24.8
def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")

print_backward_nicely(node1)

#24.9
class LinkedList:
