def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Divide")
while True:
   ch=input("Enter choice(1/2/3/4):")
   if ch in ('1','2','3','4'):
       try:
          num1=float(input("Enter first number:"))
          num2=float(input("Enter second number:"))
       except ValueError:
           print("Invalid input.Please enter a number.")
           continue
       if ch=='1':
           print(num1,"+",num2,"=",add(num1,num2))
       elif ch=='2':
           print(num1,"-",num2,"=",subtract(num1,num2))
       elif ch=='3':
           print(num1,"*",num2,"=",multiply(num1,num2))
       elif ch=='4':
           print(num1,"/",num2,"=",divide(num1,num2))
       next_calculation=input("Lets do next calculation?(yes/no):")
       if next_calculation=="no":
         break
   else:
        print("Invalid Input!")