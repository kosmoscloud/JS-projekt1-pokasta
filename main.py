import sys, random
from intro import Ui_Dialog
from wyniki import Ui_MainWindow
from buttons import Buttons
import pandas as pd
from wprowadzanieDanych1 import Ui_wprowadzanieDanychPunkt
from wprowadzanieDanych2 import Ui_wprowadzanieDanychPrzed
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


def stworztablice():
    global ilosciSpinArr
    if ui.radioPunkt.isChecked():
        global wartosciSpinArr
        wartosciSpinArr = [uiwd1.wartoscSpin_1, uiwd1.wartoscSpin_2, uiwd1.wartoscSpin_3, uiwd1.wartoscSpin_4, uiwd1.wartoscSpin_5, uiwd1.wartoscSpin_6, uiwd1.wartoscSpin_7, uiwd1.wartoscSpin_8, uiwd1.wartoscSpin_9, uiwd1.wartoscSpin_10, uiwd1.wartoscSpin_11, uiwd1.wartoscSpin_12,]
        ilosciSpinArr = [uiwd1.iloscSpin_1, uiwd1.iloscSpin_2, uiwd1.iloscSpin_3, uiwd1.iloscSpin_4, uiwd1.iloscSpin_5, uiwd1.iloscSpin_6, uiwd1.iloscSpin_7, uiwd1.iloscSpin_8, uiwd1.iloscSpin_9, uiwd1.iloscSpin_10, uiwd1.iloscSpin_11, uiwd1.iloscSpin_12]
    elif ui.radioPrzed.isChecked():
        global lGranSpinArr, rGranSpinArr
        lGranSpinArr = [uiwd2.lGranSpin_1, uiwd2.lGranSpin_2, uiwd2.lGranSpin_3, uiwd2.lGranSpin_4, uiwd2.lGranSpin_5, uiwd2.lGranSpin_6, uiwd2.lGranSpin_7, uiwd2.lGranSpin_8, uiwd2.lGranSpin_9, uiwd2.lGranSpin_10, uiwd2.lGranSpin_11, uiwd2.lGranSpin_12]
        rGranSpinArr = [uiwd2.rGranSpin_1, uiwd2.rGranSpin_2, uiwd2.rGranSpin_3, uiwd2.rGranSpin_4, uiwd2.rGranSpin_5, uiwd2.rGranSpin_6, uiwd2.rGranSpin_7, uiwd2.rGranSpin_8 ,uiwd2.rGranSpin_9, uiwd2.rGranSpin_10, uiwd2.rGranSpin_11, uiwd2.rGranSpin_12]
        ilosciSpinArr = [uiwd2.iloscSpin_1, uiwd2.iloscSpin_2, uiwd2.iloscSpin_3, uiwd2.iloscSpin_4, uiwd2.iloscSpin_5, uiwd2.iloscSpin_6, uiwd2.iloscSpin_7, uiwd2.iloscSpin_8, uiwd2.iloscSpin_9, uiwd2.iloscSpin_10, uiwd2.iloscSpin_11, uiwd2.iloscSpin_12]
def stworzTabliceValPunkt(a, b):
    global wartosciArrVal, ilosciArrVal
    wartosciArrVal = a
    ilosciArrVal = b


def stworzTabliceValPrzed(a, b):
    print("nada")


def sortujab(a, b):
    a.sort()
    b = [x for _, x in sorted(zip(b, a))]

    return a, b


def changeapp():
    if ui.radioDodaj.isChecked():
        if ui.radioPunkt.isChecked():
            stworztablice()
            Wd1.show()
        elif ui.radioPrzed.isChecked():
            Wd2.show()
    elif ui.radioExcel.isChecked():
        if ui.radioPunkt.isChecked():
            file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                      "", "MS Excel files (*.xlsx)")
            if check:
                df = pd.read_excel(file)
                df = df.transpose()
                ddf = df.to_numpy()
                sortowane = sortujab(ddf[0], ddf[1])
                stworzTabliceValPunkt(sortowane[0], sortowane[1])
                print(sortowane)

        elif ui.radioPrzed.isChecked():
            print("dane z excela przedziałowe")
    Dialog.close()


def wd1w():
    Wd1.close()
    Wyniki.show()


def wd2w():
    Wd2.close()
    Wyniki.show()


def loswd1():
    for i in range(0, 12):
        wartosciSpinArr[i].setProperty("value", round(random.uniform(0, 111), 2))
        ilosciSpinArr[i].setProperty("value", random.randint(0, 111))

def loswd2():
    print("zaraz")


def reswd1():
    for i in range(0, 12):
        wartosciSpinArr[i].setProperty("value", 0)
        ilosciSpinArr[i].setProperty("value", 0)


def reswd2():
    print("zaraz")


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
Wyniki = QtWidgets.QMainWindow()
Wd1 = QtWidgets.QDialog()
Wd2 = QtWidgets.QDialog()

ui = Ui_Dialog()
uiw = Ui_MainWindow()
uiwd1 = Ui_wprowadzanieDanychPunkt()
uiwd2 = Ui_wprowadzanieDanychPrzed()
but = Buttons()

ui.setupUi(Dialog)
uiw.setupUi(Wyniki)
uiwd1.setupUi(Wd1)
uiwd2.setupUi(Wd2)

ui.okButton.clicked.connect(changeapp)
ui.anulujButton.clicked.connect(but.anuluj)

uiwd1.oblicz.clicked.connect(wd1w)
uiwd1.losuj.clicked.connect(loswd1)
uiwd1.resetuj.clicked.connect(reswd1)

uiwd2.oblicz.clicked.connect(wd2w)
uiwd2.losuj.clicked.connect(loswd2)
uiwd2.resetuj.clicked.connect(reswd2)

uiw.infSrednia.clicked.connect(but.infSred)
uiw.infDominanta.clicked.connect(but.infDom)
uiw.infOdchylenie.clicked.connect(but.infOdchyl)
uiw.infWspzm.clicked.connect(but.infWspzm)
uiw.infWspas.clicked.connect(but.infWspas)
uiw.infEksces.clicked.connect(but.infEks)
uiw.infQ1.clicked.connect(but.infQ1)
uiw.infQ2.clicked.connect(but.infQ2)
uiw.infQ3.clicked.connect(but.infQ3)

Dialog.show()
sys.exit(app.exec_())