a=int(input("Enter first number to div: "))
b=int(input("Enter second number to div: "))
 
try:
    r=a/b
    k=int(input("enter a Number: "))
    
except ZeroDivisionError as e:
    print("can't divide be zero ",e)
except ValueError as e:
    print("enter int value ", e)
except Exception as e:
    print("something went wrong.. ",e)
finally:
    print("finllay its over....")