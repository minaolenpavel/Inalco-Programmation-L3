import utils, article_extractor, article_tokenizer, calc_metrics

def main():
    stopwatch = utils.Stopwatch()
    stopwatch.start()
    url = "https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es"
    article = article_extractor.scrap_article(url)
    article = utils.split_sentences(article)
    tokenized_article = article_tokenizer.tokenize_article(article, url)
    path = "serbie_rfi.csv"
    tokenized_article.export_csv(path)
    
    print(calc_metrics.longueur_moyenne(path))
    print(calc_metrics.cinq_lemmes(path))
    print(calc_metrics.noms_propres(path))

    stopwatch.stop()
    print(stopwatch.total_time)




if __name__ == "__main__":
    main()