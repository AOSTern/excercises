# %%
def commands(binary_str):
    code = {"0": "wink", "1": "double blink", "2": "close your eyes", "3": "jump"}
    response = []
    binary_str = binary_str[::-1]
    for index, number in enumerate(binary_str):
        if number == "1":
            if index == 4:
                break
            response.append(code[str(index)])
    if len(binary_str) <= 4:
        return response[::-1]
    elif binary_str[4] == "1":
        return response[::-1]
    return response


# %%
