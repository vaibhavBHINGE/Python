# Mehtod overloading

class over:
    def sum(self,a,b,c=0):
        return  a+b+c
    
obj=over()
r=obj.sum(1,2)
print(r)


# Method Overridng 

class c1:
    def div(self):
        return("in 10th")

class c2(c1):
    def div(self):
        return("in 12th")

class c3(c2):
    def div(self):
        return("in masters")

obj=c3()
print(obj.div())