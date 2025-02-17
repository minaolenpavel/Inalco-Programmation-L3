def premier_dernier(l:list):
    print(f"{l[0]}\t{l[-1]}")

def meme_longueur(l1:list, l2:list):
    if len(l1) == len(l2):
        print("même longueur")
    else:
        print("pas la même longueur")