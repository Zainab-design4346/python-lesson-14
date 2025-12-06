def employee(name):
    print(name)

def salary(exp):
    if exp>=5:
        return 3000000
    elif exp>=3:
        return 1000000
    else:
        return 500000


n=input("Enter the name of employee: ")
employee(n)
exp=int(input("Enter the experience of employee: "))
a = salary(exp)
print("The salary of employee is ",a)