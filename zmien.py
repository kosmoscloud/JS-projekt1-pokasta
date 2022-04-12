class Zmien(object):
    def uiwd1wd2(self):
            if self.radioDodaj.isChecked():
                if self.radioPunkt.isChecked():
                    Wd1.show()
                elif self.radioPrzed.isChecked():
                    Wd2.show()
            elif self.radioExcel.isChecked():
                if self.radioPunkt.isChecked():
                    print("dane z excela punktowe")
                elif self.radioPrzed.isChecked():
                    print("dane z excela przedziałowe")
    def wd1w(self):
