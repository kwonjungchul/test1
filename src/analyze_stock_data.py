import pandas as pd
import numpy as np

def analyze_stock_data(short_window, long_window):
    df = pd.read_csv("stock_data.csv", index_col=0)
    df['종가'] = df['현재가']
    
    df['short_mavg'] = df['종가'].rolling(window=short_window, min_periods=1).mean()
    df['long_mavg'] = df['종가'].rolling(window=long_window, min_periods=1).mean()
    
    df['signal'] = 0.0
    df['signal'][short_window:] = np.where(df['short_mavg'][short_window:] > df['long_mavg'][short_window:], 1.0, 0.0)
    df['positions'] = df['signal'].diff()
    
    df.to_csv("analyzed_stock_data.csv", index=False)
    print("Stock data analyzed and saved to analyzed_stock_data.csv")

if __name__ == "__main__":
    analyze_stock_data(5, 20)
