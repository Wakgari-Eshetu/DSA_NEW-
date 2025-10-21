def check(n):
    if n < 10:
        print (True)
    else:
        print(False)
check(90)
# inheritace of the class form to other 
class Class:
    var = 24  #class variable 
    def __init__(self,name ,where):
        self.name = name 
        self.where = where #instance variable 
    def check(self):
        print(self.name ,"found in ",self.where)
C = Class("name","addis")
C.check()

