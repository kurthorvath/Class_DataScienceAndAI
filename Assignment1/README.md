<img width="800" height="162" alt="image" src="https://github.com/user-attachments/assets/a2bc697d-1856-4059-a004-ad8362a8b7fc" />

# Assignment 1 – Train an ML Model Locally

This folder is the starting point for Assignment 1.

The goal is to run a simple machine-learning workflow locally:

    Training Data + Test Data
              ↓
         Train Model
              ↓
       Apply Test Data
              ↓
          Evaluate

Most of the application is already provided. Your task is to understand the
files, set up the Python environment, generate the data, train the model, and
evaluate it using test data.

## Files and folders

### `app/`

Contains the machine-learning application.

#### `app/train.py`

Trains the machine-learning model.

The script:

1. Reads a training dataset from a CSV file.
2. Selects the input features (`x1` and `x2`).
3. Uses the `label` column as the target.
4. Trains a Logistic Regression model.
5. Calculates training accuracy and F1 score.
6. Saves the trained model to a file.
7. Saves the training metrics as JSON.

The trained model is therefore a separate artifact from the Python source code.

Example:

    python -m app.train \
        --train data/train_A.csv \
        --model artifacts/model_A.joblib \
        --metrics artifacts/model_A_train_metrics.json \
        --version A

#### `app/predict.py`

Applies a previously trained model to a dataset.

The script:

1. Loads the trained model.
2. Loads the supplied CSV dataset.
3. Uses the input features to generate predictions.
4. Compares the predictions with the known labels.
5. Calculates accuracy and F1 score.
6. Writes the evaluation metrics to a JSON file.

Example:

    python -m app.predict \
        --model artifacts/model_A.joblib \
        --data data/test_A.csv \
        --metrics artifacts/model_A_test_A.json

### `data/generate_data.py`

Creates all datasets used in the assignment.

The data is generated programmatically using NumPy, so the datasets can be
recreated rather than being manually edited.

The generator creates the following datasets:

- `train_A.csv` – training data used to train the initial model.
- `test_A.csv` – test data with the same general data pattern as the training
  data. It is used to check how well the trained model performs on unseen data.
- `test_B.csv` – changed data with a different relationship between the input
  features and the label. This dataset is later used in Assignment 3 to
  demonstrate degraded model performance.
- `train_AB.csv` – combined data used later for retraining an adapted model.
- `test_C.csv` – independent test data used later to evaluate the adapted model.

For Assignment 1, the important datasets are primarily:

    train_A.csv
    test_A.csv

The basic data-generation idea is:

    Input features (x1, x2)
             ↓
       data-generation rule
             ↓
          label (0/1)

The model learns the relationship between `x1`, `x2`, and `label` from
`train_A.csv`. It is then applied to the previously unseen examples in
`test_A.csv`.

This separation is important: the model should be evaluated on data that was
not used to train it.

To generate the datasets, run:

    python data/generate_data.py

### `tests/test_pipeline.py`

Contains simple automated tests for the supplied data-generation functionality.

Run the tests with:

    python -m pytest -v tests/test_pipeline.py

The tests are included to give you an early example of automated software
testing. More extensive CI automation will be introduced in Assignment 2.

### `requirements.txt`

Lists the Python packages required by the application:

- NumPy
- pandas
- scikit-learn
- joblib
- pytest

Install them with:

    python -m pip install -r requirements.txt

## Suggested workflow

### 1. Set up the environment

Create and activate a Python virtual environment if desired, then install
the dependencies.

### 2. Generate the datasets

Run:

    python data/generate_data.py

Check that the CSV files appear in the `data/` directory.

### 3. Train the model

Run:

    python -m app.train --train data/train_A.csv --model artifacts/model_A.joblib --metrics artifacts/model_A_train_metrics.json --version A

This creates:

    artifacts/model_A.joblib
    artifacts/model_A_train_metrics.json

### 4. Evaluate the model

Apply the trained model to the test data:

    python -m app.predict --model artifacts/model_A.joblib --data data/test_A.csv --metrics artifacts/model_A_test_A.json

This creates:

    artifacts/model_A_test_A.json

The JSON file contains the evaluation metrics, including accuracy and F1 score.



    Train → Evaluate → Deploy → Monitor → Detect → Retrain → Evaluate → Deploy

Assignment 1 is therefore the foundation for the MLOps workflow developed later.
