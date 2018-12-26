import json
fileContainer = open('one.txt', 'r')
json.dump(x, fileContainer)
x = json.load(fileContainer)