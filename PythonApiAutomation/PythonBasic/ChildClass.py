from PythonBasic.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        # if the parent class constructor is parameterized you have to pass arguments in child class constructor by calling parent class name
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
