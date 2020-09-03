import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QMainWindow
import resources
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtCore import QSize


class Scene(QGraphicsScene):
    def __init__(self):
        super().__init__()
        """
        Set background SVG
        """
        self.setSceneRect(0, 0, 360, 360)
        self.SvgBack = QGraphicsSvgItem("./images/scene.svg")
        self.addItem(self.SvgBack)

        """
        Creat item - nodes which indicate self state
        pos: coordinate get in SVG
        state: id and number of states
        """
        self.SvgItems = {}
        self.SvgItems["CMB"] = {
            "pos": {"x": 165.580, "y": 70.295},
            "state": {"ON": "g2561"},
        }
        self.SvgItems["VE1"] = {
            "pos": {"x": 55.222, "y": 34.117},
            "state": {"ON": "g1745"},
        }
        self.SvgItems["VE2"] = {
            "pos": {"x": 228.073, "y": 282.911},
            "state": {"ON": "g1745"},
        }
        self.SvgItems["VE3"] = {
            "pos": {"x": 254.651, "y": 106.019},
            "state": {"ON": "g1745"},
        }
        self.SvgItems["ZQ1"] = {
            "pos": {"x": 55.22, "y": 92.367},
            "state": {"ON": "g1745"},
        }
        self.SvgItems["ZQ2"] = {
            "pos": {"x": 55.22, "y": 169.605},
            "state": {"ON": "g1745"},
        }
        self.SvgItems["NF"] = {
            "pos": {"x": 290.707, "y": 272.899},
            "state": {"ON": "g1102"},
        }
        self.SvgItems["NT"] = {
            "pos": {"x": 150.412, "y": 272.873},
            "state": {"ON": "g2867", "WAIT": "g2878"},
        }
        self.SvgItems["VE4"] = {
            "pos": {"x": 146.480, "y": 178.316},
            "state": {"ON": "g414", "CLOSE": "g404"},
        }

        """
        Gen items for QGraphicsScene and set it invisible on start GUI
        """
        self.SvgObjs = {}
        for key, items in self.SvgItems.items():
            self.SvgObjs[key] = {}
            for state, idname in items["state"].items():
                self.SvgObjs[key][state] = QGraphicsSvgItem("./images/scene.svg")
                self.SvgObjs[key][state].setElementId(idname)
                self.addItem(self.SvgObjs[key][state])
                self.SvgObjs[key][state].setPos(items["pos"]["x"], items["pos"]["y"])
                self.SvgObjs[key][state].setVisible(False)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("startup.ui", self)

        """
        Hide the PG pressure bar and label with data in init method
        """
        self.DisablePG()

        """
        Method enable the work PG sensor
        """
        self.pushButton_PG.clicked.connect(self.ButtonPGHandler)

        """
        Method change state of NT
        """
        self.pushButton_NF.clicked.connect(self.ButtonNFHandler)
        """
        Add and rule scene - scheme
        """
        self.scene = Scene()
        self.graphicsView.setScene(self.scene)

    """
    NF - Handler: anable and disable. Checking conditions for reduce crash of installation
    """

    def ButtonNFHandler(self):
        if self.pushButton_NF.isChecked():
            self.EnableNF()
        else:
            self.DisableNF()

    def EnableNF(self):
        self.scene.SvgObjs["NF"]["ON"].setVisible(True)

    def DisableNF(self):
        self.scene.SvgObjs["NF"]["ON"].setVisible(False)

    def ButtonPGHandler(self):
        if self.pushButton_PG.isChecked():
            self.EnablePG()
        else:
            self.DisablePG()

    def EnablePG(self):
        self.progressBar_PG.setVisible(True)
        self.label_isPG.setVisible(True)
        self.label_pressure_PG.setVisible(True)
        self.label_PG.setVisible(True)

    def DisablePG(self):
        self.progressBar_PG.setVisible(False)
        self.label_isPG.setVisible(False)
        self.label_pressure_PG.setVisible(False)
        self.label_PG.setVisible(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
