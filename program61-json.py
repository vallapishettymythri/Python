#Json is used for storing and exchanging the data. Json is written with java script.
#Conversion of Json to python
import json
x='{"name":"John","age":30,"city":"new york"}'
y=json.loads(x)
print(y["age"])

#conversion of python to json
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)