def str_splitting(arg):
    arg = list(arg)
    dig = []
    tp = []
    for i in arg:
        try:
            a = int(i)
            dig.append(i)
        except:
            tp.append(i)
    return int(''.join(dig)), ''.join(tp).lstrip()

