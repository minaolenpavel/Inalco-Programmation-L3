class Token:
    def __init__(self, token):
        self.lemma = token.lemma_
        self.gram_cat = token.pos_
        self.form = token.text