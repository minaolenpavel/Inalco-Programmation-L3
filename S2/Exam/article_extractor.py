from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException, TimeoutException
import time
import os


def scrap_article(url:str):
    service = Service(executable_path=r"C:\Program Files (x86)\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    #options.add_argument("--headless")
    options.add_argument("--disable-cookies")
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    driver = webdriver.Firefox(service=service, options=options)
    
    driver.get(url)
    xpath = ""
    if "lemonde.fr" in url:
        xpath = "/html/body/div[10]/div/footer/button"
    elif "rfi.fr" in url:
        xpath = '//*[@id="didomi-notice-agree-button"]'
    elif "leparisien.fr" in url:
        xpath = '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[3]/button'
    time.sleep(2)
    accepter = driver.find_element(By.XPATH, xpath)
    accepter.click()

    # Supposition selon laquelle le titre est forcément un <h1> avec 'title' dans le nom de la classe
    title = driver.find_element(By.XPATH, "//h1[contains(@class, 'title')]")
    print(title.text)
    # Logique selon laquelle tout le text de l'article est dans une balise <p>
    text = driver.find_elements(By.TAG_NAME, "p")
    for i in text:
        print(i.text)
    # Ces deux suppositions ont été vérifiées pour les sites d'articles supporté par le scrapper.

    driver.close()

scrap_article("https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es")
#scrap_article("https://www.leparisien.fr/loiret-45/cette-ville-du-loiret-met-en-vente-une-maisona-0-euro-25-04-2025-KLRQ5QUNUJHUXGY5BADFPZGBWY.php")
#scrap_article("https://www.rfi.fr/en/international/20250524-macron-heads-to-vietnam-as-france-seeks-bigger-role-in-indo-pacific")
#scrap_article("https://www.lemonde.fr/international/article/2025/04/15/manifestations-en-serbie-les-etudiants-bloquent-la-radio-television-publique_6596235_3210.html")