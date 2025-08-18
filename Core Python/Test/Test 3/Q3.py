n_emp = int(input('Enter No of Emp :'))
count = 1
total_salary= 0
total_salary_all = 0
while(count <= n_emp):
    salary = int (input('Enter basic salary of emp :'))
    if(salary <= 20000):
        da = salary * 10 /100
        total_salary = salary + da
        ta = salary * 12 /100
        total_salary = total_salary +ta
        hra = salary * 15 /100
        total_salary = total_salary + hra
        print(f'\nTotal Salary of emp is {total_salary}\n')
    else:
        da = salary * 15 /100
        total_salary = salary + da
        ta = salary * 18 /100
        total_salary = total_salary +ta
        hra = salary * 20 /100
        total_salary = total_salary + hra
        print(f'\nTotal Salary of emp is {total_salary}\n')
    total_salary_all += total_salary
    count += 1
print()
print(f'Total salary of all emp is {total_salary_all}')