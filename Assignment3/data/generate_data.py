from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent


def make_data(n, seed, kind):
    rng = np.random.default_rng(seed)

    if kind == "train_A":
        x1 = rng.normal(0, 1, n)
        x2 = rng.normal(0, 1, n)
        label = ((x1 + x2 + rng.normal(0, 0.35, n)) > 0).astype(int)

    elif kind == "test_A":
        x1 = rng.normal(0, 1, n)
        x2 = rng.normal(0, 1, n)
        label = ((x1 + x2 + rng.normal(0, 0.35, n)) > 0).astype(int)

    elif kind == "test_B":
        x1 = rng.normal(0, 1, n)
        x2 = rng.normal(0, 1, n)
        label = ((x1 - x2 + rng.normal(0, 0.35, n)) > 0).astype(int)

    elif kind == "train_AB":
        a = make_data(n // 2, seed, "train_A")
        b = make_data(n - n // 2, seed + 1, "test_B")
        return pd.concat([a, b], ignore_index=True)

    elif kind == "test_C":
        x1 = rng.normal(0, 1, n)
        x2 = rng.normal(0, 1, n)
        label = ((x1 + 0.8 * x2 + rng.normal(0, 0.55, n)) > 0).astype(int)

    else:
        raise ValueError(kind)

    return pd.DataFrame({"x1": x1, "x2": x2, "label": label})


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    make_data(800, 1, "train_A").to_csv(ROOT / "train_A.csv", index=False)
    make_data(400, 2, "test_A").to_csv(ROOT / "test_A.csv", index=False)
    make_data(400, 3, "test_B").to_csv(ROOT / "test_B.csv", index=False)
    make_data(800, 4, "train_AB").to_csv(ROOT / "train_AB.csv", index=False)
    make_data(400, 5, "test_C").to_csv(ROOT / "test_C.csv", index=False)


if __name__ == "__main__":
    main()
