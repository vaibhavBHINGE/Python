class A:
    def __init__(self):
        print("c=vsb")
    def m1(self):
        print("Vaibhav")

class B:
    def __init__(self):
        print("vb")
    def m2(self):
        print("Suresh")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("Vaibhav")
    def m3(self):
        print("Bhinge")

s=C()
s.m1()
s.m2()
s.m3()