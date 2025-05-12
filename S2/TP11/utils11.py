"""
Fichier qui m'a aidé à faire certaines tâches plus facilement pour finir ce TP.
"""
import csv

def correct_tsv(path:str, delimiter:str="\t") -> None:
    """
    Corrige les TSV pour que les colonnes soient bien alignées.
    """
    file_list = []
    with open(path, encoding='utf-8', mode="r") as tsv_file:
        for line in tsv_file:
            line = line.strip()
            file_list.append((line[:-4].strip(), line[-4:].strip()))
    with open(path, encoding='utf-8', mode='w') as tsv_file:
        writer = csv.writer(tsv_file, delimiter=delimiter, lineterminator='\n')
        for l in file_list:
            writer.writerow(l)

def is_substring_in_list(target:str, double_list:list) -> bool:
    """
    Répond à la question 'est-ce que le mot est dans une des sous-listes de cette liste ?'
    """
    return any(target in s for sublist in double_list for s in sublist)

def find_substring_index(target, double_list:list) -> tuple:
    """
    Renvoie un tuple contenant en [0] l'index de la sous-liste et en [1] l'index dans la sous-liste.
    """
    for i, sublist in enumerate(double_list):
        for j, s in enumerate(sublist):
            if target in s:
                return (i, j)
    return None 


if __name__ == "__main__":
    correct_tsv("errors.tsv")