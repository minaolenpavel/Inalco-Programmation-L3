import csv, json, utils

class Token:
    def __init__(self, token):
        self.lemma = token.lemma_.strip()
        self.pos_tag = token.pos_.strip()
        self.form = token.text.strip()

class Phrase:
    _id = -1
    def __init__(self, tokenized_phrase:list):
        Phrase._id +=1
        self.ID = Phrase._id
        self.tokens = tokenized_phrase

class Article:
    def __init__(self, URL:str, phrases:list):
        self.URL = URL
        self.phrases = phrases

    def export_csv(self, path:str) -> None:
        """
        Exporte les tokens de l'article en format CSV, tel que | forme | pos_tag | lemme | id_phrase |
        """
        HEADERS = ["forme", "pos_tag", "lemme", "id_phrase"]
        with open(path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=";", quoting = csv.QUOTE_MINIMAL)
            writer.writerow(HEADERS)
            for p in self.phrases:
                for t in p.tokens:
                    writer.writerow([t.form, t.pos_tag, t.lemma, p.ID])

