# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

s_num=int(input("enter number of student = "))
total_marks=0
total_percentage=0

for i in range (0,s_num):
    C=int(input("Enter C marks = "))
    PHP=int(input("Enter PHP marks = "))
    DBMS=int(input("Enter DBMS marks = "))
    Java=int(input("Enter Java marks = "))
    Python=int(input("Enter Python marks = "))

    total_marks= C+PHP+DBMS+Java+Python
    percentage= (total_marks/500)*100
    
    print(f'percentage = {percentage}',end=' ')
    print()
    total_percentage=total_percentage+percentage


average_percentage=total_percentage/s_num
print(f'Average percentage : {average_percentage}')