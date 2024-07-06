from PyQt5.QtWidgets import QApplication
from PyQt5.QAxContainer import QAxWidget

app = QApplication([])
widget = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
widget.show()
app.exec_()
