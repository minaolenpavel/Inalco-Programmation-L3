import spacy, time, re
from joblib import Memory
from models import *
# Prérequis pour cache les resultats de Spacy et rendre l'execution un peu plus rapide
memory = Memory(location="Exam/.spacy_cache", verbose=0)
nlp = spacy.load("fr_core_news_md")

@memory.cache
def annotate_article(article:str):
    return nlp(article)

def split_sentences(text:str) -> list:
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    return re.split(pattern, text)

def tokenize_phrase():
    phrase = "Crise politique en Serbie: des universitaires lancent une pétition pour des législatives anticipées"
    doc = annotate_article(phrase)
    tokenized_phrase = []
    for t in doc:
        print(t.text, t.lemma_, t.pos_)
        token = Token(t)
        tokenized_phrase.append(token)


    

if __name__ == "__main__":
    start = time.time()
    tokenize_phrase()
    end = time.time()
    print(end-start)
