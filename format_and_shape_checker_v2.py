import math


def instructions():
    print("""
~~~Instructions~~~
  1. Select your shape from the list.
  2. Choose what to find (perimeter or area).
  3. Enter your values.
  4. Read your answer!
""")


def float_check(question):
    """runs until the user enters a positive number greater than 0.1."""
    while True:
        try:
            value = float(input(question))
            if value < 0.1:
                print("Sorry, this is too small. Please try again.")
            elif value > 1e40:
                print("Sorry, this is too large. Please try again.")
            else:
                return value
        except ValueError:
            print("Oops - please enter a number.")


def string_check(question, valid_answers, num_letters):
    """Accepts the full word or its first num_letters characters."""
    while True:
        response = input(question).lower().strip()
        for item in valid_answers:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose from {valid_answers}")


shape_ans = ["square", "triangle", "rectangle"]
format_ans = ["perimeter", "area"]
yes_no = ["yes", "no"]

while True:
    print()

    if string_check("Would you like to see the instructions? ", yes_no, 1) == "yes":
        instructions()

    shape = string_check("What shape? ", shape_ans, 1)
    fmt = string_check("Perimeter or area? ", format_ans, 1)

    # Collect dimensions
    base = float_check("Base: ")
    height = float_check("Height: ")
    side3 = None
    if shape == "triangle" and fmt == "perimeter":
        side3 = float_check("Third side: ")

    # Calculate and display result
    if fmt == "area":
        if shape == "triangle":
            result = 0.5 * base * height
        else:
            result = base * height
        print(f"The area of your {shape} is {result}.")

    else:  # perimeter
        if shape == "square":
            result = base * 4
        elif shape == "rectangle":
            result = (base + height) * 2
        else:  # triangle
            result = base + height + side3
        print(f"The perimeter of your {shape} is {result}.")




