import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QPushButton,
    QWidget,
)
import arrange_algo as arr
import pdf_gen


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("EquiSeat")
        self.resize(600, 500)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        tabs = QTabWidget()
        self.general_checkboxes = []
        self.network_checkboxes = []

        tabs.addTab(self.generalTabUI(), "Rooms")
        tabs.addTab(self.networkTabUI(), "Section")
        layout.addWidget(tabs)

    def generalTabUI(self): 
        generalTab = QWidget()
        layout = QVBoxLayout()
        checkbox1 = QCheckBox("IT-1")
        layout.addWidget(checkbox1)
        self.general_checkboxes.append(checkbox1)

        checkbox2 = QCheckBox("IT-2")
        layout.addWidget(checkbox2)
        self.general_checkboxes.append(checkbox2)

        checkbox3 = QCheckBox("IT-3")
        layout.addWidget(checkbox3)
        self.general_checkboxes.append(checkbox3)

        checkbox4 = QCheckBox("IT-4")
        layout.addWidget(checkbox4)
        self.general_checkboxes.append(checkbox4)

        button = QPushButton('Submit', self)
        button.clicked.connect(self.get_selected_checkboxes_general)
        layout.addWidget(button)
        generalTab.setLayout(layout)
        return generalTab

    def networkTabUI(self):
        networkTab = QWidget()
        layout = QVBoxLayout()
        checkbox1 = QCheckBox("IT-3A")
        layout.addWidget(checkbox1)
        self.network_checkboxes.append(checkbox1)

        checkbox2 = QCheckBox("IT-3B")
        layout.addWidget(checkbox2)
        self.network_checkboxes.append(checkbox2)

        button = QPushButton('Submit', self)
        button.clicked.connect(self.get_selected_checkboxes_network)
        layout.addWidget(button)
        networkTab.setLayout(layout)
        return networkTab

    def get_selected_checkboxes_general(self):
        selected_rooms = [checkbox.text() for checkbox in self.general_checkboxes if checkbox.isChecked()]
        self.arrange()

    def get_selected_checkboxes_network(self):
        selected_sections = [checkbox.text() for checkbox in self.network_checkboxes if checkbox.isChecked()]
        self.arrange()

    def arrange(self):
        selected_rooms = [checkbox.text() for checkbox in self.general_checkboxes if checkbox.isChecked()]
        selected_sections = [checkbox.text() for checkbox in self.network_checkboxes if checkbox.isChecked()]
        matrices = arr.arrange(arr.get_data(selected_sections), selected_rooms)
        if isinstance(matrices, list):  
            pdf_gen.generate_pdfs_for_matrices(matrices)
        else:
            print("No arrangement was possible.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
