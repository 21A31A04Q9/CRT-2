class student:
    def __init__(self,name,rollNum,javaMarks,pythonMarks,mathMarks):
         self.name=name
         self.rollNum=rollNum
         self.javaMarks=javaMarks
         self.pythonMarks=pythonMarks
         self.mathMarks=mathMarks

    def printalldetails(self):
        print(self.name)
        print(self.rollNum)
        print(self.javaMarks)
        print(self.pythonMarks)
        print(self.mathMarks)
obj=student("kumar",501,67,45,78)
obj.printalldetails()
