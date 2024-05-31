class student:
    def __init__(self,name,rollNum,javaMarks,pythonMarks,mathMarks):
         self.name=name
         self.rollNum=rollNum
         self.javaMarks=javaMarks
         self.pythonMarks=pythonMarks
         self.mathMarks=mathMarks
         
obj=student("kumar",501,67,45,78)
print(obj.name)
print(obj.rollNum)
print(obj.javaMarks)
print(obj.pythonMarks)
print(obj.mathMarks)
