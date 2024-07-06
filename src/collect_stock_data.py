import pandas as pd
from pykiwoom.kiwoom import Kiwoom
import time

def collect_stock_data():
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    
    stock_code = "005930"  # 삼성전자 예시
    df = kiwoom.block_request("opt10081",
                              종목코드=stock_code,
                              기준일자="20210701",
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=0)
    df['종목코드'] = stock_code
    df.to_csv("stock_data.csv")
    print("Stock data collected and saved to stock_data.csv")

if __name__ == "__main__":
    collect_stock_data()
