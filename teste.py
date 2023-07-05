import json
  
# Opening JSON file
f = open('data.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
#print(data)

for key in data.keys():
    if key.startswith("table") and isinstance(value, list):
        print("Tabela")
        print(key)
    elif key.startswith("text"):
        print("Texto")
        print(key)
    elif key.startswith("map"):
        print("Mapa")
        print(key)
  
# Closing file
f.close()