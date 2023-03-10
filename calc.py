def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def prdt(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("select operations: ")
print("1.Add")
print("2.Subtarct")
print("3.Multiply")
print("4.Division")

while True:
    choice=input("enter choice 1/2/3/4: ")

    if choice in ('1','2','3','4'):
        try:
            n1=float(input('enter first number: '))
            n2=float(input('enter second number: '))
        except ValueError:
            print('invalid input. please enter a number.')
            continue

        if choice=='1':
            print(n1,'+',n2,'=',add(n1,n2))

        elif choice=='2':
            print(n1,'-',n2,'=',sub(n1,n2))

        elif choice=='3':
            print(n1,'*',n2,'=',prdt(n1,n2))

        elif choice=='4':
            print(n1,'/',n2,'=',div(n1,n2))


        next_calculation=input('lets do next calculation (yes/no): ')
        if next_calculation=='no':
            print('thank you')
            break

    

