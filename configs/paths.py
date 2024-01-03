"""
Example to use these configurations:
from configs import paths
print(paths.FOLDER_ROOT)
"""

from pathlib import Path

# Repository root path. Note that this line will not
# work when copy-pasted into a terminal / notebook.
FOLDER_ROOT = Path(__file__).resolve().parents[1]

FOLDER_DATA = FOLDER_ROOT / "data"
FOLDER_MODELS = FOLDER_ROOT / "models"
FOLDER_NOTEBOOKS = FOLDER_ROOT / "notebooks"
FOLDER_REPORTS = FOLDER_ROOT / "reports"
FOLDER_REFERENCES = FOLDER_ROOT / "references"
FOLDER_DOCS = FOLDER_ROOT / "docs"
FOLDER_LOGS = FOLDER_ROOT / "logs"
FOLDER_CONFIGS = FOLDER_ROOT / "configs"
FOLDER_CONFIG_FILES = FOLDER_CONFIGS / "config_files"

FOLDER_DATA_RAW = FOLDER_DATA / "raw"
FOLDER_DATA_EXTERNAL = FOLDER_DATA / "external"
FOLDER_DATA_INTERIM = FOLDER_DATA / "interim"
FOLDER_DATA_PROCESSED = FOLDER_DATA / "processed"

FOLDER_FIGURES = FOLDER_REPORTS / "figures"

# LOGGER FILE PATH
FILE_LOGGER = FOLDER_LOGS / "logs.log"

# FILE PATHS: Paths to files (.csv, .xlsx),
# databases (.db, .sqlite) and their respective table names
FILE_PATH_RAW = FOLDER_DATA_RAW / "Rice_Image_Dataset"
FILE_PATH_INTERIM = FOLDER_DATA_INTERIM / "interim_dataset.csv"
FILE_PATH_PROCESSED = FOLDER_DATA_PROCESSED / "processed_dataset.csv"
