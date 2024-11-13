gradelist=[]
passers=0
student_count=0

print("Average Student Score")
print("=====================")
while student_count < 5:
    x = float(input("Enter the Student's Grade: "))
    if x < 40 or x > 100:
        print("Invalid grade. Please enter a grade between 40 and 100.")
    else:
        gradelist.append(x) 
        student_count += 1
        if x >= 75:
            passers = passers + 1
        
print("=====================")

sum = sum(gradelist)
average = sum/len(gradelist)
percent_passers=passers/len(gradelist) * 100

print(f"Average Between All Students: {average:.2f}")
print(f"Passers: {passers}")
print(f"% of those who passed: {percent_passers:.2f}%")
print(f"Grades: {gradelist}")