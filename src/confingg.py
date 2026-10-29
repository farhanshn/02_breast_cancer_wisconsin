from pathlib import Path 
#define the root path
PROJECT_ROOT=Path(__file__).resolve().parent.parent

#define the 
DATA_DIR=PROJECT_ROOT / "data"
RAW_DATA_DIR=DATA_DIR / "raw"
PROCESSED_DATA_DIR=DATA_DIR / "processed"

#define the output models if is there any
MODELDS_DIR=PROJECT_ROOT/ "models"
REPORTS_DIR=PROJECT_ROOT /"reports"

BREAST_DATASET=RAW_DATA_DIR / "Breast Cancer Wisconsin (Diagnostic) Data Set (1).csv"