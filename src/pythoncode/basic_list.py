import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class TodoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TODO List')
        self.setGeometry(1000, 500, 400, 300)

        layout = QVBoxLayout()

        self.taskEdit = QLineEdit(self)
        self.taskEdit.setPlaceholderText('Enter a task...')
        layout.addWidget(self.taskEdit)

        self.addButton = QPushButton('Add Task', self)
        self.addButton.clicked.connect(self.addTask)
        layout.addWidget(self.addButton)

        self.tasksList = QListWidget(self)
        self.tasksList.doubleClicked.connect(self.removeTask)
        layout.addWidget(self.tasksList)

        self.setLayout(layout)

    def addTask(self):
        taskText = self.taskEdit.text()
        if taskText:  # Only add non-empty tasks
            self.tasksList.addItem(taskText)
            self.taskEdit.clear()

    def removeTask(self):
        for item in self.tasksList.selectedItems():
            self.tasksList.takeItem(self.tasksList.row(item))

def main():
    app = QApplication(sys.argv)
    ex = TodoListApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
