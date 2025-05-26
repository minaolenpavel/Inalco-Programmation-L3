import spacy, re, article_extractor, utils
from joblib import Memory
from models import *
# Prérequis pour mettre en cache les resultats de Spacy et rendre l'execution un peu plus rapide (sur les éxecution avec la même entrée)
memory = Memory(location="Exam/.spacy_cache", verbose=0)
nlp = spacy.load("fr_core_news_md")

@memory.cache
def annotate_phrase(phrase:str):
    """
    Utilise spacy pour taguer la phrase. Utilise un cache pour améliorer la performance et limiter le temps d'execution
    """
    return nlp(phrase)

def tokenize_phrase(phrase:str) -> Phrase:
    """
    Formalise la phrase d'entrée en tokens avec spacy ainsi que les classes de models.py
    """
    doc = annotate_phrase(phrase)
    tokenized_phrase = []
    for t in doc:
        #print(t.text, t.lemma_, t.pos_)
        token = Token(t)
        tokenized_phrase.append(token)
    phrase = Phrase(tokenized_phrase)
    print(phrase.ID)
    return phrase

def tokenize_article(article:list) -> Article:
    """
    Tokenize un article grâce à la fonction qui tokenize une phrase.
    """
    tokenized_phrases_article = []
    for p in article:
        tokenized_phrase = tokenize_phrase(p)
        tokenized_phrases_article.append(tokenized_phrase)
    tokenized_article = Article(url, tokenized_phrases_article)
    return tokenized_article

if __name__ == "__main__":
    stopwatch = utils.Stopwatch()
    stopwatch.start()
    url = "https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es"
    article = article_extractor.scrap_article(url)
    article = utils.split_sentences(article)
    tokenized_article = tokenize_article(article)
    tokenized_article.to_json("serbie_rfi.json")
    
    stopwatch.stop()
    print(stopwatch.total_time)
