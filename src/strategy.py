import pandas as pd
import numpy as np

def moving_average_strategy(file_path):
    print(f"Reading data from {file_path}...")
    df = pd.read_csv(file_path)
    print("Data read successfully.")

    short_window = 5
    long_window = 20

    print(f"Calculating moving averages with short_window={short_window} and long_window={long_window}...")
    df['short_mavg'] = df['close'].rolling(window=short_window, min_periods=1).mean()
    df['long_mavg'] = df['close'].rolling(window=long_window, min_periods=1).mean()

    df['volatility'] = df['close'].rolling(window=long_window, min_periods=1).std()

    df['signal'] = 0.0
    df.loc[short_window:, 'signal'] = np.where(df['short_mavg'][short_window:] > df['long_mavg'][short_window:], 1.0, 0.0)

    df['position'] = df['signal'].diff()

    df.to_csv('strategy_processed_stock_data.csv', index=False)
    print("Results saved to strategy_processed_stock_data.csv")

def augment_data(file_path):
    print(f"Reading data from {file_path}...")
    data = pd.read_csv(file_path)
    print("Data read successfully.")
    
    augmented_data = data.copy()
    augmented_data['date'] = pd.to_datetime(augmented_data['date'])

    for i in range(10):  # 10배 데이터 증강
        new_data = data.copy()
        new_data['date'] = pd.to_datetime(new_data['date']) + pd.to_timedelta(np.random.randint(1, 100, size=len(data)), unit='D')
        new_data['signal'] = np.random.choice([0.0, 1.0], size=len(new_data))  # 랜덤하게 signal 생성
        augmented_data = pd.concat([augmented_data, new_data], ignore_index=True)
    
    augmented_data = augmented_data.sort_values(by='date').reset_index(drop=True)
    augmented_file_path = 'augmented_strategy_processed_stock_data.csv'
    augmented_data.to_csv(augmented_file_path, index=False)
    print(f"Augmented data saved to {augmented_file_path}")

# Run the strategy and augment data
moving_average_strategy('processed_stock_data.csv')
augment_data('strategy_processed_stock_data.csv')



