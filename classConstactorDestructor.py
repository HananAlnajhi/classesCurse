class Student:
    def __init__(self):
        self.__name = ''
        print("Constractor")
    def __del__(self):
      self.__name = ''
      print("Destructor")
    def setname(self, name):
        print('setname() called')
        self.__name = name

    def getname(self):
        print('getname() called')
        return self.__name

    name = property(getname, setname)
ob = Student()
ob.setname("Hanan")
print(ob.getname())
