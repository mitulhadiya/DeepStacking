# DeepStacking

A custom multi-layer stacking framework for machine learning classification built using Python and Scikit-learn.

## Project Description

DeepStacking is a custom implementation of sequential stacking. Multiple machine learning models can be arranged into different layers, where predictions from one layer are added as features for the next layer.

The project uses Out-of-Fold (OOF) predictions with Stratified K-Fold cross-validation to reduce data leakage during training.

## How It Works

```text
Input Data
    ↓
Layer 1
(RF + LR + SVC)
    ↓
OOF Predictions
    ↓
Layer 2
(RF + LR)
    ↓
OOF Predictions
    ↓
Layer 3
(Logistic Regression)
    ↓
Final Prediction
```

## Technologies

- Python
- NumPy
- Pandas
- Scikit-learn

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd DeepStacking

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt

##Run

python train.py

##Author

Mitul Hadiya