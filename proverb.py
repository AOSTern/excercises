def proverb(*args, qualifier=None):
    words = []
    if args == ():
        return words
    if qualifier == None:
        words.append(f"And all for the want of a {args[0]}.")
    else:
        words.append(f"And all for the want of a {qualifier} {args[0]}.")
    count = len(args)
    if len(args) > 1:
        while count >= 2:
            words.append(f"For want of a {args[count-2]} the {args[count-1]} was lost.")
            count -= 1
    return words[::-1]
