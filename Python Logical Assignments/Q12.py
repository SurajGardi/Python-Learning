# 12. Reverse Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

# Reverse logic
prev = None
curr = head

while curr is not None:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

head = prev

# Print reversed list
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next