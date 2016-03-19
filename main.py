
class Stack:
    def __init__(self):
        self.stack_heap = []

    def push(self, *params):

        for items in params:
            if len(self.stack_heap) != 5 and isinstance(items, str):
                self.stack_heap.append(items)
            else:
                raise Exception("Parameter format invalid")

                '''
                 [stack_pile.append(items) for items in params if len(stack_pile) is not 5 and isinstance(items, str)]
                '''

    def pop(self):
        self.stack_heap.remove(self.stack_heap[len(self.stack_heap) - 1])
