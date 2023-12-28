# %%
import re


def flatten(iterable):
    fl = []
    flat = str(iterable)
    flattened = re.sub(r"\[", "", flat)
    flattened = re.sub(r"\]", "", flattened)
    flattened = re.sub(r"None,", "", flattened)
    flattened = re.sub(r"None", "", flattened)
    flattened = flattened.strip()
    flattened = flattened.rstrip(",")
    flattened = flattened.split(",")
    if flattened == [""]:
        return []
    else:
        for item in flattened:
            fl.append(int(item))
    return fl


# %%
