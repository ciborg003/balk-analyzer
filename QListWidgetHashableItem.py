from PyQt5.QtWidgets import QListWidgetItem


class QListWidgetHashableItem(QListWidgetItem):

    def __hash__(self):
        return self.text()[:self.text().index('.')].__hash__()