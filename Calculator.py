#name = "MynameNikita"
#number = 1234
#print ("Hello")
#print (number)
#print (name)

# b = input("First\n")
# a = input("Second\n")
# dia = input("What to do\n")

# if   dia=="*":
#     print(int(a)*int(b))
# elif dia=="+":
#     print(int(a)+int(b))
# elif dia=="-":
#     print(int(a)-int(b))    
# elif dia=="/":
#     print(int(a)/int(b))
# else:
#     print("Error")    
# for i in range(10):
#     print (23)

def calculate_tax(income):

    if income <= 1000:

        tax = income * 0.05

    elif income <= 5000:

        tax = income * 0.10

    else:

        tax = income * 0.15

    return tax


def calculate_net_income(income, tax):

    return income - tax


def main():

    income = float(input("Введіть вашу заробітну плату: "))

    tax = calculate_tax(income)

    net_income = calculate_net_income(income, tax)

    print("Заробітна плата:", income)

    print("Оподаткування:", tax)

    print("Чистий дохід:", net_income)


if __name__ == "__main__":

    main()
