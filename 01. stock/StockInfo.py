import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kiwoom Login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")

        # OpenAPI + Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)

        self.setWindowTitle("Roy Stock")
        self.setGeometry(300, 300, 450, 650)

        label = QLabel("종목코드 ", self)
        label.move(20, 20)

        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("039490")

        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 60, 400, 550)
        self.text_edit.setEnabled(False)

    def event_connect(self, err_code):
        if err_code ==0:
            self.text_edit.append("Roy님 반갑습니다.")

    def btn1_clicked(self, err_code):
        code = self.code_edit.text()
        # self.text_edit.append("[+] 종목코드 : " + code)

        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        
        # CommRqData
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")

    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "종목명")
            high = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "연중최고")
            low = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "연중최저")
            current = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "현재가")
            yesterday = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "전일대비")
            high250 = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "250최고")
            low250 = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "250최저")
            
            result = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "매출액")
            operIncom = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "영업이익")
            netIncom = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "당기순이익")

            foreign = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "외인소진률")
            total = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "시가총액")
            base = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "액면가")
            month = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "결산월")
            volume = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "거래량")

            per = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PER")
            eps = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "EPS")
            roe = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "ROE")
            pbr = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "PBR")
            bps = self.kiwoom.dynamicCall("CommGetData(QString, QString, QString, int, QString)", trcode, "", rqname, 0, "BPS")

            self.text_edit.append("\n")
            self.text_edit.append("[기본정보]")
            self.text_edit.append("  [+] 종목명   : " + name.strip())
            self.text_edit.append("  [+] 현재가격 : " + current.strip()+"원")
            self.text_edit.append("  [+] 전일대비 : " + yesterday.strip()+"원")
            
            
            self.text_edit.append("\n")
            self.text_edit.append("[매출정보]")
            self.text_edit.append("  [+] 매출총이익 : " + result.strip()+"억")
            self.text_edit.append("  [+] 영업이익   : " + operIncom.strip()+"억")
            self.text_edit.append("  [+] 당기순이익 : " + netIncom.strip()+"억")

            self.text_edit.append("\n")
            self.text_edit.append("[고저가격]")                
            self.text_edit.append("  [+] 250최고  : " + high250.strip()[1:]+"원")
            self.text_edit.append("  [+] 250최저  : " + low250.strip()[1:]+"원")
            self.text_edit.append("  [+] 연중최고 : " + high.strip()[1:]+"원")
            self.text_edit.append("  [+] 연중최저 : " + low.strip()[1:]+"원")

            self.text_edit.append("\n")
            self.text_edit.append("[보조정보]")
            self.text_edit.append("  [+] 거래량     : " + volume.strip()+"주")
            self.text_edit.append("  [+] 시가총액   : " + total.strip()+"억")
            self.text_edit.append("  [+] 외인소진률 : " + foreign.strip()[1:]+"%")
            self.text_edit.append("  [+] 액면가     : " + base.strip()+"원")
            self.text_edit.append("  [+] 결산월     : " + month.strip()+"월")

            self.text_edit.append("\n")
            self.text_edit.append("[비율정보]")
            self.text_edit.append("  [+] PER     : " + per.strip())
            self.text_edit.append("  [+] EPS     : " + eps.strip())
            self.text_edit.append("  [+] ROE     : " + roe.strip())
            self.text_edit.append("  [+] PBR     : " + pbr.strip())
            self.text_edit.append("  [+] BPS     : " + bps.strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
