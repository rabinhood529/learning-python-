# day 1 learning oop 
class Student():
    def __init__(self, name, math, science, geometry):
        self.name = name
        self.math = math
        self.science = science
        self.geometry = geometry
        
# we can sue list here 
# instead self.math, self.science, self.geometr we could have used
# self.marks
        
    def avergae(self):
        total_average = sum([self.math, self.science, self.geometry])/3
        return total_average
#best method is to use loop 
# def average(self):
# sum=0
# for value in self.marks:
# sum += value
# print(self.name,sum/3)
#  
s1 = Student("sabin", 45, 50, 60)
print(s1.avergae())





