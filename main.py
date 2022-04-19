
# getting maximum and minimum input from the user
minimum_number = int(input("Enter the minimum number"))
maximum_number = int(input("Enter the maximum number"))

# accept set of disabled numbers till exit
active = True
disabled_numbers = []
while active:
    user_input = input("Enter the disabled number or 'N' to stop ")
    if user_input == 'n' or user_input == 'N':
        active = False
    else:
        disabled_numbers.append(int(user_input))

# checking weather the validation number in min and max number


def Check_number(validation_number):
    num_status = False
    for number in range(minimum_number, maximum_number):
        if number == validation_number:
            num_status = True
            break
    # checking weather the validation number in disabled number
    if num_status:
        if validation_number not in disabled_numbers:
            print(validation_number)
        else:
            validation_number += 1
            Check_number(validation_number)
    else:
        print("Invalid output")


# accept the number to validate and calling function to evaluate
validation_number = int(input("Enter the number for the validation"))
Check_number(validation_number)

#added some linessss
#added some more linessss