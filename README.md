dades_assemblea_clima
==============================

Anàlisi i modelatge de les dades open-source de l'Assemblea Ciutadana pel Clima de Catalunya.


## Resum
Aquest projecte conté les dades extretes sobre les propostes fetes a [l'Assemblea Ciutadana pel Clima de Catalunya](https://participa.gencat.cat/processes/assembleaclima)
S'ha realitzat un anàlisi de les dades i un posterior tractament per aplicar un model de Topic Modeling.

## Objectiu
Detectar de forma automàtica els tòpics de cada proposta i entendre quines variables fan que una proposta tingui més engagement i possibilitats de ser aprovada.

## Preprocessing
El dataset contenia moltes propostes de diferents processos participatius i ha calgut acotar-ne les dades per poder treballar únicament amb les de l'Assemblea. La majoria de columnes originals eren buides i s'ha optat per prescindir-ne. Finalment, s'han eliminat també les columnes que es consideren innecessàries per treballar amb un model de Topic Modeling, tals com id, url, etc...

## Requisits
- Pandas
- Matplotlib
- Seaborn
- ydata-profiling
- gensim

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------
