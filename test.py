def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError and int != 1 and int != 2 and int !=3 and int != 4:
            print("Invalid input.")


input_int("hej")