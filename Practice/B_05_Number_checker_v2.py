# functions go here
def int_check(question, num_type, exit_code=None):
    """Checks users enter an integer/float that is more than
    zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - Please enter an integer more than 0."
        change_to = int
    else:
        error = "oops - please enter a number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for exit code
        if response == exit_code:
            return response


        try:
            # Change the response to an integer and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return
            else:
                print(error)

        except ValueError:
            print(error)

# main routine goes here


#loop for testing
while True:
    print()

    # ask user for their name

    # Ask for their age and check it's between its 12 120
    age = int_check("Age: ")

    # ask user for an integer
    my_num = int_check("Choose a number more than zero: ")
    print(f"You Chose {my_num}")

