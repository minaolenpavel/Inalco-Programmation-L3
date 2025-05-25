class Token:
    def __init__(self, token):
        self.lemma = token.lemma_
        self.gram_cat = token.pos_
        self.form = token.text

class Phrase:
    _id = 0
    def __init__(self, tokenized_phrase:list):
        Phrase._id +=1
        self.ID = Phrase._id
        self.tokens = tokenized_phrase

class Article:
    def __init__(self, URL:str, phrases:list):
        self.URL = URL
        self.phrases = phrases