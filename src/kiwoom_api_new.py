# kiwoom_api_new.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QAxContainer import QAxWidget
from pykiwoom.kiwoom import Kiwoom

class KiwoomAPI:
    def __init__(self, app):
        self.app = app
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        QMessageBox.information(None, "Info", "KHOpenAPI.KHOpenAPICtrl.1 loaded")
        self._set_signals_slots()

    def _set_signals_slots(self):
        self.kiwoom.OnEventConnect.connect(self._on_event_connect)

    def _on_event_connect(self, err_code):
        if err_code == 0:
            QMessageBox.information(None, "Info", "Connected successfully")
        else:
            QMessageBox.critical(None, "Error", "Connection failed")

    def login(self):
        self.kiwoom.dynamicCall("CommConnect()")

if __name__ == "__main__":
    app = QApplication([])
    api = KiwoomAPI(app)
    api.login()
    app.exec_()




