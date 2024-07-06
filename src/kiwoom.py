from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

        self.login_event_loop = None
        self.condition_event_loop = None

        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveConditionVer.connect(self._receive_condition_ver)
        self.OnReceiveTrCondition.connect(self._receive_tr_condition)
        self.OnReceiveRealCondition.connect(self._receive_real_condition)

        self.condition_stock_dict = {}

    def CommConnect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("로그인 성공")
        else:
            print("로그인 실패")
        self.login_event_loop.exit()

    def GetConnectState(self):
        return self.dynamicCall("GetConnectState()")

    def GetConditionLoad(self):
        self.dynamicCall("GetConditionLoad()")
        self.condition_event_loop = QEventLoop()
        self.condition_event_loop.exec_()

    def _receive_condition_ver(self, lRet, sMsg):
        if lRet == 1:
            self.condition_list = self.dynamicCall("GetConditionNameList()").split(";")[:-1]
        else:
            self.condition_list = []
        self.condition_event_loop.exit()

    def GetConditionNameList(self):
        self.GetConditionLoad()
        conditions = []
        for condition in self.condition_list:
            cond_id, cond_name = condition.split('^')
            conditions.append((cond_id, cond_name))
        return conditions

    def SendCondition(self, scrNo, strConditionName, nIndex, nSearch):
        self.dynamicCall("SendCondition(QString, QString, int, int)", scrNo, strConditionName, nIndex, nSearch)

    def _receive_tr_condition(self, scrNo, strCodeList, strConditionName, strIndex, nNext):
        codes = strCodeList.split(';')[:-1]
        self.condition_stock_dict = {code: strConditionName for code in codes}

    def _receive_real_condition(self, strCode, strType, strConditionName, strConditionIndex):
        if strType == 'I':
            self.condition_stock_dict[strCode] = strConditionName
        elif strType == 'D':
            del self.condition_stock_dict[strCode]

