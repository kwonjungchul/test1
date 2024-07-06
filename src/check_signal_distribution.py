import pandas as pd

def check_signal_distribution(file_path):
    df = pd.read_csv(file_path)
    print("Signal 값 분포:")
    print(df['signal'].value_counts())

check_signal_distribution('strategy_processed_stock_data.csv')
