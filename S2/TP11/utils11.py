import csv

def correct_tsv(path:str) -> None:
    file_list = []
    with open(path, encoding='utf-8', mode="r") as tsv_file:
        for line in tsv_file:
            line = line.strip()
            file_list.append((line[:-3].strip(), line[-3:]))
    with open(path, encoding='utf-8', mode='w') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t', lineterminator='\n')
        for l in file_list:
            writer.writerow(l)

if __name__ == "__main__":
    correct_tsv("annotations_manuelles.tsv")