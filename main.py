
import sys
from random import choice
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet():
    if msgLabel.text():
        msgLabel.setText("")

    else:
        msgLabel.setText(print(choice(['Bmw', 'Audi', 'Mercedes-Benz', 'Ford', 'Honda', 'Volkswagen', 'Hyundai', 'Nissan'])))

app = QApplication([])
window = QWidget()
window.setWindowTitle("Приложение")
layout = QVBoxLayout()

button = QPushButton("Приветствовать")
button.clicked.connect(greet)

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())