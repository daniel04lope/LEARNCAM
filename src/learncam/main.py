from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Primera App con PyQt6")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)

        self.boton = QPushButton("Haz clic", self)
        self.boton.clicked.connect(self.mostrar_mensaje)

        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def mostrar_mensaje(self):
        self.boton.setText("¡Hola, PyQt6!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi Primera App con PyQt6")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)

        self.boton = QPushButton("Haz clic", self)
        self.boton.clicked.connect(self.mostrar_mensaje)

        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        self.setLayout(layout)

    def mostrar_mensaje(self):
        self.boton.setText("¡Hola, PyQt6!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
