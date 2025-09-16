# Time series preprocessing script
import pandas as pd

def preprocess_timeseries(input_path, output_path):
    # TODO: Implement time series preprocessing (cleaning, normalization)
    print(f"Preprocessing time series from {input_path} to {output_path}")

if __name__ == '__main__':
    preprocess_timeseries('data/raw/weather_data.csv', 'data/processed/weather_data.csv')
