import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget

app = QApplication(sys.argv)
kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

if kiwoom:
    print("KHOpenAPI.KHOpenAPICtrl.1 초기화 성공")
else:
    print("KHOpenAPI.KHOpenAPICtrl.1 초기화 실패")
