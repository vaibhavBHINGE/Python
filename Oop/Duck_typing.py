class A:
    def Name(self):
        print("Vaibahv_a")


class B:
    def Name(self):
        print("Vaibahv_b")
    
def Duck(c):
    c.Name()


a=A()
b=B()

Duck(a)
Duck(b)