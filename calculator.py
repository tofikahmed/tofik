#Let's Build a calculator
#a + b
# a - b
#a * b
#a / b
#a % b

first = input("enter first number : ")
operator = input("enter operator (+,-,*,/,%) : ")
second = input("enter second number : ")

first = int(first)


second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

elif operator == :
    print(first % second)

else:
    print ("Invalid operation")
    import datetime

    current_time = datetime.datetime.now()
    print("Current Time is:", current_time.strftime("%H:%M:%S"))

    current_date = datetime.date.today()
    print("Current Date is:", current_date.strftime("%d/%m/%Y"))