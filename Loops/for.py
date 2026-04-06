for k in range(10):
    print(k)


for i in range(4):
        for j in range(4):
         print("*",end="")
        print()


for i in range(5):
    for j in range (i+1):
             print("*", end="")
    print()



# for else: 


list=[1,2,3,4,5,67,7,8, 15,135,120]

for list in list:
    if (list%13==0):
         print( list)
         break
else:
     print('not found')