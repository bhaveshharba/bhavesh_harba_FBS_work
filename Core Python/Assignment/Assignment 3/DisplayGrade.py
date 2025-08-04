# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = int(input('Enter Marks of First Subject :')) 
sub2 = int(input('Enter Marks of Second Subject :'))
sub3 = int(input('Enter Marks of Third Subject :'))
sub4 = int(input('Enter Marks of Fourth Subject :'))
sub5 = int(input('Enter Marks of Fifth Subject :'))

total_marks = (sub1 + sub2 + sub3 + sub4 + sub5)
percentage = (total_marks/500)*100

print(f'{percentage}%')

if(percentage >= 95):
    print('Grade : First Class.')
elif(percentage >= 75):
    print('Grade : Second Class.') 
elif(percentage >= 60):
    print('Grade : Third Class.')
elif(percentage >= 35):
    print('Grade : Pass.')
else:
    print('Fail.')