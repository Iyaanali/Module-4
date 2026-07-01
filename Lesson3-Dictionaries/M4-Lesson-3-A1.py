student_data = {
    "id1": {"name": "John", "class": "v", "subject integration": ["math", "science", "english"]},
    "id2": {"name": "Jane", "class": "v", "subject integration": ["math", "science", "english"]},
    "id3": {"name": "John", "class": "v", "subject integration": ["math", "science", "english"]},#duplicate of id1
    "id4": {"name": "Mike", "class": "v", "subject integration": ["math", "science", "english"]},
}

result = {}
seen_keys = set()

for key, value in student_data.items():
    # Create a unique identifier for each student based on their name and class
    unique_identifier = (value["name"], value["class"])
    
    if unique_identifier not in seen_keys:
        seen_keys.add(unique_identifier)
        result[key] = value

print(result)