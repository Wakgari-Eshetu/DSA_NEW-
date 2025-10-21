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
        self.where = where #instance variable 
    def check(self,name ,nan):
        self.name = name 
        self.nan = nan

