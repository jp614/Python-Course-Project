sales = [0] * 7
again = "y"


while again == "y":
    total = 0
    print("Enter sales for each day of the week: ")
    
    for index in range(len(sales)):
        sales[index] = float(input(f'Day #{index + 1}: '))
        total += sales[index]
    
    print("Here each day you've entered:")

    for value in sales:
        print(value)

    print("Here's is the total sales for the week:")
    print(total)

    again = input("Would you like to find the total sales for another week?(Enter y for yes): ")
    
