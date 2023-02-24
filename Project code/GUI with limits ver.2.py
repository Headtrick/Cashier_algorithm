import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QInputDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label = QLabel("Enter the amount to be changed:")
        self.amount_input = QLineEdit()
        self.find_button = QPushButton("Find Minimal Number of Change")
        self.result_label = QLabel()
        self.limits = [0] * 12
        self.limit_buttons = []

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.find_button)
        layout.addWidget(self.result_label)

        # Create limit buttons
        for i in range(12):
            button = QPushButton(f"Set Limit for Denomination {i + 1}")
            self.limit_buttons.append(button)
            layout.addWidget(button)
            button.clicked.connect(self.submit_limit)

        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle("Minimal Number of Change")
        self.setGeometry(300, 300, 300, 150)

        # Connect signals to slots
        self.find_button.clicked.connect(self.find_min)

    def submit_limit(self):
        button = self.sender()
        index = self.limit_buttons.index(button)
        limit, ok = QInputDialog.getInt(self, "Set Limit", "Enter limit:")
        if ok:
            self.limits[index] = limit

    def find_min(self):
        # All denominations of Turkish Currency
        deno = [1, 5, 10, 25, 50,
                100, 500, 1000, 2000, 5000, 10000, 20000]
        n = len(deno)

        # Initialize Result
        ans = []

        # Get amount from input field
        V = float(self.amount_input.text()) * 100

        # Traverse through all denomination
        i = n - 1
        while (i >= 0):
            # Find denominations
            while (V >= deno[i] and self.limits[i] > 0):
                V -= deno[i]
                self.limits[i] -= 1
                ans.append(deno[i])
            i -= 1

        # Format and display result
        result = ", ".join([str(a / 100) for a in ans])
        self.result_label.setText(f"Minimal number of change: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
