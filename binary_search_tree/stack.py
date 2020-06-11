"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   A linked list is a class, where you have to create the methods that it uses to access length, ad/remove elements, etc.
   An array has built in methods.
### Stacks
* Should have the methods: `push`, `pop`, and `len`.
   * `push` adds an item to the top of the stack.
   * `pop` removes and returns the element at the top of the stack
   * `len` returns the number of elements in the stack.
"""
from singly_linked_list import LinkedList


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(-1)


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            pop = self.storage.remove_tail()
            self.size -= 1
            return pop