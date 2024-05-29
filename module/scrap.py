from bs4 import BeautifulSoup

def scrap_profil(driver):
    global soup, name, apropos, expe_metier, expe_entreprise, expe_date, localisation
    print("--- Scraping en cours ---")

    try:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
    except Exception as e:
        print("Erreur sur la récupération de la page, ", e)
        pass

    # récupération du nom complet et de la localisation
    try:
        name = soup.find("h1").getText().strip()
        localisation = soup.find("div", class_="not-first-middot").find("span").getText().strip()
    except Exception as e:
        print("Erreur sur le scrap name, localisation, ", e)

    # récupération de la description
    try:
        description = soup.find("h2", class_="top-card-layout__headline break-words font-sans text-md leading-open text-color-text").getText().strip()
    except Exception as e:
        print("Erreur sur le scrap description, ", e)
        description = None

    #récupération du A propos
    try:
        apropos = soup.find("section", attrs={"data-section": "summary"})
        apropos = apropos.findChild("p").get_text().strip()
    except Exception as e:
        print("L'utilisateur n'a pas de A propos", e)
        apropos = None

    # récupération de la derniere expérience pro
    try:
        experiences = soup.find("section", attrs={"data-section": "experience"})
        if experiences.find("li", class_="experience_group"):
            expe_entreprise = experiences.find("", class_="experience-group-header__company text-[18px] font-bold text-color-text")
        else:
            expe_entreprise = experiences.find("span", class_="experience-item__subtitle").getText().strip()

        expe_metier = experiences.find("span", class_="experience-item__title").getText().strip()
        expe_date = experiences.find("span", class_="date-range text-color-text-secondary font-sans text-md leading-open font-regular").find_all("time")
        expe_date = [date.get_text() for date in expe_date]
        expe_date = " - ".join(expe_date)
    except Exception as e:
        print("L'utilisateur n'a pas d'expérience pro, ", e)
        expe_date = None
        expe_entreprise = None
        expe_metier = None

    # récupération de la derniere formation
    try:
        section_formation = soup.find("section", attrs={"data-section": "educationsDetails"})
        form_ecole = section_formation.find("h3").get_text().strip()
        form_formation = section_formation.find("h4").get_text().strip()
        form_date = section_formation.find("span", class_="date-range text-color-text-secondary font-sans text-md leading-open font-regular").get_text().strip()

    except Exception as e:
        print("L'utilisateur n'a pas de formation, ", e)
        form_date = None
        form_ecole = None
        form_formation = None

    return name, description, localisation, apropos, expe_metier, expe_entreprise, expe_date, form_ecole, form_formation, form_date

# Si la page utilisateur nécessite un de se connecter
def page_flou(driver):
    try:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
    except Exception as e:
        print("Erreur sur la récupération de la page, ", e)
        pass

    try:
        if soup.find("div", class_="blurred-overlay w-screen h-screen relative !w-full !h-full  experience-education__list"):
            return True
    except:
        pass

