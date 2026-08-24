def string_check(question, valid_ans_list):
    """Checks that users enter the full world
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:


            # check if the response is the entire word
            if response == item:
                return item

            #check if its the first letter
            elif response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")

# main routine starts here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check("Do you like coffee? ", ['yes', 'no'])
choose_level = string_check("Choose a level: ", levels)