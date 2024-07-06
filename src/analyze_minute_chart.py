# analyze_minute_chart.py
from pykiwoom.kiwoom import Kiwoom
import pandas as pd

def analyze_minute_chart(stock_code):
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    
    df = kiwoom.block_request("opt10080",
                              종목코드=stock_code,
                              틱범위=1,
                              수정주가구분=1,
                              output="주식분봉차트조회",
                              next=0)

    if df.empty:
        return None

    df['거래대금'] = df['현재가'] * df['거래량']
    total_volume = df['거래량'].sum()
    total_value = df['거래대금'].sum()
    avg_volume_per_min = df['거래량'].mean()
    avg_value_per_min = df['거래대금'].mean()
    volume_per_sec = df['거래량'].sum() / (df.shape[0] * 60)
    value_per_sec = df['거래대금'].sum() / (df.shape[0] * 60)

    return {
        'total_volume': total_volume,
        'total_value': total_value,
        'avg_volume_per_min': avg_volume_per_min,
        'avg_value_per_min': avg_value_per_min,
        'volume_per_sec': volume_per_sec,
        'value_per_sec': value_per_sec
    }

if __name__ == "__main__":
    from filter_rising_stocks import get_rising_stocks
    from get_leading_stocks import get_leading_stocks

    leading_stocks = get_leading_stocks()
    rising_stocks = get_rising_stocks(leading_stocks)

    for stock in rising_stocks:
        analysis = analyze_minute_chart(stock)
        if analysis:
            print(f"Stock Code: {stock}, Analysis: {analysis}")
