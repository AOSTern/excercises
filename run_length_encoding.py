# %%
import re


def decode(string):
    string = string.replace(" ", "_")
    chunks = []
    chunks_two = []
    chunks_three = []
    count = 0
    love = ""
    for index, character in enumerate(string):
        if character.isdigit():
            count += 1
            continue
        if character != character.isdigit():
            chunks.append(string[index - count : index + 1])
            count = 0
    for item in chunks:
        newset = list(filter(None, re.split(r"(\d+)", item)))
        chunks_two.append(newset)
    for item in chunks_two:
        if len(item) > 1:
            chunks_three.append(int(item[0]) * item[1])
        else:
            chunks_three.append(1 * item[0])
        love = "".join(chunks_three)
        love = love.replace("_", " ")
    return love


def encode(string):
    new_string = []
    encoded = []
    string = string.replace(" ", "_")
    for index, letter in enumerate(string):
        if index == len(string) - 1:
            new_string.extend(string[index])
            break
        if letter == string[index + 1]:
            new_string.extend(letter)
            continue
        else:
            new_string.extend(letter + " ")
    mod_string = "".join(new_string)
    love = mod_string.split()
    love = [item.replace("_", " ") for item in love]
    for item in love:
        if len(item) > 1:
            encoded.append((str(len(item)) + item[0]))
        else:
            encoded.append(item[0])
    return "".join(encoded)


# %%
