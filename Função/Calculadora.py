def addition(number, number2):
    return number + number2

def subtration(number, number2):
    return number - number2

def multiplication(number, number2):
    return number * number2

def division(number, number2):
    return number / number2

def porcentagem(number, number2):
    return (number/100)*number2

def porcentagem2(number, number2):
    return (number/number2)*100

while True:
    number = float(input("Choose an number: "))
    number2 = float(input("Choose an other number: "))
    question = input("Disponible operation: \n+ - Addition\n- - Subtration\n* - Multiplication\n/ - Division\n% - Percentage\n")
    if question == "+":
        print(addition(number, number2))

    elif question == "-":
        print(subtration(number, number2))

    elif question == "*":
        print(multiplication(number, number2))

    elif question == "/":
        print(division(number, number2))

    elif question == "%":
        temp = input("1 - 80% of 40 = X\n2 - X% of 60 = 12\n")
        temp2 = input("1 - The first value is what you are looking for: \n2 - The second value is what you are looking for: ")
        if temp =="1":
            if temp2 == "2":
                number, number2 = number2, number
            print(porcentagem(number, number2))
        elif temp =="2":
            if temp2 == "2":
                number, number2 = number2, number
            print(porcentagem2(number, number2))
        else:
            print("Error")

    else:
        print("Invalid operation!!!")))