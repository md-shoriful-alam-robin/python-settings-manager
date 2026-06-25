





class Student:

  def __init__(self, name, listOfMarks):
    self.name=name
    self.listOfMarks= listOfMarks

  def average(self):
    sum= 0
    for eachValue in self.listOfMarks:
      sum= sum+eachValue

      average= sum/3
    print("Average is: ", average)

student1= Student("Robin", [99, 98, 97])
student1.average()