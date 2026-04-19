import os

# Reading a file
f = open(r'F:\Gen AI\myfile.txt', 'r')  # 'r' is used to read the file
result = f.read()  # calling the read function
print(result)  # printing file content
f.close()

# Writing to a file (overwrites existing content or creates a new file)
w = open('file.txt', 'w')
show = w.write("This is me!")
w.close()

# Appending to a file (adds content to existing file)
a = open('file.txt', 'a')
p = a.write(" and my name is Vaibhav")
a.close()

# Using 'with' (no need to explicitly close the file)
with open('file.txt', 'r') as see:
    data = see.read()
    print(data)

# Creating a new file (using 'w' here)
with open("newFile.txt", "w") as new:
    dis = new.write("This is the new file created")

# Deleting a file
path = r"F:\Gen AI\newFile.txt"

if os.path.exists(path):
    os.remove(path)
    print("File removed..")
else:
    print("File not found")

# removing folder
os.rmdir(r"F:\Gen AI\Python\testing")
print("removed folder....")