
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
    # 1: Iterate through the unsorted list.
    # 2: Compare the current element to the sorted list.
    # 3: If the current element is smaller than the sorted list, move the sorted list one position to the right and insert the current element.
    # 4: If the current element is larger than the sorted list, move the sorted list one position to the right and insert the current element.
    # 5: Repeat until the unsorted list is empty.
    # ! psuedo code below was generated by CoPilot AFTER function was created.
    # psudeo code:
    # while unsorted list is not empty:
    #     current element = unsorted list[0]
    #     sorted list = sorted list

