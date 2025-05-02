import spacy, csv
from utils11 import *
from itertools import zip_longest

def load_article(path:str) -> list:
    article = []
    with open(path, mode="r", encoding="utf-8") as file:
        for line in file:
            article.append(line.strip())
    article = " ".join(article)
    return article

def load_tsv(path:str) -> list:
    loaded_tsv = []
    with open(path, encoding='utf-8', mode='r') as tsv_file:
        reader = csv.reader(tsv_file, delimiter="\t")
        for row in reader:
            loaded_tsv.append(row)
    return loaded_tsv

def write_annotations(annotations:list) -> None:
    with  open("annotations_automatiques.tsv", encoding='utf-8', mode="w", newline='') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        for a in annotations:
            writer.writerow(a)

def annotate_text(text:str) -> list:
    nlp = spacy.load("fr_core_news_md")
    doc = nlp(text)
    annotations = []
    for ent in doc.ents:
        annotation = (ent.text, ent.label_)
        annotations.append(annotation)
    return annotations

def calc_precision() -> float:
    pass

def calc_recall() -> float:
    pass

def calc_fmeasure() -> float:
    pass

def count_binary_class(results:list) -> dict:
    """
    Fonction qui compte le nombre de TP, FP, FN.
    """
    true_pos:int = len([x for x in results if x[0] is not None and x[1] is not None])
    false_pos:int = len([x for x in results if x[0] is None])
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


if __name__ == "__main__":
    #text = load_article("article.txt") 
    #annotations_automatiques = annotate_text(text)
    #write_annotations(annotations_automatiques)
    annotations_auto = load_tsv("annotations_automatiques.tsv")
    annotations_manuelles = load_tsv("annotations_manuelles.tsv")
    test = match_tokens(annotations_manuelles, annotations_auto)
    binary_classes = count_binary_class(test)