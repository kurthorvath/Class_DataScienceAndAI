from pathlib import Path

import pandas as pd

from data.generate_data import main


def test_data_generation():
    main()

    expected = [
        "train_A.csv",
        "test_A.csv",
        "test_B.csv",
        "train_AB.csv",
        "test_C.csv",
    ]

    for filename in expected:
        path = Path("data") / filename
        assert path.exists()
        df = pd.read_csv(path)
        assert not df.empty
        assert {"x1", "x2", "label"} <= set(df.columns)
