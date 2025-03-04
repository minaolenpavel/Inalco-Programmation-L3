import rectangle, disc, my_token

hauteur = int(input("hauteur: "))
largeur = int(input("largeur: "))

r = rectangle.Rectangle(hauteur, largeur)
print(r.surface())
print(r.perimetre())
print(r.square())

d = disc.Disc(5,10,80)

phrase = [
        ("Je", "je", "PRON"),
        ("déteste", "détester", "VERB"),
        ("la", "le", "DET"),
        ("comptabilité", "comptabilité", "NOUN"),
        ("financière", "financier", "ADJ"),
        (".", ".", "PUNCT")
    ]

tokens = [my_token.Token(forme, lemme, spart) for forme, lemme, spart in phrase]
for token in tokens:
    print(token.affichage()) 
