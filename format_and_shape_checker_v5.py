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
    """Runs until the user enters a positive number between 0.01 and 3e8."""
    while True:
        try:
            value = float(input(question))
            if value < 0.01:
                print("Sorry, this is too small. Please try again.")
            elif value > 3e8:
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


def display_results(fields: dict):
    """Prints a neatly aligned table of label -> value pairs."""
    label_width = max(len(k) for k in fields) + 1
    print()
    for label, value in fields.items():
        print(f"  {label + ':':<{label_width}} {value:.2f}")
    print()


shape_ans = ["square", "triangle", "rectangle", "circle"]
format_ans = ["perimeter", "area"]
yes_no = ["yes", "no"]

# Stores all calculations
history = []

if string_check("Would you like to see the instructions? ", yes_no, 1) == "yes":
    instructions()

while True:
    print()

    shape = string_check(
        "What shape? (square, triangle, rectangle, circle) ",
        shape_ans, 2)

    # Circles
    if shape == "circle":
        radius = float_check("Radius: ")
        diameter = radius * 2
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2

        display_results({
            "Radius": radius,
            "Diameter": diameter,
            "Circumference": circumference,
            "Area": area,
        })

        history.append({
            "Shape": "Circle",
            "Radius": radius,
            "Diameter": diameter,
            "Circumference": circumference,
            "Area": area
        })

    else:
        fmt = string_check("Perimeter or area? ", format_ans, 1)

        # Get dimensions
        if shape == "square":
            side = float_check("Side length: ")
            base = height = side
        else:
            base = float_check("Base: ")
            height = float_check("Height: ")

        side3 = None
        if shape == "triangle" and fmt == "perimeter":
            side3 = float_check("Third side: ")

        # Area
        if fmt == "area":
            if shape == "triangle":
                result = 0.5 * base * height
            else:
                result = base * height

            display_results({f"{shape.capitalize()} area": result})

            history.append({
                "Shape": shape.capitalize(),
                "Calculation": "Area",
                "Result": result
            })

        # Perimeter
        else:
            if shape == "square":
                result = base * 4
            elif shape == "rectangle":
                result = (base + height) * 2
            else:
                result = base + height + side3

            display_results({f"{shape.capitalize()} perimeter": result})

            history.append({
                "Shape": shape.capitalize(),
                "Calculation": "Perimeter",
                "Result": result
            })

    if string_check("Calculate another shape? ", yes_no, 1) == "no":
        print("\n=== Calculation History ===\n")

        for i, item in enumerate(history, start=1):
            if item["Shape"] == "Circle":
                print(f"{i}. Circle")
                print(f"   Radius: {item['Radius']:.2f}")
                print(f"   Diameter: {item['Diameter']:.2f}")
                print(f"   Circumference: {item['Circumference']:.2f}")
                print(f"   Area: {item['Area']:.2f}\n")
            else:
                print(
                    f"{i}. {item['Shape']} {item['Calculation']}: {item['Result']:.2f}")

        print("\nGoodbye!")
        break

