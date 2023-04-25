class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.next = next
        self.prev = prev
        self.data = data

def push(head, data):
    node = Node(data, None, head)
    node.data = data
    node.next = head

    if (head != None):
        head.prev = node
    head = node
    return head

def swap(node):
    temp = node.prev
    node.prev = node.next
    node.next = temp

def revertList(head):
    prev = None
    node = head

    while node:
        swap(node)
        prev = node
        node = node.prev

    if prev:
        head = prev
    return head

def bubbleSort(head): 
    count = 0
    tail = None

    if (head == None):
        return
    
    while True:
        count = 0
        node = head

        while (node.next != tail):
            if (node.data > node.next.data):
                node.data, node.next.data = node.next.data, node.data
                count = 1
            node = node.next
        tail = node
        if count == 0:
            break

def printList(msg, head):
 
    print(msg, end='')

    while head:
        print(head.data, end=' —> ')
        head = head.next
 
    print('None')

if __name__ == '__main__':
 
    list = [2, 5, 8, 3, 21, 1, 0]
    head = None

    for i in range(7):
        head = push(head, list[i])
 
    printList('Before: ', head)
    bubbleSort(head)
    head = revertList(head)
    printList('After: ', head)