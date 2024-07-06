from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QAxContainer import QAxWidget

app = QApplication([])

mainWindow = QMainWindow()
axWidget = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1", mainWindow)
mainWindow.setCentralWidget(axWidget)
mainWindow.show()

app.exec_()
