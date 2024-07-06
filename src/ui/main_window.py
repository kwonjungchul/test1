# main_window.py 파일의 내용 예제

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Trading App")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        # UI 요소를 초기화하고 배치하는 코드
        pass

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

