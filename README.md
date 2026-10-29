# Breast Cancer Classification (Wisconsin Diagnostic)

A machine learning project that classifies breast tumors as **malignant** or **benign** using the Breast Cancer Wisconsin (Diagnostic) dataset and an **XGBoost** classifier.

## Results

| Metric    | Score |
|-----------|-------|
| Accuracy  | 97%   |
| F1-score  | 96%   |
| Precision | 100%  |
| Recall    | 93%   |

Precision of 100% means every tumor predicted as malignant was truly malignant. Recall of 93% means a few malignant cases were missed, which is the metric to improve first in a medical setting.

## Dataset

- **Name:** Breast Cancer Wisconsin (Diagnostic)
- **Samples:** 569
- **Features:** 30 numeric features computed from images of cell nuclei (radius, texture, perimeter, area, etc.)
- **Target:** `M` (malignant) / `B` (benign)

## Project Structure

```
02_breast_cancer_wisconsin/
├── data/          # raw and processed datasets
├── models/        # saved trained model
├── note.book/     # Jupyter notebooks (exploration, preprocessing, training)
├── reports/       # evaluation report and figures
├── src/           # configuration and helper code
├── .gitignore
└── README.md
```

## Workflow

1. **Data exploration:** distributions, class balance, correlations
2. **Preprocessing:** cleaning, encoding the target, scaling, train/test split
3. **Model training:** XGBoost classifier (`max_depth=1`)
4. **Evaluation:** confusion matrix and classification report, saved to `reports/`

## Installation

```bash
git clone https://github.com/farhanshn/02_breast_cancer_wisconsin.git
cd 02_breast_cancer_wisconsin
pip install -r requirements.txt
```

## Usage

Start Jupyter and run the notebooks in the `note.book` folder in order:

```bash
jupyter notebook
```

1. `01_data_exploration`
2. `02_data_preprocessing`
3. `03_model_training`

## Tech Stack

Python, pandas, NumPy, scikit-learn, XGBoost, Matplotlib, Seaborn, Jupyter

## Author

**farhanshn**
