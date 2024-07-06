# filter_rising_stocks.py
import datetime
from pykiwoom.kiwoom import Kiwoom

def get_rising_stocks(leading_stocks):
    kiwoom = Kiwoom()
    rising_stocks = []
    today = datetime.datetime.today().strftime("%Y%m%d")

    for code in leading_stocks:
        df = kiwoom.block_request("opt10081",
                                  종목코드=code,
                                  기준일자=today,
                                  수정주가구분=1,
                                  output="주식일봉차트조회",
                                  next=0)
        if not df.empty:
            df = df[['일자', '현재가', '전일대비']].sort_values(by='일자', ascending=False)
            if df.iloc[0]['전일대비'] >= 10:
                rising_stocks.append(code)

    return rising_stocks

if __name__ == "__main__":
    from get_leading_stocks import get_leading_stocks
    
    leading_stocks = get_leading_stocks()
    rising_stocks = get_rising_stocks(leading_stocks)
    print(rising_stocks)
