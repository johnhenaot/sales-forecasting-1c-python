import pandas as pd

if __name__ == '__main__':
    df: pd.DataFrame = \
        pd.read_csv(
            "",
            header=None, names=["time"])

    print(df.head())
