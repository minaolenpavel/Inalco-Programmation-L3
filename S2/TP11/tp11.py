import spacy, csv
from utils11 import *

def load_txt(path:str) -> str:
    """
    Ouvre un fichier .txt et renvoie le contenu sous forme d'une chaine de caractères 
    """
    article = []
    with open(path, mode="r", encoding="utf-8") as file:
        for line in file:
            article.append(line.strip())
    article = " ".join(article)
    return article

def load_tsv(path:str) -> list:
    """
    Ouvre un fichier .tsv
    """
    loaded_tsv = []
    with open(path, encoding='utf-8', mode='r') as tsv_file:
        reader = csv.reader(tsv_file, delimiter="\t")
        for row in reader:
            loaded_tsv.append(row)
    return loaded_tsv

def write_tsv(annotations:list, path:str, delimiter="\t") -> None:
    """
    Ecrit les annotations de Spacy dans un fichier .tsv
    """
    with  open(path, encoding='utf-8', mode="w", newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter=delimiter, lineterminator='\n')
        for a in annotations:
            writer.writerow(a)

def annotate_text(text:str) -> list:
    """
    Utilise Spacy pour annoter le corpus et renvoie les entités nommées
    """
    nlp = spacy.load("fr_core_news_md")
    doc = nlp(text)
    annotations = []
    for ent in doc.ents:
        annotation = (ent.text, ent.label_)
        annotations.append(annotation)
    return annotations

def calc_precision(binary_class:dict) -> float:
    """
    Calcule la précision arrondie à deux décimales
    """
    precision = binary_class["TP"]/(binary_class["FP"]+binary_class["TP"])
    return round(precision, 2)

def calc_recall(binary_class:dict) -> float:
    """
    Calcule le rappel arrondi à deux décimales
    """
    recall = binary_class["TP"]/(binary_class["TP"]+binary_class["FN"])
    return round(recall, 2)

def calc_fmeasure(binary_class:dict) -> float:
    """
    Calcule la f-mesure arrondie à deux décimales
    """
    precision:float = calc_precision(binary_class)
    recall:float = calc_recall(binary_class)
    fmeasure = (2*precision*recall)/(precision+recall)
    return round(fmeasure, 2)

def count_binary_class(results:list) -> dict:
    """
    Fonction qui compte le nombre de TP, FP, FN.
    """
    def print_data(results:list):
        for i, (manual, auto) in enumerate(results):
            print(f"{i:03d}: MANUAL={manual} | AUTO={auto}")
    
    true_pos_list:list = [x for x in results if x[0] is not None and x[1] is not None]
    false_pos:int = len([x for x in results if x[0] is None])
    true_pos:int = 0
    for x in true_pos_list:
        if x[0][1].strip().lower() == x[1][1].strip().lower():
            true_pos+=1
        else:
            false_pos+=1
    false_neg:int = len([x for x in results if x[1] is None])
    return {
        "TP" : true_pos,
        "FP" : false_pos,
        "FN" : false_neg
    }

def match_tokens(annotations_manuelles:list, annotations_auto:list) -> list:
    """
    Fais des paires d'annotation auto et manuelles
    """
    list_tokens = []
    auto_copy = annotations_auto.copy()
    for am in annotations_manuelles:
        for i, aa in enumerate(auto_copy):
            if am[0].strip().lower() == aa[0].strip().lower():
                list_tokens.append((am, aa))
                auto_copy.pop(i)
                break
        else:
            list_tokens.append((am, None))
    for aa in auto_copy:
        list_tokens.append((None, aa))
    return list_tokens

def write_mistakes(corrigee:list) -> None:
    mistakes = []
    for i in corrigee:
        if i[-1] != "TP":
            mistakes.append(i)
    write_tsv(mistakes, "errors.csv", ";")



if __name__ == "__main__":
    text = load_txt("article.txt") 
    annotations_auto = annotate_text(text)
    write_tsv(annotations_auto, "annotations_automatiques.tsv")
    annotations_manuelles = load_tsv("annotations_manuelles.tsv")
    list_tokens = match_tokens(annotations_manuelles, annotations_auto)
    binary_class = count_binary_class(list_tokens)
    print(binary_class)
    print(calc_precision(binary_class))
    print(calc_recall(binary_class))
    print(calc_fmeasure(binary_class))
