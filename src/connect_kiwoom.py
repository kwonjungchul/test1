from pykiwoom.kiwoom import Kiwoom
import time

def connect_to_kiwoom():
    kiwoom = Kiwoom()
    kiwoom.CommConnect(block=True)
    print("Connected to Kiwoom API")
    return kiwoom

if __name__ == "__main__":
    kiwoom = connect_to_kiwoom()
    account_number = "63074821"
    print(f"Using account: {account_number}")
