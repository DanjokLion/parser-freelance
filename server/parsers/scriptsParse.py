def str_splitting(arg):
    if not arg[0].isdigit(): return 0, arg
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

