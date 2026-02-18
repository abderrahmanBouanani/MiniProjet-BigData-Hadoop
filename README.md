# Mini-Projet Big Data : Pipeline Hadoop

Ce dépôt contient l'infrastructure et le code source pour la "Conception et mise en œuvre d'une mini-chaîne Big Data basée sur Hadoop".

## 📌 État d'avancement

* **Étape 1 : Infrastructure & HDFS** (Réalisé par *Membre 1*)
* Environnement Dockerisé (Hadoop NameNode + DataNode).
* Service HDFS et YARN opérationnels.


* Arborescence stricte créée dans HDFS : `/user/hadoopuser/project/`.





## Démarrage Rapide (Pour toute l'équipe)

1. **Cloner le projet :**
```bash
git clone https://github.com/VOTRE_USER/MiniProjet-BigData-Hadoop.git
cd MiniProjet-BigData-Hadoop

```


2. **Lancer l'environnement :**
```bash
docker-compose up -d

```


3. **Vérifier l'accès :**
* Interface Web HDFS : [http://localhost:9870](https://www.google.com/search?q=http://localhost:9870)
* Vérifier les dossiers HDFS :
```bash
docker exec -it hadoop-master hdfs dfs -ls -R /user/hadoopuser/project/

```





---

## Répartition des Tâches (To-Do List)

### Membre 2 : Ingestion de Logs (Apache Flume)

**Objectif :** Simuler et ingérer des logs en temps réel.

* [ ] Créer un script Python (`scripts/generate_logs.py`) pour générer des logs aléatoires.


* [ ] Configurer l'agent Flume (`config/flume.conf`) :
* 
**Source :** `exec` (commande qui lance le script python).


* 
**Channel :** `memory`.


* 
**Sink :** `HDFS`.




* [ ] **Livrable :** Les logs doivent apparaître dans `/user/hadoopuser/project/logs`.



### Membre 3 : Ingestion Base de Données (Apache Sqoop)

**Objectif :** Importer des données relationnelles structurées.

* [ ] Configurer un conteneur MySQL (ajouter au `docker-compose.yml` ou installer localement).
* [ ] Créer une table avec des données de test.
* [ ] Exécuter l'import Sqoop vers `/user/hadoopuser/project/db_data`  avec :


* Un séparateur personnalisé.


* Une clause `WHERE` pour filtrer les données.


* Utiliser au moins 2 mappers (`-m 2`).





### Membre 4 : Traitement (MapReduce / Hadoop Streaming)

**Objectif :** Analyser les données ingérées.

* [ ] Développer `scripts/mapper.py` et `scripts/reducer.py`.
* [ ] Logique suggérée : WordCount sur les logs ou comptage par catégorie.


* [ ] Lancer le job avec **Hadoop Streaming**.


* [ ] **Livrable :** Les résultats doivent être stockés dans `/user/hadoopuser/project/output`.



### Membre 5 : Analyse & Rapport

**Objectif :** Interprétation et consolidation.

* [ ] Récupérer les fichiers de sortie depuis HDFS (`hdfs dfs -get ...`).
* [ ] Créer un script de visualisation (graphes) ou analyser les données.
* [ ] **Livrable :** Rédaction du rapport final (Word/PDF) incluant l'architecture, les codes, et l'interprétation des résultats.



---

## Structure du Projet

```text
├── config/             # Fichiers de configuration (flume.conf, etc.)
├── scripts/            # Scripts Python (logs, mapper, reducer)
├── sql/                # Scripts de création de table MySQL
├── data_local/         # Données de test (ignoré par git)
├── docker-compose.yml  # Configuration de l'infrastructure
└── README.md           # Documentation du projet

```

## Consignes de Collaboration (Git)

1. Ne travaillez jamais directement sur la branche `main`.
2. Créez une branche pour votre tâche : `git checkout -b feature/flume-ingestion`.
3. Faites vos commits et poussez votre branche.
4. Créez une **Pull Request** quand votre partie est prête à être testée par le Membre 1.