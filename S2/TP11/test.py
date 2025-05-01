from tp11 import * 

manuelles = load_tsv("annotations_manuelles.tsv")
automatiques = load_tsv("annotations_automatiques.tsv")

for am, aa in zip(manuelles, automatiques):
    print(am, aa)