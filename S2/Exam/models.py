import csv, json

class Token:
    def __init__(self, token):
        self.lemma = token.lemma_.strip()
        self.pos_tag = token.pos_.strip()
        self.form = token.text.strip()
    
    def to_dict(self) -> dict :
        return {"lemma":self.lemma, "pos_tag":self.pos_tag, "form":self.form}

class Phrase:
    _id = -1
    def __init__(self, tokenized_phrase:list):
        Phrase._id +=1
        self.ID = Phrase._id
        self.tokens = tokenized_phrase
    
    def to_dict(self) -> dict :
        return {"ID":self.ID, "tokens":[t.to_dict for t in self.tokens]}

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
    
    def to_dict(self) -> dict:
        return {'url': self.URL, "phrases": [p.to_dict for p in self.phrases]}
    
    def to_json(self, path:str) -> None:
        data = self.to_dict()
        with open(path, encoding='utf-8', mode ="w") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


    