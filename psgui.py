from PyQt4.QtCore import *
from PyQt4.QtGui import *
import pscore


class PsGui(QWidget):

    def __init__(self, parent=None):
        super(PsGui, self).__init__(parent)
        self.setupUi()
        QTimer.singleShot(0, self.refreshProcessList)

    def setupUi(self):
        self.processList = QTableWidget()
        self.processList.horizontalHeader().setDefaultSectionSize(140)
        # self.processList.horizontalHeader().setStretchLastSection(True)
        self.processList.verticalHeader().setDefaultSectionSize(25)
        self.processList.verticalHeader().setVisible(False)
        self.processList.setEditTriggers(QTableWidget.NoEditTriggers)
        self.processList.setSelectionMode(QTableWidget.SingleSelection)
        self.processList.setSelectionBehavior(QTableWidget.SelectRows)
        self.processList.setColumnCount(3)
        self.processList.setColumnWidth(1, 60)
        self.processList.setHorizontalHeaderLabels(['Name', 'PID', 'Status'])
        self.processList.setAlternatingRowColors(True)
        self.processList.setShowGrid(False)
        self.processList.setSortingEnabled(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.processList)
        self.setLayout(self.layout)
        self.resize(500, 400)

    def refreshProcessList(self):
        currentRow = self.processList.currentRow()
        proc_list = pscore.ps_list()
        self.processList.clearContents()
        self.processList.setRowCount(0)
        for row, proc in enumerate(proc_list):
            self.processList.insertRow(row)
            nameItem = QTableWidgetItem(proc['name'])
            self.processList.setItem(row, 0, nameItem)
            pidItem = TableWidgetItemNumber(QString("%1").arg(proc['pid']))
            # pidItem.setTextAlignment(Qt.AlignCenter)
            self.processList.setItem(row, 1, pidItem)
            statusItem = QTableWidgetItem(proc['status'].capitalize())
            self.processList.setItem(row, 2, statusItem)
        self.processList.selectRow(currentRow)


class TableWidgetItemNumber(QTableWidgetItem):
    def __lt__(self, other):
        return self.text().toInt() < other.text().toInt()
    def __gt__(self, other):
        return self.text().toInt() > other.text().toInt()


def gui_launcher():
    import sys
    from PyQt4.QtGui import QApplication
    app = QApplication(sys.argv)
    win = PsGui()
    win.show()
    return app.exec_()
