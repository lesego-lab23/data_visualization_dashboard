import pandas as pd

def load_data(filepath="car_price_prediction_.csv"):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)
    return df
