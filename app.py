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
        import time
        t = int(str(time.time()).replace('.', '')[-5:])
        rand_index = t % len(self.data)
        return self.data[rand_index]

def infinite_counter(start=0):
    while True:
        yield start
        start += 1

