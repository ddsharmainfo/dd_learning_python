class Test():

    def __init__(self):
        print("==== From init method ====")

    def m1(self):
        print("==== From method 1")

    def m2(self):
        print("==== From method 2")

if __name__ == "__main__":
    print("==== From Main method ====")

    test = Test()
    test.m1()
    test.m2()