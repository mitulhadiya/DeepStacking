# DeepStacking

A custom multi-layer stacking framework for machine learning classification built using Python and Scikit-learn.

## Project Description

DeepStacking is a custom implementation of sequential stacking. Multiple machine learning models can be arranged into different layers, where predictions from one layer are added as features for the next layer.

The project uses Out-of-Fold (OOF) predictions with Stratified K-Fold cross-validation to reduce data leakage during training.

## How It Works

```text
Input Features (X)
        │
        ▼
   ┌─────────┐
   │ Layer 1 │  RandomForest × 3
   └─────────┘
        │
        │ OOF predictions
        ▼
X + Layer 1 predictions
        │
        ▼
   ┌─────────┐
   │ Layer 2 │  RandomForest × 2
   └─────────┘
        │
        │ OOF predictions
        ▼
X + Layer 1 + Layer 2 predictions
        │
        ▼
   ┌─────────┐
   │ Layer 3 │  RandomForest (final)
   └─────────┘
        │
        ▼
  Final Prediction
```
## Features
 
- Sequential, multi-layer stacking architecture
- Any Scikit-learn–compatible classifier can be used as a base model
- Automatic `predict_proba` / `predict` fallback per model
- Leak-resistant training via Stratified K-Fold OOF predictions
- Simple, Keras-style API: `add()`, `fit()`, `predict()`

## Technologies

- Python
- NumPy
- Pandas
- Scikit-learn

## Installation

```bash
git clone https://github.com/mitulhadiya/DeepStacking.git
cd DeepStacking
 
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # macOS / Linux
 
pip install -r requirements.txt
```

## Run the Example
 
```bash
python train.py
```

## Author
 
**Mitul Hadiya**