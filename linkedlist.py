class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в кінець списку
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Вивід списку
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print('None')

    # Реверсування списку
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # Сортування злиттям
    def sort(self):
        def merge_sort(node):
            if not node or not node.next:
                return node

            # Знаходження середини
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None

            left = merge_sort(node)
            right = merge_sort(mid)
            return merge(left, right)

        def merge(left, right):
            dummy = Node(0)
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        self.head = merge_sort(self.head)

# Об’єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    a, b = list1.head, list2.head

    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b

    merged = LinkedList()
    merged.head = dummy.next
    return merged


print("Початковий список:")
ll = LinkedList()
for val in [4, 1, 3, 2]:
    ll.append(val)
ll.print_list()

print("\n Реверсований список:")
ll.reverse()
ll.print_list()

print("\n Відсортований список:")
ll.sort()
ll.print_list()

print("\n Другий список:")
ll2 = LinkedList()
for val in [0, 5, 6]:
    ll2.append(val)
ll2.sort()
ll2.print_list()

print("\n Об'єднаний відсортований список:")
merged = merge_sorted_lists(ll, ll2)
merged.print_list()