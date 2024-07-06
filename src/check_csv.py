import pandas as pd

df = pd.read_csv('strategy_processed_stock_data.csv')
print("CSV 파일의 처음 몇 줄:")
print(df.head())
print("\nCSV 파일의 열 이름:")
print(df.columns)
