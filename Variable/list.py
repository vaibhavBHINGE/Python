# Lists are mutuable
age=[12,13,14,15,12,12,161,7,125,1]
print(age)
Name=[12,"Vaibhav"]
print(Name)
Name.append(19)
print(Name)
Name.append("Bhinge")
print(Name)
Name.insert(2,"Suresh")
print(Name)
print(age.count(12))
age.reverse()
print(age)
Name[3]="Bhinge"
print(Name)