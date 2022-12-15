<!-- GETTING STARTED -->
## Getting Started

Ce projet est à un but éducatif et donc potentiellement instable merci de ne pas tenter de le déployer en public.

### Prérequis

Ceci est une liste des étapes à suivre pour l'installation et le bon fonctionnement du site.

* Cloner la repo
  ```sh
  git clone https://github.com/Altaryss/pokedex-py.git
  ```
 
### Installation

1. Environnement Virtuel (Optionnel)
   ```sh
   py -m venv env
   ./env/Scripts/activate
   ```

2. Installation des dépendances
   ```sh
   pip install -r requirements.txt
   ```
3. Configuration du projet
   ```sh
   cd ./web
   py manage.py tailwind update
   ```
4. Démarrer le serveur
   ```sh
    py manage.py runserver
   ```