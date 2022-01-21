from ed.secuenciales.notacionprefija import Prefija
from guiPrefija import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

class Ventana(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Configuración de los botones numéricos/operadores
        for n in range(0, 10): 
            getattr(self.ui, 'btn%s' % n).pressed.connect(lambda v=n: self.agregarCaracter(v))
        self.ui.btnEspacio.pressed.connect(lambda : self.agregarCaracter(' '))
        self.ui.btnParIzq.pressed.connect(lambda : self.agregarCaracter('('))
        self.ui.btnParDer.pressed.connect(lambda : self.agregarCaracter(')'))
        self.ui.btnSuma.pressed.connect(lambda : self.agregarCaracter('+'))
        self.ui.btnResta.pressed.connect(lambda : self.agregarCaracter('-'))
        self.ui.btnMulti.pressed.connect(lambda : self.agregarCaracter('*'))
        self.ui.btnDiv.pressed.connect(lambda : self.agregarCaracter('/'))
        self.ui.btnPot.pressed.connect(lambda : self.agregarCaracter('^'))

        #Configuración botones generales
        self.ui.btnBorrar.pressed.connect(self.borrar)
        self.ui.btnPrefija.pressed.connect(self.prefija)
        self.ui.btnIgual.pressed.connect(self.resultado)
       

    def agregarCaracter(self,caracter):
        text = self.ui.tEditDisplay.toPlainText()
        text += str(caracter)
        self.ui.tEditDisplay.setText(text)

    def borrar(self):
        self.ui.tEditDisplay.clear()
        self.ui.tEditPrefija.clear()

    def prefija(self):
        infija = self.ui.tEditDisplay.toPlainText()
        prefija = Prefija(infija)
        self.ui.tEditPrefija.setText(prefija.prefija())

    def resultado(self):
        infija = self.ui.tEditDisplay.toPlainText()
        prefija = Prefija(infija)
        self.ui.tEditPrefija.setText(str(prefija.eval_expr_aritm()))


stylesheet = """

QMainWindow {
    background-color: white; 
}

QLabel{
    color: Teal;    
}

QPushButton{
    background-color: white;  
    border: 0px; 
    color: Teal;
}

QPushButton:hover{
    background-color: #e9e9e9;
}

QPushButton:pressed {
    background-color: #e0e0e0;    
}

QTextEdit{
    color: Teal;    
}
"""

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = Ventana()
    widget.show()
    widget.setStyleSheet(stylesheet)
    app.exec_()