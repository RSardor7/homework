def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as file:
            file.write(f"Parameters: {args}, {kwargs}\n")
            file.write(f"Result: {result}\n")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greeting(name):
    return f"Salom, {name}!"

print(add(3, 5))
print(greeting("Sardorbek"))

