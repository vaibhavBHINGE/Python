import json

# Writting JSON file
data={
    "Nmae":"Vaibhav",
    "age":23
}
with open("jsonFile.json", "w") as js_data:
    dt=json.dumps(data)
    js_data.write(dt)

# Reading the JSON File

with open("jsonFile.json","r")as f:
    result=f.read()
    print(result)
    