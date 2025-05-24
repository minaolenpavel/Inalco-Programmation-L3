# first line: 8
@memory.cache
def annotate_phrase(phrase:str):
    """
    Utilise spacy pour taguer la phrase. Utilise un cache pour améliorer la performance et limiter le temps d'execution
    """
    return nlp(phrase)
