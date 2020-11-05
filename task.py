# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as youcan, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

def average(lista):
  sum = 0
  for el in lista:
    sum+=el
  return sum/len(lista)


class Student:
  def __init__(self, first_name, surname):
    self.first_name = first_name
    self.surname = surname
    self.grades = []

  def student_average(self):
    sum = 0
    for el in grades:
      sum+=el
    return surname

class SchoolClass:
  def __init__(self, name):
    self.name = name
    self.students = []
  def append_student(self,s):
    students.append(s)
  def class_average(self):
    stud_averages = []
    for stud in students:
      stud_averages.append(average(el))
    return average(stud_averages)


class School:
  def __init__(self, school_name):
    self.school_name = school_name;
    self.classes = []
  def append_class(self,c):
    classes.append(c)


if __name__ =='__main__':
  s1 = Student('Marek', 'Kowalski')
  s2 = Student ('Jarek', 'Mały')
#   sclass = SchoolClass('1A')
#   sclass.append_student(s1)
#   sclass.append_student(s2)
