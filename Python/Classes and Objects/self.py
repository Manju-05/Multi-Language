# self parameter
"""The self parameter is a reference to the current instance / object of the class, and is used to access variables / functions of  that current class.

It must be provided as the extra parameter inside the method definition.

==> self is a keyword that is used to refer / acces the varibles/functions of that current class.
"""

class diploma:
    branch1 = "CME"
    std = "Manju"
    roll = 47
    def details(self):
        print(self.std)
        print(self.branch1)
        print(self.roll)

obj = diploma()
obj.details()


class info():
    name = "ramu"
    occ = "tester"
    city = "nandyal"
    def getdata(self):
        print(f"my name is {self.name}. And I am {self.occ} .And I am from {self.city}")
object4 = info()
object4.getdata()