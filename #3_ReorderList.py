'''
Created on 2014/2/25

@author: valthonis
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reorderList(head):
    # handle list with 0, 1, 2 elements
    if ((head == None)or(head.next == None)or(head.next.next == None)):
        return
    # cut the list in half, reverse the second half
    midNode = cutList(head)
    reversedhead = reverseList(midNode)
    mergeList(head, reversedhead)
    
def cutList(head):
# cut the list in half, return the middle node
    node = head
    count = 1
    # find length of the list
    while (node.next):
        node = node.next
        count += 1
    node = head
    # find the middle node
    for i in range((count-1) / 2):
        node = node.next
    midnode = node.next
    node.next = None    # cut the list into two sublist
    return midnode

def reverseList(node):
# reverse given list, return the new first node
    if (node.next == None):
        return node
    prevnode = node
    node = node.next
    prevnode.next = None
    while(node.next):
        pointer = node.next
        node.next = prevnode
        prevnode = node
        node = pointer
    node.next = prevnode
    return node

def mergeList(head, node):
# merge the two given list
    if (node.next == None):
        node.next = head.next
        head.next = node
        node.next.next = None
        return
    node1 = head.next
    node2 = node.next
    while (head.next):
        head.next = node
        node.next = node1
        head = node1
        node = node2
        node1 = head.next
        if (node.next != None):
            node2 = node.next
    if (node2):
        head.next = node2
        node2.next = None
    else:
        head.next = None

if __name__ == "__main__":
    node = []
    for i in range(5):
        node.append(ListNode(i))
    for i in range(4):
        node[i].next = node[i+1]
    reorderList(node[0])
    head = node[0]
    for i in range(5):
        print node[i].val,
    print
    for i in range(4):
        print head.val,
        head = head.next
    print head.val
