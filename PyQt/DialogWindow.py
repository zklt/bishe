from PyQt5.QtWidgets import QDialog
import dialog


class DialogWindow(QDialog):
    def __init__(self,p):
        super(DialogWindow, self).__init__(parent=p)
        self.ui = dialog.Ui_Dialog()
        self.ui.setupUi(self)