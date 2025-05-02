import spacy, csv
from models import *
from utils11 import *

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

def match_tokens(annotations1:list, annotations2:list) -> list:
    size = 0
    if len(annotations1) > len(annotations2):
        size = len(annotations1)
    else:
        size = len(annotations2)
    final_list = []
    for i in range(size):
        print(annotations1[i], annotations2[i])
        if len(annotations1[i][0]) != len(annotations2[i][0]):
            max_str = max(annotations1[i][0], annotations2[i][0], key=len)
            min_str = min(annotations1[i][0], annotations2[i][0], key=len)
            if min_str in max_str:
                print(min_str,"is in", max_str)

if __name__ == "__main__":
    #text = load_article("article.txt") 
    #annotations_automatiques = annotate_text(text)
    #write_annotations(annotations_automatiques)
    correct_tsv("annotations_manuelles.tsv")
    annotations_automatiques = load_tsv("annotations_automatiques.tsv")
    annotations_manuelles = load_tsv("annotations_manuelles.tsv")
    match_tokens(annotations_manuelles, annotations_automatiques)