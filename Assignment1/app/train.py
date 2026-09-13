import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", required=True)
    parser.add_argument("--model", required=True)
    parser.add_argument("--metrics", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.train)
    X = df[["x1", "x2"]]
    y = df["label"]

    model = LogisticRegression(random_state=42)
    model.fit(X, y)

    predictions = model.predict(X)
    metrics = {
        "model_version": args.version,
        "accuracy": accuracy_score(y, predictions),
        "f1": f1_score(y, predictions),
    }

    Path(args.model).parent.mkdir(parents=True, exist_ok=True)
    Path(args.metrics).parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(model, args.model)
    Path(args.metrics).write_text(json.dumps(metrics, indent=2))

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
