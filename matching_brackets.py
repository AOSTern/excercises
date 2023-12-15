def is_paired(input_string):
    test_string = ""
    test_string_b = ""
    for character in input_string:
        if character in "()[]{}":
            test_string = test_string + character
    if len(test_string) % 2 != 0:
        return False
    while len(test_string) >= len(test_string_b):
        test_string = test_string.replace("[]", "")
        test_string = test_string.replace("{}", "")
        test_string = test_string.replace("()", "")
        if len(test_string) == len(test_string_b):
            break
        test_string_b = test_string
    if test_string == "":
        return True
    return False
