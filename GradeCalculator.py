# Ask's the user to input the name and grade's of the student

grades = input("Please Enter The Student's Name Followed By The Grades: ")


# Split's the grade's into a list

grades_list = grades.split(",")

# Make's sure the input is not exactly 6

if len(grades_list) != 6:

	print("Invalid Input!!!")

else:

# Computes the grade's

	students_grades = grades_list[2:]
  
# Turn's the student grade's into integer's

	students_grades = [int(i) for i in students_grades]
  
# Compute's the sum of the grade's

	total_grades = sum(students_grades)
  
  
# Compute's the letter grade
	
	if total_grades >= 90:
	
		letter_grade = "A"
	  
	elif total_grades >= 80 and total_grades <= 89:
		
		letter_grade = "B"
	  
	elif total_grades >= 70 and total_grades <= 79:
		
		letter_grade = "C"
	  
	elif total_grades >= 60 and total_grades <= 69:
		
		letter_grade = "D"
	  
	else:
		
		letter_grade = "F"
  
  
# Print's the student's name and the letter grade

print("{},{}, {},".format(grades_list[0],grades_list[1],letter_grade))