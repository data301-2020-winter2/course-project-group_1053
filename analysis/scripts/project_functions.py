import numpy as np
import pandas as pd

def load_and_process(path):
    data = (pd.read_csv(path))
    data.to_csv('../data/processed/data.csv')
    return data
