import time, re, csv
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