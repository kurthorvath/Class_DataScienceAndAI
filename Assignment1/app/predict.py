import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--metrics", required=True)
    args = parser.parse_args()

    model = joblib.load(args.model)
    df = pd.read_csv(args.data)

    X = df[["x1", "x2"]]
    y = df["label"]

    predictions = model.predict(X)

    metrics = {
        "accuracy": accuracy_score(y, predictions),
        "f1": f1_score(y, predictions),
    }

    Path(args.metrics).parent.mkdir(parents=True, exist_ok=True)
    Path(args.metrics).write_text(json.dumps(metrics, indent=2))

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
