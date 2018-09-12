# file two.py
import one as o

print("top-level in two.py")
o.func()

def func():
    print("func() in two.py")

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")

func()
