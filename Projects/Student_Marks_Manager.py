'''

📍 Concepts: Lists, Tuples, Sets, Dictionaries, List/Dict/Set Comprehensions, Iteration, Membership.
📝 Task: Student Marks Manager

Store student names and marks in a dictionary.

Find topper, average, pass/fail using conditions.

Use list comprehensions to filter students above average.

Use set operations to compare students of two classes.

'''
def student_report():
    student_data = {}
    n = int(input("Enter the number of student you want to add : "))

    for i in range(n):
        Name = input(f"Kindly Enter the name of Student {i+1} : ")
        Marks = int(input(f"Kindly Enter the marks of {Name} : "))
        student_data[Name] = Marks
    
    topper = max(student_data,key=student_data.get)

    average = sum(student_data.values())/len(student_data)
        
    print("Student report : ")

    for name,marks in student_data.items():
        status = "Pass" if marks>=50 else "Fail"
        print(f"{name} : {marks} - {status}")

    print(f"Toppper is {topper} with {student_data[topper]} Marks")
    print(f"Class Average marks are : {round(average,2)}")
    above_avg = [student for student in student_data.keys() if student_data[student]>average]
    print(f"Students with above average marks i.e {average} are : ",above_avg)



    classA = set(student_data.keys())
    classB = {"Rajesh","Akshay","Naitik"}
    print("Class A : ",classA)
    print("Class B : ",classB)
    print("Common Students : ",classA & classB) # intersection
    print("Unique Students from class A : ",classA-classB) # Difference
    print("Unique students form class B : ",classB-classA) # Difference
    print("All Students : ",classA | classB) # Union


student_report()

