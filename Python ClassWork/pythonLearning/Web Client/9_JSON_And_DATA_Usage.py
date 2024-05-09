import json

json_data = '{"name": "John", "age": 30, "isStudent": false}'

# JSON data ==> dictionary object  ==> DESERIALIZATION
python_obj = json.loads(json_data)
print(python_obj)

# dictionary object ==> JSON data  ==> SERIALIZATION
python_obj['city'] = 'New York'
json_data_updated = json.dumps(python_obj)
print(json_data_updated)

#=================================================

import json

# Serialize Python object to JSON
python_obj = {'name': 'John', 'age': 30, 'is_student': False}
json_data = json.dumps(python_obj)
print("Serialized JSON:", json_data)

# Deserialize JSON to Python object
json_data = '{"name": "John", "age": 30, "is_student": false}'
python_obj = json.loads(json_data)
print("Deserialized Python Object:", python_obj)