class Stack:
    def __init__(self):
        self.data = []

    def validate_if_string(self,element):
        if not isinstance(element, str):
            raise TypeError('Only strings')

    def push(self, element):
        self.validate_if_string(element)
        return self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


    def __str__(self):
        return str(self.data)




