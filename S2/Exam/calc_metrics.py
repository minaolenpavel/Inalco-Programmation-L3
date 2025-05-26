import utils


def longueur_moyenne(path:str) -> float:
    """
    Renvoie la longueur moyenne des phrases de l'article
    """
    article = utils.import_csv(path)
    # Dans l'algorithme ci-dessous on va regarder l'ID de chaque sous-liste que l'on traite et on verifie à quel phrase elle appartient
    # De cette manière on peut déterminer les mots de chaque phrase et donc, les compter
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
    """
    Renvoie la liste des cinq lemmes de plus de 3 caractères les plus fréquents
    """
    article = utils.import_csv(path)
    # Selon la structure de données, on ne garde que l'index 2, qui correspond aux lemmes
    lemmes_list = [x[2] for x in article]
    lemmes_count = {}
    for l in lemmes_list:
        if l in lemmes_count.keys():
            lemmes_count[l] += 1
        else:
            lemmes_count[l] = 1
    return [x[0] for x in sorted((item for item in lemmes_count.items() if len(item[0])>3), key=lambda x :x[1], reverse=True)[:5]] 

def noms_propres(path:str) -> list:
    """
    Renvoie la liste de tous les noms propres de l'article
    """
    article = utils.import_csv(path)
    ens = [x[2] for x in article if x[1] == "PROPN"]
    return ens



if __name__ == "__main__":
    print(longueur_moyenne("Exam/serbie_rfi.csv"))
    print(cinq_lemmes("Exam/serbie_rfi.csv"))
    print(noms_propres("Exam/serbie_rfi.csv"))


