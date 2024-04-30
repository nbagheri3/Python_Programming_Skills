# In this program I want to practice using loops.
student_heights = input("Enter a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height_of_student in student_heights:
    total_height += height_of_student

number_of_students = 0
for height_of_student in student_heights:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")