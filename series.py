def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    slice_num = len(series)
    counter = 0
    slices = []
    while counter < slice_num:
        if len(series[counter:length]) < length - counter:
            break
        slices.append(series[counter:length])
        counter += 1
        length += 1
    return slices
