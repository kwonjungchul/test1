import pandas as pd

def preprocess_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("CSV 파일의 처음 몇 줄:")
        print(df.head())
    except pd.errors.ParserError as e:
        print(f"파일을 읽는 중 오류 발생: {e}")
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                print(f"라인 {i+1}: {line.strip()}")
                if i >= 20:
                    break
        return

    try:
        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        df = df.sort_index()

        df['short_mavg'] = df['close'].rolling(window=40, min_periods=1).mean()
        df['long_mavg'] = df['close'].rolling(window=100, min_periods=1).mean()
        df['volatility'] = df['close'].rolling(window=100, min_periods=1).std()

        df.to_csv('processed_' + file_path)
    except KeyError as e:
        print(f"열 이름 오류: {e}")

preprocess_data('stock_data.csv')
