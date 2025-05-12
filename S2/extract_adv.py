import spacy, random
from spacy.matcher import Matcher

def gen_random() -> int:
    return random.randint(10000, 20000)

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

def annotate_text_adv(text:str) -> list:
    """
    Utilise Spacy pour annoter le corpus et renvoie les entités nommées
    """
    nlp = spacy.load("fr_core_news_md")
    doc = nlp(text)
    return doc

def count_adv(annotations:list) -> dict:
    adverbs = [token.text for token in annotations if token.pos_ =="ADV"]
    adverbs_sorted = {}
    for a in adverbs:
        if a.lower() not in adverbs_sorted.keys():
            adverbs_sorted[a.lower()] = 1
        else:
            adverbs_sorted[a.lower()]+=1
    return dict(sorted(adverbs_sorted.items(), key=lambda a: a[1], reverse=True))

def adv_plus_adj(text:str):
    nlp = spacy.load("fr_core_news_md")
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)
    pattern = [{"LOWER": "plus"}, {"POS": "ADJ"}]
    matcher.add("plus_adj", [pattern])
    matches = matcher(doc)
    collocation_counts = {}
    
    for match_id, start, end in matches:
        collocation = doc[start:end].text.lower()
        if collocation in collocation_counts:
            collocation_counts[collocation] += 1
        else:
            collocation_counts[collocation] = 1

    return dict(sorted(collocation_counts.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    text = load_txt("Madame_Bovary.txt")
    #adverbs = annotate_text_adv(text)
    #adverbs_ranked = count_adv(adverbs)
    #print(adverbs_ranked)
    adv_plus_adj(text)

