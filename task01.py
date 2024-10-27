class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Конвертуємо список у звичайний Python список для виведення
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Функція для реверсування однозв'язного списку
def reverse_linked_list(linked_list):
    prev = None  
    current = linked_list.head 
    while current:
        next_node = current.next 
        current.next = prev  
        prev = current 
        current = next_node
    linked_list.head = prev 

# Функція сортування злиттям для однозв'язного списку
def merge_sort_linked_list(linked_list):
    if linked_list.head is None or linked_list.head.next is None:
        return linked_list 

    middle = get_middle(linked_list.head)
    next_to_middle = middle.next
    middle.next = None

    left_half = LinkedList()
    left_half.head = linked_list.head
    right_half = LinkedList()
    right_half.head = next_to_middle

    left = merge_sort_linked_list(left_half)
    right = merge_sort_linked_list(right_half)

    sorted_list = LinkedList()
    sorted_list.head = sorted_merge(left.head, right.head)
    return sorted_list

# Функція для знаходження середини списку (для злиття)
def get_middle(node):
    if not node:
        return node
    slow, fast = node, node.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Функція для злиття двох відсортованих списків
def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result

# Функція об'єднання двох відсортованих однозв'язних списків в один відсортований
def merge_two_sorted_lists(list1, list2):
    merged_list = LinkedList()
    merged_list.head = sorted_merge(list1.head, list2.head)
    return merged_list

# Тестування функцій
if __name__ == "__main__":
    
    list1 = LinkedList()
    list2 = LinkedList()

    for value in [1, 4, 6]:
        list1.append(value)

    for value in [2, 3, 5]:
        list2.append(value)

    # Реверсування списку
    print("Original list 1:", list1.to_list())
    reverse_linked_list(list1)
    print("Reversed list 1:", list1.to_list())

    # Сортування списку
    unsorted_list = LinkedList()
    for value in [3, 1, 4, 2]:
        unsorted_list.append(value)

    print("Unsorted list:", unsorted_list.to_list())
    sorted_list = merge_sort_linked_list(unsorted_list)
    print("Sorted list:", sorted_list.to_list())

    # Об'єднання двох відсортованих списків
    merged_list = merge_two_sorted_lists(list1, list2)
    print("Merged sorted lists:", merged_list.to_list())