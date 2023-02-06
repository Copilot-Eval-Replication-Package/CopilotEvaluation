import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="" "")
            temp = temp.next


def insertion_sort(head):
    if head is None:
        return None
    sorted_list = Node(head.data)
    head = head.next
    while head:
        if head.data < sorted_list.data:
            temp = sorted_list
            sorted_list = Node(head.data)
            sorted_list.next = temp
        else:
            temp = sorted_list
            while temp.next and temp.next.data < head.data:
                temp = temp.next
            temp.next = Node(head.data)
            temp.next.next = temp.next
        head = head.next
    return sorted_list


if __

