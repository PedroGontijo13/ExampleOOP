class Student:
    
    #step1: defining properties
    #properties, attribtes
    #name,grades, studentID     instance properties
    
    
    #step2: define an initializer for the class
    #_ private 
    
    def __init__(self, name, sGrades, SstudentID):
        self._name = name
        self._grades = sGrades
        self._studentID = SstudentID
        
    
    #step3: defining some public interfcaes
    #getGPA
    #addGrade
    
    def addGrade(self, newGrade):
        self._grades.append(newGrade)
        
    
    def getGPA(self):
        totalSum = 0
        for grade in self._grades:
            totalSum = totalSum + grade
        
        avg = totalSum/len(self._grades)
        return avg
        
def CreateStudent():
  name = str(input("Name:"))
  grade = []
  studentID = str(input("Student ID:"))
  student1 = Student(name, grade, studentID)
    
  student1.addGrade(20)
  student1.addGrade(50)
  
  print("GPA so far is %f" %(student1.getGPA()))
  
  student1.addGrade(80)
  student1.addGrade(35)
  
  print("GPA so far is %f" %(student1.getGPA()))
        
def main():
  CreateStudent()
    
    
    
main()
    