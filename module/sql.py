import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraping"
)
cursor = conn.cursor()


def inserer_utilisateur(nom, desc=None, loca=None, prop=None, meti=None, entre=None, expe_date=None, ecole=None,
                        form=None, form_date=None):
    try:
        cursor.execute(
            "INSERT INTO utilisateur (nom, description, localisation, propos, metier, entreprise, expe_date, ecole, formation, formation_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (nom, desc, loca, prop, meti, entre, expe_date, ecole, form, form_date))
        conn.commit()
        print("Les données de l'utilisateur ont été inscrites")
    except Exception as e:
        print("Echec de l'insertion utilisateur, ", e)


def afficher_utilisateurs():
    cursor.execute("SELECT * FROM utilisateur")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
