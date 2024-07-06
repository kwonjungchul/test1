import pandas as pd
from pykiwoom.kiwoom import Kiwoom
import time

def execute_trading_strategy():
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    
    account_number = "63074821"
    df = pd.read_csv("analyzed_stock_data.csv")
    
    for index, row in df.iterrows():
        if row['positions'] == 1.0:
            print(f"Buying {row['종목코드']} at {row['종가']}")
            kiwoom.SendOrder("send_order_req", "0101", account_number, 1, str(row['종목코드']), 1, int(row['종가']), "00", "")
            time.sleep(1)  # Too fast requests can be denied
            
        elif row['positions'] == -1.0:
            print(f"Selling {row['종목코드']} at {row['종가']}")
            kiwoom.SendOrder("send_order_req", "0101", account_number, 2, str(row['종목코드']), 1, int(row['종가']), "00", "")
            time.sleep(1)  # Too fast requests can be denied

if __name__ == "__main__":
    execute_trading_strategy()
