import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QAxContainer import QAxWidget
from PyQt5.QtCore import QObject, pyqtSlot, QEventLoop

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self._create_event_handlers()
        self.comm_connect()

    def _create_event_handlers(self):
        self.OnEventConnect.connect(self.on_event_connect)
        self.OnReceiveTrCondition.connect(self.on_receive_tr_condition)

    @pyqtSlot(int)
    def on_event_connect(self, err_code):
        if err_code == 0:
            print("로그인에 성공하였습니다.")
        else:
            print("로그인에 실패하였습니다.")
        self.login_event_loop.exit()

    @pyqtSlot(str, str, str, str)
    def on_receive_tr_condition(self, screen_no, codes, condition_name, condition_index, next):
        print(f"Received condition: {condition_name} with codes: {codes}")
        self.condition_list = codes.split(';')
        self.condition_event_loop.exit()

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def get_condition_load(self):
        self.dynamicCall("GetConditionLoad()")
        self.condition_event_loop = QEventLoop()
        self.condition_event_loop.exec_()
        return self.condition_list

    def send_condition(self, screen_no, condition_name, condition_index):
        self.dynamicCall("SendCondition(QString, QString, int, int)", screen_no, condition_name, condition_index, 0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.kiwoom = Kiwoom()
        self.setCentralWidget(self.kiwoom)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('KHOpenAPI Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
