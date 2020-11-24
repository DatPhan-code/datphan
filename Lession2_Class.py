class Employee :
  countemp = 0

  def __init__ (self, name , salary):
    self.name= name
    self.salary = salary
    Employee.countemp +=1

  def displaycount(self):
    print "Total employee %d " % Employee.countemp

  def displayemployee(self):
    print "Name: " , self.name  , ", salary:",self.salary

emp1 = Employee("Zara", 300)
emp2 = Employee('H&M' , 200)

emp1.displayemployee()
emp2.displayemployee()

print 'Total employee %d' % Employee.countemp


class Parent :
    parentatt =100

    def __init__(self) :
        print 'Parent contructor'
    def parentmethod(self):
        print 'Parent method'
    def setAttribute(self , att) :
        Parent.parentatt = att
    def getAttribute(self):
        print 'Parent attribute: ' ,Parent.parentatt
class child(Parent):
    def __init__(self):
        print 'Calling parent contructor'
    def childmethod(self):
        print 'Calling parent method'
c = child()
c.childmethod()
c.parentmethod()
c.setAttribute(200)
c.getAttribute()







