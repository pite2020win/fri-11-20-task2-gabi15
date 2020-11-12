# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
import statistics
import json
import os
import sys

def get_school(schools, school_name):
    picked_school = next(school for school in schools if school["school_name"] == school_name)
    return picked_school


def get_class(schol, school_name, class_name):
    picked_school = get_school(schools, school_name)
    picked_class = next(c for c in picked_school['classes'] if c["class_name"] == class_name)
    return picked_class


def get_student(schools, school_name, class_name, students_surname):
    picked_class = get_class(schools, school_name, class_name)
    picked_student = next(student for student in picked_class['students'] if student['surname']==students_surname)
    return picked_student


def get_students_average(schools, school_name, class_name, students_surname):
    picked_student = get_student(schools, school_name, class_name, students_surname)
    return statistics.mean(picked_student['grades'])
        

def get_school_average(schools, school_name):
    picked_school = get_school(schools, school_name)
    class_averages = []
    for c in picked_school['classes']:
        class_averages.append(get_class_average(schools,school_name, c["class_name"]))
    return statistics.mean(class_averages)


def get_class_average(school, school_name, class_name):
    picked_class = get_class(school, school_name, class_name)
    class_average = []
    for student in picked_class['students']:
        class_average.append(statistics.mean(student['grades']))
    return statistics.mean(class_average)

def append_student(school, school_name, class_name, s_name, s_surname, s_grades):
    picked_class = get_class(schools, school_name, class_name)
    picked_class["students"].append({"name":s_name, "surname":s_surname, "grades":s_grades})

def append_attendance(school, school_name, class_name, students_surname, is_present):
    picked_student = get_student(school, school_name, class_name, students_surname)
    picked_student['presence'].append(is_present)

def get_students_attendance(school, school_name, class_name, students_surname):
    chosen_student = get_student(school,school_name,class_name,students_surname)
    return sum(chosen_student['presence'])/len(chosen_student['presence'])
    
        


if __name__ == "__main__":

    with open(os.path.join(sys.path[0], "school.json")) as json_file:
        schools = json.load(json_file)

    print("School average for 3LO is {average}".format(average = get_school_average(schools, "3LO")))
    print("Class average for 1A in 3LO is {average}".format(average = get_class_average(schools,'3LO','1A')))
    print("Students Kowalski average is {average}".format(average = get_students_average(schools,'3LO','1A','Kowalski')))
    print("Students Gorgol presence is {presence}".format(presence = get_students_attendance(schools,'3LO','1B','Gorgol')))

    #some changes in data
    append_student(schools,'3LO','1A','Ania','Magiera',[1,4,5])
    append_attendance(schools, '3LO','1A','Kowalski',True)
    with open('new_schools.json', 'w') as f:
        json.dump(schools, f, indent =2)



