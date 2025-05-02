import spacy, csv
from models import *
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

def create_annotation(annotation_manuelle:list, annotation_auto:str)-> Annotation:
    annotation = Annotation(annotation_manuelle[0], 
                            annotation_auto[0], 
                            annotation_manuelle[1], 
                            annotation_auto[1])
    return annotation

def match_tokens(annotations_manuelles:list, annotations_auto:list) -> list:
    final_list = []
    orphelins_manuels = []
    orphelins_auto = []
    for manuelle, auto in zip_longest(annotations_manuelles, annotations_auto):
        # Les listes peuvent être de longueurs différentes
        # Donc si in élément est None, il devient orphelin, félicitations à lui.
        if manuelle is None:
            orphelins_auto.append(auto)
            continue
        elif auto is None:
            orphelins_manuels.append(manuelle)
            continue
        if manuelle[0].lower() == auto[0].lower():
            final_list.append(create_annotation(manuelle, auto))
        else:
            max_str = max(manuelle[0], auto[0], key=len)
            min_str = min(manuelle[0], auto[0], key=len)
            if min_str in max_str:
                final_list.append(create_annotation(manuelle, auto))
            else:
                if is_substring_in_list(manuelle[0], orphelins_auto):
                    index:tuple = find_substring_index(manuelle[0], orphelins_auto)
                    pair = orphelins_auto.pop(index[0])
                    final_list.append(create_annotation(manuelle, pair))
                elif is_substring_in_list(auto[0], orphelins_manuels):
                    index:tuple = find_substring_index(auto[0], orphelins_manuels)
                    pair = orphelins_manuels.pop(index[0])
                    final_list.append(create_annotation(auto, pair))
                else:
                    orphelins_auto.append(auto)
                    orphelins_manuels.append(manuelle)
    print("orphelins auto", orphelins_auto)
    print()
    print("orphelins manuels", orphelins_manuels)
    print()
    return final_list


if __name__ == "__main__":
    #text = load_article("article.txt") 
    #annotations_automatiques = annotate_text(text)
    #write_annotations(annotations_automatiques)
    annotations_auto = load_tsv("annotations_automatiques.tsv")
    annotations_manuelles = load_tsv("annotations_manuelles.tsv")
    test = match_tokens(annotations_manuelles, annotations_auto)
    for i in test:
        print(i)
    