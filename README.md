# study-assistant

[![CI](https://github.com/roastytoasty777/study-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/roastytoasty777/study-assistant/actions/workflows/ci.yml)

Un assistant d'étude qui répond à tes questions à partir de **tes propres documents** (cours, notes, documentation) et cite ses sources.

> Projet en cours de construction.

## Principe

Ce projet utilise la technique du **RAG** (*Retrieval-Augmented Generation*) :

1. Les documents sont découpés en petits passages.
2. Quand tu poses une question, le programme retrouve les passages les plus pertinents.
3. Un modèle de langage rédige la réponse à partir de ces passages et indique de quel document elle vient.

## Objectifs

- Fonctionne sur n'importe quel dossier de documents : il suffit de changer de dossier pour changer de sujet.
- Réponses toujours accompagnées de leurs sources.
- Qualité mesurée sur un jeu de questions de référence, avec les résultats dans ce README.
- Documents personnels gardés en local : le dossier `private/` n'est jamais envoyé sur GitHub.

## Avancement

- [x] Création du repo
- [ ] Choix du corpus de démonstration
- [ ] Chargement et découpage des documents
- [ ] Recherche par similarité
- [ ] Génération des réponses avec citations
- [ ] Évaluation de la qualité
- [ ] Démo en ligne

## Technologies

Python, Pydantic, pytest, GitHub Actions. D'autres outils seront ajoutés au fil du projet.