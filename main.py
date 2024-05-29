import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from xpath import *
from module.scrap import scrap_profil
from module.scrap import page_flou
from module.sql import inserer_utilisateur
from module.util import useragents

# page index, obligatoire avant page recherche
website = "https://www.linkedin.com/?trk=seo-authwall-base_nav-header-logo"

# inputs pour la recherche d'utilisateurs
firstname = input("prénom : ")
lastname = input("nom : ")

# délai pour chargement de page
delay = 5

# initialisation du driver chrome
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1500,750")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

def scraping():
    # Pour plus de discrétion
    user_agent = random.choice(useragents)
    options.add_argument("user_agent=" + user_agent)

    driver.get(website)

    # page de recherche utilisateurs
    driver.find_element(By.XPATH, research_page).click()
    # envoie des inputs
    time.sleep(delay)
    driver.find_element(By.XPATH, form_firstname).send_keys(firstname)
    driver.find_element(By.XPATH, form_lastname).send_keys(lastname)
    driver.find_element(By.XPATH, research_button).click()
    time.sleep(delay)

    # Si il existe plusieurs utilisateurs avec ce nom, nous scrapons alors les 3 premiers comptes
    if driver.current_url.startswith("https://www.linkedin.com/pub/"):
        lien_utilisateurs = [] # Nécessaire pour parcourir la liste d'url
        try:
            serp_page = driver.find_element(By.CLASS_NAME, "serp-page__results-list")
            pages = serp_page.find_elements(By.TAG_NAME, "a")
            # Changer la valeuss de page[] pour choisir le nombre de pages
            for page in pages[:1]:
                lien_utilisateurs.append(page.get_property("href"))
                print(page)
            for page in lien_utilisateurs:
                time.sleep(delay)
                driver.get(page)
                time.sleep(delay) # Permet le chargement de la page
                try:
                    if page_flou(driver):
                        print("Impossible de scraper le compte, un compte connecté est nécessaire")
                    else:
                        donnees_utilisateur = scrap_profil(driver)
                        inserer_utilisateur(*donnees_utilisateur)
                except Exception as e:
                    print("Erreur sur le scraping profil, ", e)
                    pass
        except Exception as e:
            print(e)
    else:
        try:
            if page_flou(driver):
                print("Impossible de scraper le compte, un compte connecté est nécessaire")
            else:
                donnees_utilisateur = scrap_profil(driver)
                inserer_utilisateur(*donnees_utilisateur)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    scraping()