import math


def instructions():
    print("""
~~~Instructions~~~
  1. Select your shape from the list.
  2. Choose what to find (perimeter/circumference or area).
  3. Enter your values.
  4. Read your answer!
""")


def float_check(question):
    """Runs until the user enters a positive number between 0.1 and 1e40."""
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
        abbrevs = [item[:num_letters] for item in valid_answers]
        print(f"Please choose from {valid_answers} (or {abbrevs})")


shape_ans = ["square", "triangle", "rectangle", "circle"]
format_ans = ["perimeter", "area"]
yes_no = ["yes", "no"]

while True:
    print()

    if string_check("Would you like to see the instructions? ", yes_no, 1) == "yes":
        instructions()

    shape = string_check("What shape? (square, triangle, rectangle, circle) ", shape_ans, 2)

    # Circles have a fixed set of outputs — skip the perimeter/area choice
    if shape == "circle":
        radius = float_check("Radius: ")
        diameter = radius * 2
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2
        print(f"\n  Radius:        {radius:.2f}")
        print(f"  Diameter:      {diameter:.2f}")
        print(f"  Circumference: {circumference:.2f}")
        print(f"  Area:          {area:.2f}")

    else:
        fmt = string_check("Perimeter or area? ", format_ans, 1)

        # Collect dimensions
        if shape == "square":
            side = float_check("Side length: ")
            base = height = side
        else:
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
            print(f"The area of your {shape} is {result:.2f}.")

        else:  # perimeter
            if shape == "square":
                result = base * 4
            elif shape == "rectangle":
                result = (base + height) * 2
            else:  # triangle
                result = base + height + side3
            print(f"The perimeter of your {shape} is {result:.2f}.")

    print()
    if string_check("Calculate another shape? ", yes_no, 1) == "no":
        print("Goodbye!")
        break




