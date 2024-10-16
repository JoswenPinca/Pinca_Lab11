#ask for name
name=input("What is your full name? ")

#ask for 3 subject grades
grade_1=float(input("What is the grade of your first subject? "))
grade_2=float(input("What is the grade of your second subject? "))
grade_3=float(input("What is the grade of your third subject? "))

#averaging process
sum_grade=(grade_1 + grade_2 + grade_3)
avg_grade=(sum_grade/3)

#print results
print(f"Name: {name}")
print(f"Average Grade: {avg_grade:.2f}")

#print results with if, elif, else conditions
if avg_grade>=85 and avg_grade<=94:
    print(f"Congratulations! You are qualified to be an Academic Honor Student this Semester with an average grade of {avg_grade:.2f}!")
elif avg_grade>=95 and avg_grade<=100:
    print(f"Congratulations! You are qualified to be an Academic Honor Student this Semester with Highest Honors, with an average grade of {avg_grade:.2f}!")
else:
    print(f"Congratulations, this is your grade for this semester! {avg_grade:.2f}")