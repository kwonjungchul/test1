import logging
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget

# 로그 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Kiwoom:
    def __init__(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnReceiveTrCondition.connect(self.OnReceiveTrCondition)
        self.ocx.OnReceiveRealCondition.connect(self.OnReceiveRealCondition)
        self.condition_loaded = False
        self.login_event_loop = QEventLoop()

    def comm_connect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_event_loop.exec_()

    def get_condition_name_list(self):
        self.ocx.dynamicCall("GetConditionLoad()")
        while not self.condition_loaded:
            QCoreApplication.processEvents()

        conditions = self.ocx.dynamicCall("GetConditionNameList()")
        return [(c.split('^')[0], c.split('^')[1]) for c in conditions.split(';') if c]

    def send_condition(self, screen_no, condition_name, condition_index, is_real_time):
        self.ocx.dynamicCall("SendCondition(QString, QString, int, int)", screen_no, condition_name, condition_index, is_real_time)

    def OnReceiveTrCondition(self, screen_no, codes, condition_name, index, next):
        logging.info(f"OnReceiveTrCondition called with codes: {codes}")

    def OnReceiveRealCondition(self, code, event, condition_name, condition_index):
        logging.info(f"OnReceiveRealCondition called with code: {code}, event: {event}")

    def OnEventConnect(self, err_code):
        if err_code == 0:
            logging.info("로그인 성공")
        else:
            logging.info("로그인 실패")
        self.login_event_loop.exit()

def get_leading_stocks():
    app = QApplication([])
    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    conditions = kiwoom.get_condition_name_list()
    return conditions

def run_auto_trading():
    conditions = get_leading_stocks()
    condition_name = "주도주"
    condition_id = next((cid for cid, cname in conditions if cname == condition_name), None)

    if condition_id is None:
        print(f"조건식 '{condition_name}'을 찾을 수 없습니다.")
        return

    print(f"Sending condition {condition_name} with id {condition_id}")
    kiwoom.send_condition("0150", condition_name, condition_id, 1)

    while True:
        print("Waiting for condition results...")
        QCoreApplication.processEvents()
