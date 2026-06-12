#   functions for calculator 

class calculator:

    @staticmethod
    def add(a,b):
        return a+b
    
    def sub(self,c,d):
        return c-d
    
    def mul(self,e,f):
        return e*f
    @staticmethod
    def div(g,h):
        if (h==0):
            return ("please enter number greater that 0 ")
            
        return g/h
    

cal=calculator()
result=calculator.div(0,3)
print("Divide using class fun: ",result)
print("divide class obj: ", cal.div(3,0))