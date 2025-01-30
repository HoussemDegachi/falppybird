import json

try:
    with open('data.json', 'w') as load_file:
        data = json.load(load_file)
        print(data)
except:
    print("no")