#GPA calculator

#input data from xml
GPV = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "E": 0.0}
import xml.etree.ElementTree as ET
tree = ET.parse('course.xml')
root = tree.getroot()
department = input("Enter your Department: ")
level = input("Enter your Level: ")
total_gpv = 0
total_credits = 0
if root.find(department):
    for depart in root.findall(department):
        if depart.find(level):
            for level_1 in depart.findall(level):
                for course in level_1:
                    grade = input(course.find('code').text)
                    if grade in GPV.keys():
                        gpv = GPV[grade]
                        credit = int(course.find('credit').text)
                        total_gpv = total_gpv + (gpv * credit)
                        total_credits = total_credits + credit
                    else:
                        print("no")
GPA = total_gpv / total_credits
print(GPA)