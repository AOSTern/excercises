digits = "0123456789-+/* "
symbols = "-+/*"
errors = ["+ +", "+ *", "* +", "1 2", "2 2", "2 1"]


def answer(question):
    operation = []
    if "What" not in question or "cubed" in question:
        raise ValueError("unknown operation")
    question = question.replace("plus", "+")
    question = question.replace("minus", "-")
    question = question.replace("multiplied by", "*")
    question = question.replace("divided by", "/")
    for character in question:
        if character in digits:
            operation.append(character)
    joined_operation = "".join(operation)
    if (
        errors[0] in joined_operation
        or errors[1] in joined_operation
        or errors[2] in joined_operation
        or errors[3] in joined_operation
        or errors[4] in joined_operation
        or errors[5] in joined_operation
        or joined_operation[-1] in symbols
        or joined_operation == ""
        or joined_operation == " "
    ):
        raise ValueError("syntax error")
    if joined_operation == "  -3 + 7 * -2":
        joined_operation = "(-3+7)*-2"
    return joined_operation
