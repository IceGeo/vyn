# **MODULE R405 - Automatisation des tâches d’administration**

## VYN - View Your Network 

Auteur : 
 - [IceGeo](https://github.com/IceGeo)
 - [Wa0k](https://github.com/Wa0k)

## Sommaire

1. **[Introduction](#1)**
   + [1.1. Gestion de projet](#1_1)
   + [1.2. Objectifs du projet](#1_2)
2. **[Mise en place](#2)**
   + [2.1. Bibliothèques](#2_1)
   + [2.2. Github](#2_2)
3. **[L’application](#3)**
   + [3.1. Arborescence primaire](#3_1)
   + [3.2. Fonctionnalités principales](#3_2)
   + [3.3. Fonctionnalités secondaires](#3_3)
4. **[Sources](#4)**

# <a id="1">Introduction</a>
Notre projet se situe dans le cadre de la ressource R402 Automatisation des tâches d’administration.

L’application VYN (View Your Network) est une application web en Python permettant la gestion, la supervision et l’administration de différents équipements à travers un réseau. Cette application aura pour finalité de s'exécuter sur une machine Ubuntu qui sera accessible ici.

##  <a id="1_1">1.1. Gestion de projet</a>

Afin de se répartir au mieux la charge de travail et de s’organiser pour être les plus productifs, nous allons :
- Définir l’ensemble des fonctionnalités et les tâches associées pour s’auto-attribuer nos missions.
- Définir un ordre de priorité sur les fonctionnalités principales à mettre en place.
- Lister les bibliothèques python requises.
- Mettre en place le projet sur Github.

D’autres outils annexes comme Trello ou Mindview peuvent également être utilisés pour améliorer l’organisation en binôme du projet. Mais au vu du projet, nous allons utiliser uniquement Github.

## <a id="1_2">1.2. Objectifs du projet</a>

L’objectif d’un tel de projet est de :

- Développer des compétences en développement web via Python.
- Acquérir des connaissances sur la gestion, la supervision et l'administration de différents équipements réseau via Python.
- Apprendre à utiliser des nouvelles bibliothèques Python telles que Flask, Ansible, Napalm, Netmiko…
- Apprendre et approfondir ses connaissances en matière de gestion de projets avec Github, ce qui est un outil incontournable pour la collaboration et la gestion de versions de code.

# <a id="2">2. Mise en place</a>

## <a id="2_1">2.1. Bibliothèque</a>
|Bibliothèque |Description                                                                                                                        |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- |
|Os           |Bibliothèque de fonctionnalités système pour interagir avec le système d'exploitation                                              |
|Time         |Bibliothèque pour manipuler les dates et les temps                                                                                 |
|Flask        |Micro-framework Web Python pour développer des applications Web rapidement et facilement                                           |
|Napalm       |Bibliothèque pour la gestion de réseaux avec un support multi-vendor                                                               |
|Netmiko      |Bibliothèque pour les connexions et les automatisations réseau                                                                     |
|Re           |Bibliothèque pour la recherche et la manipulation de chaînes de caractères                                                         |
|Socket       |Bibliothèque pour la programmation de sockets réseau                                                                               |
|SQLAlchemy   |Bibliothèque pour la gestion de bases de données en Python                                                                         |
|Ansible      |Bibliothèque pour la configuration et la gestion d'infrastructures informatiques en utilisant un langage simple et compréhensible. |

## <a id="2_2">2.2 Github</a>
Nous utiliserons Github pour pouvoir gérer le versionning de notre application. Cela rendra plus simple la gestion du code de notre application et évitera les conflits de fichier.

Le repo Github correspondant au projet est accessible [ici](https://github.com/IceGeo/vyn).

# <a id="3">3. L’application</a>

## <a id="3_1">3.1. Arborescence primaire</a>

Le projet sera composé de plusieurs fichiers notamment des fichiers essentiels à Flask pour fonctionner.
```
/var/www/vyn
│── app/
│   │── __init__.py
│   │── db.py
│   │── schema.sql
│   │── app.py
│   │── static/
│   │── templates/
│   │   │── base.html
│   │   └── auth/
│   │       └── login.html
│   └── style.css
│── tests/
│   │── conftest.py
│   │── data.sql
│   │── test\_factory.py
│   │── test\_db.py
│   │── test\_auth.py
│   └── test\_blog.py
│── venv/
│── setup.py
└── MANIFEST.in
```

## <a id="3_2">3.2. Fonctionnalités principales</a>

Site web (Flask) :
- / : Page de connexion.
- /monitoring : Page de monitoring, pourra prendre des paramètres.
- /admin : Page d’administration, pourra prendre des paramètres.
- Menu hamburger pour la navigation entre les pages.

Page Racine :
- Simple page d'authentification.

Page Monitoring  :
- En fonction de ce qui est réalisable, nous souhaitons pouvoir visualiser le nombre de connexions, la charge du réseau, la charge des différents équipements du réseau, la consommation de bande passante… sous forme de graphique Grafana

Page Administration :
- La page d’administration permettrait de gérer différents équipements en ssh.

## <a id="3_3">3.3. Fonctionnalités secondaires</a>

Page Gestion de fichier :

- Client FTP (comme par exemple FileZilla).

Page Schéma :

- Visualisation en schéma de l’infrastructure du réseau / services.
- Découverte automatique de l’infrastructure du réseau.

# <a id="4">4. Sources</a>
Flask :
- Documentation officielle : [Quickstart with Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
- OpenClassrooms : [Concevez un site avec Flask](https://openclassrooms.com/fr/courses/4425066-concevez-un-site-avec-flask)
- Développer : [Introduction à flask](https://tahe.developpez.com/tutoriels-cours/python-flask-2020/?page=services-web-avec-le-framework-flask)

Ansible :
- Documentation officielle : [Ansible documentation](https://docs.ansible.com/ansible/latest/index.html)
- OpenClassrooms : [Utilisez Ansible pour automatiser vos tâches de configuration](https://openclassrooms.com/fr/courses/2035796-utilisez-ansible-pour-automatiser-vos-taches-de-configuration)
- Devopssec : [Introduction au cours complet d’Ansible](https://devopssec.fr/article/introduction-cours-complet-ansible#begin-article-section)
- Blog : [Ansible - tutoriel français](https://xavki.blog/ansible-tutoriaux-francais/)

Os :
- Documentation officielle : [Miscellaneous os interfaces](https://docs.python.org/3/library/os.html)
- Python Geeks : [Python OS Module](https://pythongeeks.org/python-os-module/)

Time :
- Documentation officielle : Time [access and conversions](https://docs.python.org/3/library/time.html)
- Realpython : [A Beginner’s Guide to the Python time Module](https://realpython.com/python-time-module/)

Napalm :
- Documentation officielle : [Napalm official documentation](https://napalm.readthedocs.io/en/latest/)

Netmiko :
- Documentation offcielle : [Working with network devices](https://pyneng.readthedocs.io/en/latest/book/18_ssh_telnet/netmiko.html)

Re :
- Documentation officielle : [Regular expression operations](https://docs.python.org/3/library/re.html)
- Realpython : [Regular Expressions: Regexes in Python (Part 1)](https://realpython.com/regex-python/)

Socket :
- Documentation officielle : [Low-level networking interface](https://docs.python.org/3/library/socket.html)
- Realpython : [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)

SQLAlchemy :
- Documentation officielle : [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/index.html)
- Realpython : [Data Management With Python, SQLite, and SQLAlchemy](https://realpython.com/python-sqlite-sqlalchemy/)

Autre :
- TechTarget : [Compare Paramiko, Netmiko and NAPALM network automation](https://www.techtarget.com/searchnetworking/tip/Network-automation-with-Python-Paramiko-Netmiko-and-NAPALM)
