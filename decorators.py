

class Duck :
    def __init__(self, **args):
        self.properties = args
    def getProperties(self):
        return self.properties
    def getProperty(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None)
    
    @color.setter
    def color(self, c) :
        self.properties['color'] = c
    
    @color.getter
    def color(self) :
        return self.properties


obj = Duck(color = "red")
obj.color = 'Red'
print(obj.color)