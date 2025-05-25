import utils


def longueur_moyenne(path:str):
    article = utils.import_csv(path)
    phrases = utils.reform_sentences(article)
    phrases_len = {}
    for p in phrases:
        phrases_len[p] = len(p)
    total_letters = sum(phrases_len.values())
    avg_length = total_letters/len(phrases_len.keys())
    print(avg_length)



if __name__ == "__main__":
    longueur_moyenne("Exam/serbie_rfi.csv")


