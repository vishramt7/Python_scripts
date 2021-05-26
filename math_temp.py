
def add (a, b):
    return a + b

print("This is outside the main function", __name__)

if __name__ == "__main__":
    print("This is inside main function")
    print(add(5, 15))