class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        result = self.stack[len(self.stack) - 1]
        temporary_stack = self.stack
        self.stack = []
        cnt = 1
        for item in temporary_stack:
            if cnt < (len(temporary_stack)):
                self.stack.append(item)
            cnt += 1
        return result

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

my_stack = Stack()
my_stack.push("x")
my_stack.push("y")
my_stack.push("z")
print(my_stack.pop())
print(my_stack.pop())