
class Student:
    def __init__(self,roll,name,marks_list):
        self.roll = roll
        self.name = name
        self.marks_list= marks_list

    def calculate_percentage(self,m):
        percentage =sum(self.marks_list)//m
        return percentage

    def find_grade(self,percentage):
        if percentage >= 80:
            return 'grade is A'
        elif 80 < percentage >= 60:
            return 'garde is B'
        elif 60 < percentage >=40:
            return 'garde is C'
        else:
            return 'F'
        
        

list_obj = []
roll = int(input())
name = input()
marks_list = []
m = int(input())
for i in range(m):
    marks_list.append(int(input()))


list_obj.append(Student(roll,name,marks_list))

print(list_obj[0].calculate_percentage(m))
print(list_obj[0].find_grade(percentage))
