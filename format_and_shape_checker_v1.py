# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank.  Please try again.\n")


def string_check(question, valid_answers, num_letters):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a range of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


# Main Routine goes here

# intialise variables / non-default options for string checker
shape_ans = ("circle", "square", "triangle", "rectangle")
format_ans = ("perimeter", "area")

# loop for testing purposes...
while True:
    print()

    # ask what shape they want and print the result
    shape = string_check("Shape chosen: ", shape_ans, 1)
    print(f"You have selected ({shape})")

    format = string_check(
        "Do you want to find the perimeter or the area? ", format_ans, 1
    )
    print(f"You have selected {format}")

    # Ask for their dimensions
    dimensions1 = int_check("First dimensions (base) of your shape: ")

    dimensions2 = int_check("Second dimensions (height) of your shape: ")

    if shape == "triangle" and format == "perimeter":
        dimensions3 = int_check("Third dimensions (for perimeter) of your shape: ")
    else:
        continue

    # format calculations
    area = dimensions1 * dimensions2
    area_triangle = 0.5 * dimensions1 * dimensions2
    perimeter_square = dimensions1 + dimensions2
    perimeter_triangle = dimensions1 + dimensions2 + dimensions3
    perimeter_rectangle = dimensions1 + dimensions2 * 2

    # to find area and print the result
    if shape == "square" and format == "area":
        print(f"The area of your square is {area}")
    elif shape == "rectangle" and format == "area":
        print(f"The area of your Rectangle is {area}")
    elif shape == "triangle" and format == "area":
        print(f"The area of your Triangle is {area_triangle}")

    # Output error message / success message for 1st dimension
    if dimensions1 < 0.1:
        print("Sorry, this is too small. try again. ")
        continue
    elif dimensions1 > 9999:
        print("Sorry, this is too large. try again. ")
        continue
    else:
        pass

    # Output error message / success message for 2nd dimension
    if dimensions2 < 0.1:
        print("Sorry, this is too small. try again. ")
        continue
    elif dimensions2 > 9999:
        print("Sorry, this is too large. try again. ")
        continue
    else:
        pass

    # Output error message / success message for 3rd dimension
    if shape == "triangle" and format == "perimeter" and dimensions3 < 0.1:
        print("Sorry, this is too small. try again. ")
        continue
    elif shape == "triangle" and dimensions3 > 9999:
        print("Sorry, this is too large. try again. ")
        continue
    else:
        pass







