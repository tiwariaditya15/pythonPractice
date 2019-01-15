import simplejson as json
import os 

#if file exist then increasing age in json file
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is ", data["age"], "-----------Adding a year")
    data["age"] = data["age"] + 1
    print("New age is ", data["age"])
else:
    old_file = open("./ages.json", "w+")
    data = { "name":"aditya", "age":19}
    print("No file found , setting default age 19")

old_file.seek(0)
old_file.write(json.dumps(data)) 