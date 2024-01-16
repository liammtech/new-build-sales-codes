import sys, pyodbc, datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.connectToDatabase()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sales Code Generator (New Build)")
        self.setStyleSheet("font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;")

        # App Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Main Section
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)

        # Buying Code
        buying_code_label = QLabel("Enter buying code")
        main_layout.addWidget(buying_code_label)
        self.buying_code_edit = QLineEdit()
        inspect_button = QPushButton("Inspect")
        buying_code_layout = QHBoxLayout()
        buying_code_layout.addWidget(self.buying_code_edit)
        buying_code_layout.addWidget(inspect_button)
        main_layout.addLayout(buying_code_layout)

        # Connect the Inspect button
        inspect_button.clicked.connect(self.queryBuyingCode)

        # Data Preview
        data_preview_label = QLabel("Data preview")
        main_layout.addWidget(data_preview_label)
        data_preview = QLabel("Description\nLong Description\nSupplier")
        data_preview.setStyleSheet("background-color: white; color: grey; padding: 0.5em;")
        main_layout.addWidget(data_preview)

        # Suggested Sales Code
        suggested_code_label = QLabel("Suggested sales code")
        main_layout.addWidget(suggested_code_label)
        suggested_code_edit = QLineEdit()
        edit_code_button = QPushButton("Edit")
        suggested_code_layout = QHBoxLayout()
        suggested_code_layout.addWidget(suggested_code_edit)
        suggested_code_layout.addWidget(edit_code_button)
        main_layout.addLayout(suggested_code_layout)

        # Suggested Product Type
        product_type_label = QLabel("Suggested product type")
        main_layout.addWidget(product_type_label)
        product_type_edit = QLineEdit()
        edit_type_button = QPushButton("Edit")
        product_type_layout = QHBoxLayout()
        product_type_layout.addWidget(product_type_edit)
        product_type_layout.addWidget(edit_type_button)
        main_layout.addLayout(product_type_layout)

        layout.addLayout(main_layout)

        # Footer
        footer = QHBoxLayout()
        generate_button = QPushButton("Generate")
        generate_button.setStyleSheet("background-color: grey; color: white; padding: 0.5em;")
        footer.addWidget(generate_button)
        layout.addLayout(footer)

        # Set the main window's size
        self.resize(500, 300)

    def connectToDatabase(self):
        conn_str = r'DSN=SysproCompanyN'
        connection =  pyodbc.connect(conn_str)
        self.cursor = connection.cursor()

    def queryBuyingCode(self):
        buying_code = self.buying_code_edit.text()
        query = "SELECT * FROM InvMaster WHERE StockCode = ?;"
        App.cursor.execute(query, buying_code)
        print(App.cursor.fetchone())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())