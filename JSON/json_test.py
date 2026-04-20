import json

# Converts Py object in JSON

data={
    "Name":"Vaibhav",
    "City":"Pune",
    "Age":23
}

json_data=json.dumps(data)
print(json_data)


# Convrts JSON into a object 

response = '{"user": {"name": "Vaibhav"}}'
js_data = json.loads(response)

print(js_data)
print(type(js_data))


