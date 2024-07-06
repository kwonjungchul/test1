from kiwoom_api import Kiwoom
from PyQt5.QtWidgets import QApplication
import sys

class AutoTrading:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()
        self.kiwoom.comm_connect()
        self.setup_conditions()
        sys.exit(self.app.exec_())

    def setup_conditions(self):
        conditions = self.kiwoom.get_condition_load()
        print("Conditions:", conditions)
        condition_name = '주도주'
        condition_index = '001'
        self.kiwoom.send_condition("0", condition_name, condition_index)

if __name__ == "__main__":
    AutoTrading()
