# Number of classes and students per class
classes = 6
students = 45

# Calculate total number of students
total_students = classes * students

# Calculate total number of classes (with maximum 27 students each)
total_classes = total_students / 27

# Testing output
print("Number of students:", total_students)
print("Number of classes needed:", total_classes)