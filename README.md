rice classification
==============================

A short description of the project.

Project Organization
------------
```
├── README.md          <- The top-level README for developers using this project.
├── main.py            <- Script to run the entire pipeline
│
├── configs
│   ├── __init__.py    <- Makes configurations a Python module
│   └── config_files   <- Config files with credentials, API keys, etc., ignored by .gitignore
│   ├── parameters.py  <- Globally defined parameters used in src 
│   ├── names.py  <- Globally defined parameters used in src 
│   └── paths.py       <- Globally defined folder and file paths 
|
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── logs               <- A folder containing .log files
│
├── logger.py          <- Definition of logger
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is: the creator's initials,
│                         a number (for ordering), and a short `-` delimited description, e.g.
│                         `jqp-1.0-initial-data-exploration`.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
|
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── <>.py
│
├── tests
│   ├── __init.py__    <- Makes tests a Python module
│   └── test_basic.py  <- Basic pytest test
│
├── .gitignore         <- files to be ignored by git  

```


--------
## Installation
#### Set up a virtual environment via:

```
conda env create --file environment.yml
```

### Activate the virtual environment:

```
conda activate env_ld_bp
```

### Install the project and required packages in the activated virtual environment via:

```
python -m pip install -U pip setuptools wheel
python -m pip install -e ".[dev]"
pre-commit install
```

## Base Example
Base example of how to use this project.

## Documentation
Link to the documentation page.
