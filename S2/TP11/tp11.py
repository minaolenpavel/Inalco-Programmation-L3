import spacy, csv

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
    print(loaded_tsv)

def write_annotations(annotations:list) -> None:
    with  open("TP11/annotations_automatiques.tsv", encoding='utf-8', mode="w", newline='') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
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

def calc_precision(annotations1:list, annotations2:list) -> float:
    pass


if __name__ == "__main__":
    #text = load_article("TP11/article.txt") 
    #annotations = annotate_text(text)
    #write_annotations(annotations)
    loaded_tsv = load_tsv("TP11/annotations_manuelles.tsv")