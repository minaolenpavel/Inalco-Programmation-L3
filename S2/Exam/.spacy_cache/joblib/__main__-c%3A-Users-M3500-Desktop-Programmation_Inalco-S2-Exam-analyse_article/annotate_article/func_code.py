# first line: 8
@memory.cache
def annotate_article(article:str):
    return nlp(article)
