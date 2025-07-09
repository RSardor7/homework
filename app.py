class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def start_from(self, index):
        if 0 <= index < len(self.data):
            self.index = index
        else:
            raise IndexError("Index out of range")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def random(self):
        total = 0
        for i in range(len(self.data)):
            total += (i + 1) * (self.data[i] % 10)
        index = total % len(self.data)
        return self.data[index]

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

