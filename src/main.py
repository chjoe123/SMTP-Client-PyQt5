import sys
import smtplib
from email.mime.text import MIMEText
from UI_MailBox import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


class MailBox(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MailBox, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda : self.sendMessage(self.lineEdit.text(),
                                                                  self.lineEdit_2.text(),
                                                                  self.lineEdit_3.text(),
                                                                  self.lineEdit_4.text(),
                                                                  self.lineEdit_5.text(),
                                                                  self.lineEdit_6.text(),
                                                                  self.plainTextEdit.toPlainText(),
                                                                  self.checkBox.checkState()))

    def split_s(self, s):
        s_li = s.split(';')
        return s_li

    def sendMessage(self, host, port, user, password, sender, receivers, text, check_ssl):
        receivers = self.split_s(receivers)
        message = MIMEText(text, 'plain', 'utf-8')
        message['from'] = sender
        message['subject'] = 'title'
        message['to'] = ','.join(receivers)

        try:
            if check_ssl == 2:
                smtpObj = smtplib.SMTP_SSL(host, port)
                smtpObj.login(user, password)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.quit()
            elif check_ssl == 0:
                smtpObj = smtplib.SMTP(host, port)
                smtpObj.login(user, password)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.quit()

        except smtplib.SMTPException as e:
            print('error: ', e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mb = MailBox()
    mb.show()

    sys.exit(app.exec_())