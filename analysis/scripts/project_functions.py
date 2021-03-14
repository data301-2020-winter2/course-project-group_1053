import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          #.rename(...)
          #.dropna(...)
          # etc...
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(...)
      )

    # Make sure to return the latest dataframe

    return df2 


def hello():
    print("test")
