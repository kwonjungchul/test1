import sys
from PyQt5.QtWidgets import QApplication
from pykiwoom.kiwoom import Kiwoom

def get_stock_info():
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    
    print("Get stock information")
    stock_code = "005930"  # 삼성전자 코드
    stock_info = kiwoom.GetMasterCodeName(stock_code)
    print(f"Stock Code: {stock_code}, Stock Name: {stock_info}")

if __name__ == "__main__":
    get_stock_info()
