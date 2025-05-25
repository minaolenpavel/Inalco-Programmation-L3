import utils


def longueur_moyenne(article:list):
    phrases_str = []
    current_phrase = ""
    current_id = article[0][-1]
    for i, p in enumerate(article):
        if p[-1] == current_id:
            if current_phrase.endswith("'") or current_phrase.endswith("’") or current_phrase.endswith("("):
                current_phrase+=p[0]
            elif any(punct in p[0] for punct in [".",","," ",")","%"]):
                current_phrase+=p[0]
            else:
                current_phrase+=f" {p[0]}"
        else:
            phrases_str.append(current_phrase.strip())
            current_id = p[-1]
            current_phrase = p[0]
    print(phrases_str)


if __name__ == "__main__":
    article = utils.import_csv("Exam/serbie_rfi.csv")
    
    longueur_moyenne(article)


