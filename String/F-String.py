# this is to simplify string formatng 
info="My name is {} and i am from {}"
name='Vaibahv'
plcae="Pune"
print(info.format(name,plcae))#first way that existing strign by using string variabels to existing string variable
intro="Hello my name is {0} and i am from {1}".format(name,plcae)
print(intro) # this is the another way

# New followign the new way after the py 3.6
print("this is the new way to fromat string: ",f"i am from {plcae} adn i am in {plcae}")