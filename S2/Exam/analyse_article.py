import spacy, time, re, article_extractor
from joblib import Memory
from models import *
# Prérequis pour cache les resultats de Spacy et rendre l'execution un peu plus rapide
memory = Memory(location="Exam/.spacy_cache", verbose=0)
nlp = spacy.load("fr_core_news_md")

@memory.cache
def annotate_phrase(phrase:str):
    """
    Utilise spacy pour taguer la phrase. Utilise un cache pour améliorer la performance et limiter le temps d'execution
    """
    return nlp(phrase)

def split_sentences(text:str) -> list:
    """
    Sépare un article en phrases, selon l'expression regex ci-dessous
    """
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    return re.split(pattern, text)

def tokenize_phrase(phrase:str) -> Phrase:
    """
    Formalise la phrase d'entrée en tokens avec spacy ainsi que les classes de models.py
    """
    #phrase = "Crise politique en Serbie: des universitaires lancent une pétition pour des législatives anticipées"
    doc = annotate_phrase(phrase)
    tokenized_phrase = []
    for t in doc:
        #print(t.text, t.lemma_, t.pos_)
        token = Token(t)
        tokenized_phrase.append(token)
    phrase = Phrase(tokenized_phrase)
    print(phrase.ID)
    return phrase
    

if __name__ == "__main__":
    start = time.time()
    url = "https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es"
    article = article_extractor.scrap_article(url)
    article = split_sentences(article)
    tokenized_phrases_article = []
    for p in article:
        phrase = tokenize_phrase(p)
    tokenized_article = Article(url, tokenized_phrases_article)
    end = time.time()
    breakpoint()
    print(end-start)
