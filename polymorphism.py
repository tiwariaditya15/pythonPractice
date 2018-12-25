

#class having details about engineer 
class engineer:
        def profession(self):
            print("Engineer's have different field of expertise such as IT, CS, Electronics etc.")
        def degreeDuration(self):
            print("Academics duration is nearly {0} years.".format(4))



#class having deatils about doctor's

class doctor:
    def profession(self):
        print("Doctor's have different fields of expertise such as Heart Speacialist, Surgeon, general Physician etc.")

    def degreeDuration(self):
        print("Academics duration is more than 5 years depending upon course.")

def bank(eg):
    eg.profession()
    eg.degreeDuration()

def hospital(dc):
    dc.profession()
    dc.degreeDuration()


def callingMain():
    eng = engineer()
    doc = doctor()
    bank(doc)
    hospital(eng)
#This line would generate an error in different programming language beacause object variable is refencing to list which has object's of type class engineer as well as 
#doctor but python's polymorphism supports refencing to both type of objects 
'''    for object in [eng, doc]:
        object.profession()
        object.degreeDuration()
'''
callingMain()
'''
In python , as we know it is a loosely typed language objects  really don't care about name of the class 
'''