def egalite(l:list): 
    first = l[0]
    l_bool = [True if x == first else False for x in l ]
    return all(l_bool)