from flask import Flask, render_template

app = Flask("CV")

experiences = {
    0:{
        "poste": "Senior legal counsel",
        "lieu": "Suresnes",
        "employeur": "CrossKnowledge",
        "date_debut": "2014",
        "date_fin": "2020",
        "description": "Rédaction et négociation des contrats avec les clients, partenaires et auteurs (EN/FR)"
    },
    1:{
        "poste": "Juriste",
        "lieu": "Vincennes",
        "employeur": "IGN",
        "date_debut": "2009",
        "date_fin": "2014",
        "description": "Validation des contrats de la direction commerciale et de la maîtrise d'ouvrage du service public. Appui à la direction sur les questions liées à la réutilisation des informtions publiques."
    },
    2:{
        "poste": "Juriste junior",
        "lieu": "Paris, 10e",
        "employeur": "Micro Application",
        "date_debut": "2007",
        "date_fin": "2009",
        "description": "Rédaction et négociation de contrats d'édition et de distribution de logiciels"
    }
    }

formations = {
    0:{
        "nom": "Master 2 Droit de la distribution et des Contrats d'Affaires",
        "lieu": "Montpellier",
        "organisme": "Université Montpellier I",
        "date_debut": "2005",
        "date_fin": "2006",
        "description": "Depuis 1982, le DEA devenu Master « Droit de la distribution et des Contrats d’Affaires » forme des juristes hautement qualifiés dans les accords et contrats d’affaires liés à la vie de l’entreprise, particulièrement les contrats de distribution (distribution sélective, concession, franchise….). Le Master permet notamment la maîtrise des contraintes et des risques qui pèsent sur la négociation, la rédaction et l’exécution des contrats d’affaires, au travers d’une approche à la fois fondamentale (par l’initiation à la recherche que constitue le mémoire, pouvant déboucher sur une thèse universitaire), et pratique (nombreux séminaires et stage)."
    },
    1:{
        "nom": "Master 2 Droit et Informatique",
         "lieu": "Montpellier",
        "organisme": "Université Montpellier I",
        "date_debut": "2004",
        "date_fin": "2005",
        "description": "Le Master Informatique et Droit abordait à la fois le droit l'informatique et l'informatique juridique."
    },
    2:{
        "nom": "Management Général",
        "lieu": "CNIT - La Défense",
        "organisme": "ESSEC",
        "date_debut": "2016",
        "date_fin": "2017",
        "description": "Le programme Management Général a pour objectifs d'actualiser la maîtrise des outils de base en contrôle de gestion, gestion financière, marketing, logistique etc. en y intégrant les paramètres de la globalisation, d'approfondir les nouvelles techniques de gestion et d’analyse stratégique et de développer les qualités entrepreneuriales nécessaires à tout dirigeant ; enfin de synthétiser les acquis du programme à travers un projet stratégique répondant à une problématique concrète d’entreprise."
    },
    }

@app.route("/")
def home():
    return render_template("home.html", nom="CV", formations=formations, experiences=experiences)

@app.route("/formation/<int:study_id>")
def formation(study_id):
    return render_template("formation.html", nom="CV", formation=formations[study_id])

@app.route("/experience/<int:career_id>")
def experience(career_id):
    return render_template("experience.html", nom="CV", experience=experiences[career_id])

# Ce if permet de vérifier que ce fichier est celui qui est courrament exécuté. Cela permet par exemple d'éviter
# de lancer une fonction quand on importe ce fichier depuis un autre fichier.
# En python, lorsque l'on exécute un script avec la commande `python script.py`
# Le fichier `script.py` a en __name__ la valeur __main__.
if __name__ == "__main__":
    app.run(debug=True)