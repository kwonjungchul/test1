import pandas as pd
import numpy as np

def augment_data(file_path):
    print(f"Reading data from {file_path}...")
    data = pd.read_csv(file_path)
    print("Data read successfully.")
    
    augmented_data = data.copy()
    augmented_data['date'] = pd.to_datetime(augmented_data['date'])  # 이 부분을 추가합니다.

    for _ in range(10):  # 10배 데이터 증강
        new_data = data.copy()
        new_data['date'] = pd.to_datetime(new_data['date']) + pd.to_timedelta(np.random.randint(1, 100, size=len(data)), unit='D')
        augmented_data = pd.concat([augmented_data, new_data], ignore_index=True)
    
    augmented_data = augmented_data.sort_values(by='date').reset_index(drop=True)
    augmented_file_path = 'augmented_strategy_processed_stock_data.csv'
    augmented_data.to_csv(augmented_file_path, index=False)
    print(f"Augmented data saved to {augmented_file_path}")

augment_data('strategy_processed_stock_data.csv')
