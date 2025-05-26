import utils


def longueur_moyenne(path:str) -> float:
    article = utils.import_csv(path)
    word_per_phrase = []
    count = 0
    current_id = article[0][-1]
    for p in article:
        if current_id == p[-1]:
            count += 1
        else:
            current_id = p[-1]
            word_per_phrase.append(count)
            count = 1
    return sum(word_per_phrase)/len(word_per_phrase)

def cinq_lemmes(path:str) -> list:
    article = utils.import_csv(path)
    lemmes_list = [x[2] for x in article]
    lemmes_count = {}
    for l in lemmes_list:
        if l in lemmes_count.keys():
            lemmes_count[l] += 1
        else:
            lemmes_count[l] = 1
    return [x[0] for x in sorted((item for item in lemmes_count.items() if len(item[0])>3), key=lambda x :x[1], reverse=True)[:5]] 

def noms_propres(path:str) -> list:
    article = utils.import_csv(path)
    ens = [x[2] for x in article if x[1] == "PROPN"]
    return ens



if __name__ == "__main__":
    #longueur = longueur_moyenne("Exam/serbie_rfi.csv")
    #print(longueur)
    #print(cinq_lemmes("Exam/serbie_rfi.csv"))
    noms_propres("Exam/serbie_rfi.csv")


