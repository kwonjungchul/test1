# auto_trading_strategy.py
from pykiwoom.kiwoom import Kiwoom

def execute_trading_strategy(stock_code, account_number):
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    
    analysis = analyze_minute_chart(stock_code)
    if not analysis:
        print(f"{stock_code} 분석 실패")
        return

    # 여기서는 매매 전략의 예로 특정 조건을 만족하면 매수/매도를 수행합니다.
    if analysis['avg_value_per_min'] > 100000000:  # 예시 조건
        kiwoom.SendOrder("매수", "0101", account_number, 1, stock_code, 10, 0, "03", "")
        print(f"{stock_code} 매수")

if __name__ == "__main__":
    from analyze_minute_chart import analyze_minute_chart
    from filter_rising_stocks import get_rising_stocks
    from get_leading_stocks import get_leading_stocks

    account_number = "63074821"  # 사용자의 계좌 번호

    leading_stocks = get_leading_stocks()
    rising_stocks = get_rising_stocks(leading_stocks)

    for stock in rising_stocks:
        execute_trading_strategy(stock, account_number)
