from PyQt5.QtWidgets import QMessageBox


class Buttons():
    def anuluj(self):
        anullo = QMessageBox()
        anullo.setText("Dziękuję za korzystanie z programu.")
        anullo.exec_()

    def infSred(self):
        sredollo = QMessageBox()
        sredollo.setText("Średnia arytmetyczna danych próby - iloraz sumy wszystkich wartości próby przez ilość rekordów.\nTu ")
        sredollo.exec_()

    def infDom(self):
        domollo = QMessageBox()
        domollo.setText("Dominanta to najczęściej występująca wartość próby.\nTu ")
        domollo.exec_()

    def infOdchyl(self):
        odchyllo = QMessageBox()
        odchyllo.setText("Odchylenie standardowe opisuje jak szeroko wartości są rozrzucone wokół średniej arytmetycznej próby.\nTu ")
        odchyllo.exec_()

    def infWspzm(self):
        zmiennolo = QMessageBox()
        zmiennolo.setText("Współczynnik zmienności to miara zróżnicowania rozkładu cechy - iloraz odchylenia standardowego przez średnią arytmetyczną.\nTu ")
        zmiennolo.exec_()

    def infWspas(self):
        asymolo = QMessageBox()
        asymolo.setText("Współczynnik asymetrii pozwala na określenie symetrii układu - przyjmuje wartość zero dla układu symetrycznego, ujemne wartości dla układów o asymetrii lewostronnej, a dodatnie - dla układów o asymetrii prawostronnej.\nTu ")
        asymolo.exec_()

    def infEks(self):
        ekscello = QMessageBox()
        ekscello.setText("Eksces to miara spłaszczenia rozkładu - przyjmuje wartość zero dla rozkładu normalnego (mezokurtycznego), wartości ujemne dla rozkładu spłaszczonego (leptokurtycznego), a dodatnie - dla rozkładu wysmukłego (platokurtycznego).\nTu ")
        ekscello.exec_()

    def infQ1(self):
        kwartyllo1 = QMessageBox()
        kwartyllo1.setText("Kwartyl pierwszy wyraża sie liczbą, która jest większa od dokładnie 25% wartości próby.\nTu ")
        kwartyllo1.exec_()

    def infQ2(self):
        kwartyllo2 = QMessageBox()
        kwartyllo2.setText("Kwartyl drugi (mediana) jest liczbą, która dzieli próbę dokładnie na pół.\nTu ")
        kwartyllo2.exec_()

    def infQ3(self):
        kwartyllo3 = QMessageBox()
        kwartyllo3.setText("Kwartyl trzeci wyraża sie liczbą, która jest większa od dokładnie 75% wartości próby.\nTu")
        kwartyllo3.exec_()
