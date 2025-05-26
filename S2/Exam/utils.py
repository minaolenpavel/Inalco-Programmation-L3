import time, re, csv, json
from models import *

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._end_time = None

    def start(self):
        self._start_time = time.time()
    
    def stop(self):
        self._end_time = time.time()

    @property
    def total_time(self):
        return self._end_time - self._start_time
    

def split_sentences(text:str) -> list:
    """
    Sépare un article en phrases, selon l'expression regex ci-dessous
    """
    pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
    return re.split(pattern, text)

def import_csv(path:str) -> list:
    file = []
    with open(path, encoding='utf-8', mode='r') as csv_file:
        reader = csv.reader(csv_file, delimiter=";", quotechar='"')
        for line in csv_file:
            file.append(line.strip().split(";"))
    return file[1:]

def reform_sentences(article:list) -> list:
    phrases_str = []
    current_phrase = ""
    current_id = article[0][-1]
    for i, p in enumerate(article):
        if p[-1] == current_id:
            if current_phrase.endswith("'") or current_phrase.endswith("’") or current_phrase.endswith("("):
                current_phrase+=p[0]
            elif any(punct in p[0] for punct in [".",","," ",")","%"]):
                current_phrase+=p[0]
            else:
                current_phrase+=f" {p[0]}"
        else:
            phrases_str.append(current_phrase.strip())
            current_id = p[-1]
            current_phrase = p[0]
    return phrases_str

def json_to_article(path:str):
    article_raw = None
    with open(path, encoding='utf-8', mode='r') as json_file:
        article_raw = json.load(json_file)
    return article_raw