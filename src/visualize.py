import pandas as pd
import matplotlib.pyplot as plt

def visualize_strategy(file_path):
    print(f"Reading data from {file_path}...")
    df = pd.read_csv(file_path, index_col='date', parse_dates=True)
    print("Data read successfully.")
    
    # 전략 시각화
    print("Visualizing strategy...")
    plt.figure(figsize=(12, 6))
    
    # 종가 및 이동 평균
    plt.plot(df['close'], label='Close Price')
    plt.plot(df['short_mavg'], label='Short Moving Average (40 days)')
    plt.plot(df['long_mavg'], label='Long Moving Average (100 days)')
    
    # 매수 신호
    plt.plot(df[df['positions'] == 1].index, df['short_mavg'][df['positions'] == 1], '^', markersize=10, color='g', lw=0, label='Buy Signal')
    # 매도 신호
    plt.plot(df[df['positions'] == -1].index, df['short_mavg'][df['positions'] == -1], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
    
    plt.title('Moving Average Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    
    plt.savefig('strategy_visualization.png')
    print("Visualization saved as strategy_visualization.png")
    plt.show()

visualize_strategy('strategy_processed_stock_data.csv')
