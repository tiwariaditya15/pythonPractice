
class Range:
    def __init__(self, *args):
        numberargs = len(args)
        if numberargs < 1 : raise TypeError("Enter atleast 1 arguments")
        elif numberargs == 1 :
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numberargs == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif numberargs == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else : raise TypeError("Maximum 3 arguments are allowed.")


    def __iter__(self):
        i = self.start
        while (i < self.stop) :
            yield i
            i = i + self.step



gene = Range(20)
for i in gene : 
    print(i, end = " ")