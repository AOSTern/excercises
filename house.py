import re


def recite(start_verse, end_verse):
    poem = [
        "This is",
        "the horse and the hound and the horn that belonged to",
        "the farmer sowing his corn that kept",
        "the rooster that crowed in the morn that woke",
        "the priest all shaven and shorn that married",
        "the man all tattered and torn that kissed",
        "the maiden all forlorn that milked",
        "the cow with the crumpled horn that tossed",
        "the dog that worried",
        "the cat that killed",
        "the rat that ate",
        "the malt that lay in",
        "the house that Jack built.",
    ]
    poem_two = poem[::-1]
    diference = end_verse - start_verse
    count = 0
    two = ""
    final = []
    while count <= diference:
        result = []
        temporal = ""
        result.append(poem_two[-1])
        two = str(poem_two[(start_verse - 1 + count) :: -1])
        two = re.sub(",", "", two)
        result.append(two)
        count = count + 1
        temporal = " ".join(result)
        patn = re.sub(r"[\([{','})\]]", "", temporal)
        final.append(patn)
    return final
