from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import utils, time


def scrap_article(url:str) -> list:
    """
    Fonction qui scrappe le contenu de l'article donné en URL et renvoie les données.
    Fonctionne avec LeParisien, RFI et LeMonde.
    """
    stopwatch = utils.Stopwatch()
    stopwatch.start()
    # Initialisation de Selenium
    service = Service(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    # Mode headless pour économie de ressources et juste plus de confort
    options.add_argument("--headless")
    options.add_argument("--disable-cookies")
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox(service=service, options=options)
    # Accès à l'URL désirée
    driver.get(url)
    xpath = ""
    # Selon les sites, l'accès au bouton pour fermer le pop-up concernant les cookies va être différent
    # Ici on regarde quel site on doit scrapper pour trouver le bon Xpath afin de cliquer sur le bon bouton
    if "lemonde.fr" in url:
        xpath = "/html/body/div[10]/div/footer/button"
    elif "rfi.fr" in url:
        xpath = '//*[@id="didomi-notice-agree-button"]'
    elif "leparisien.fr" in url:
        xpath = '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[3]/button'
    time.sleep(2)
    accepter = driver.find_element(By.XPATH, xpath)
    accepter.click()

    article_text = []
    # Supposition selon laquelle le titre est forcément un <h1> avec 'title' dans le nom de la classe
    title = driver.find_element(By.XPATH, "//h1[contains(@class, 'title')]")
    article_text.append(title.text.strip())
    # Logique selon laquelle tout le text de l'article est dans une balise <p>
    text = driver.find_elements(By.TAG_NAME, "p")
    for t in text:
        article_text.append(t.text.strip())
    # Ces deux suppositions ont été vérifiées pour les sites d'articles supporté par le scrapper.

    # Fermeture du Firefox
    # En principe ce n'est pas nécessaire de le faire sur une machine personnelle mais si le script venait à être utilisé sur un serveur via un scronjob, cela pourrait très vite causer des problèmes. 
    driver.close()
    stopwatch.stop()
    print(f"l'article a été extrait en {stopwatch.total_time} secondes !")
    return " ".join(article_text)

if __name__ == "__main__":
    # Articles sample
    article = scrap_article("https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es")
    print(article)
    #article = scrap_article("https://www.leparisien.fr/loiret-45/cette-ville-du-loiret-met-en-vente-une-maisona-0-euro-25-04-2025-KLRQ5QUNUJHUXGY5BADFPZGBWY.php")
    # article = scrap_article("https://www.rfi.fr/en/international/20250524-macron-heads-to-vietnam-as-france-seeks-bigger-role-in-indo-pacific")
    # article = scrap_article("https://www.lemonde.fr/international/article/2025/04/15/manifestations-en-serbie-les-etudiants-bloquent-la-radio-television-publique_6596235_3210.html")