import sys
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QMainWindow, QMessageBox
import resources
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer
from PyQt5.QtCore import QSize
from VN3000 import VN3000


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
        self.SvgItems["Waring_VE4"] = {
            "pos": {"x": 153.153, "y": 185.572},
            "state": {"ON": "g1099"},
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
        Creat all messeage boxs
        """
        self.CodeDict = {}
        self.CodeDict[-1] = "Затвор в неопределенном положении!"
        self.CodeDict[-2] = "Турбомолекулярный насос все еще работает!"
        self.CodeDict[-3] = "Клапан VE2 открыт!"
        self.CodeDict[-4] = "Клапан VE3 открыт!"
        self.CodeDict[-5] = "Нет воды для охлаждения турбомолекулярного насоса"
        self.CodeDict[-6] = "Давление больше разрешённого для старта насоса"
        self.CodeDict[-7] = "Затвор не закрыт!"
        self.CodeDict[-8] = "Клапан VE1 открыт!"
        self.CodeDict[-9] = "Камера открыта!"
        self.CodeDict[-10] = "Давление больше разрешённого для включения датчика PG"
        self.CodeDict[-11] = "Проблемы с фазой!"
        self.CodeDict[-12] = "Давление в камере больше разрешенного!"
        self.CodeDict[-13] = "Остановка насоса длиться в течении 50 мин!"

        """
        Text aboout
        """
        self.textAbout = "Программа для управления установкой VN3000.\n"
        self.textAbout += "Данное приложение разработано в 2020, лицензия MIT.\n"
        self.textAbout += "Подробнее на https://github.com/Oerdna/VN3000"

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
        Method change state of NT
        """
        self.pushButton_NT.clicked.connect(self.ButtonNTHandler)

        """
        Method change state of VE1
        """
        self.pushButton_VE1.clicked.connect(self.ButtonVE1Handler)

        """
        Method change state of VE2
        """
        self.pushButton_VE2.clicked.connect(self.ButtonVE2Handler)

        """
        Method change state of VE3
        """
        self.pushButton_VE3.clicked.connect(self.ButtonVE3Handler)

        """
        Method change state of VE4
        """
        self.pushButton_close_VE4.clicked.connect(self.ButtonVE4close)
        self.pushButton_open_VE4.clicked.connect(self.ButtonVE4open)

        """
        Method disable sound
        """
        self.pushButton_disVolume.clicked.connect(self.ButtonVolume)

        """
        Method open window about
        """
        self.pushButton_About.clicked.connect(self.ButtonAbout)

        """
        Method open/close valve ZQ1/ZQ2
        """
        self.checkBox_ZQ1.stateChanged.connect(self.checkBoxZQ1)
        self.spinBox_ZQ1.valueChanged.connect(self.changeZQ1)
        self.checkBox_ZQ2.stateChanged.connect(self.checkBoxZQ2)
        self.spinBox_ZQ2.valueChanged.connect(self.changeZQ2)

        """
        Method to control of substrate
        """
        self.checkBox_rotation_substrate.stateChanged.connect(self.checkBoxRotationSub)
        self.spinBox_Speed.valueChanged.connect(self.changeRotationSub)
        self.checkBox_currnet_heat.stateChanged.connect(self.checkBoxHeatSub)
        self.spinBox_current_heat.valueChanged.connect(self.changeHeatSub)

        """
        Method open window with setting
        """
        # self.pushButton_settings.clicked.connect()

        """
        Add and rule scene - scheme
        """
        self.scene = Scene()
        self.graphicsView.setScene(self.scene)

        """
        Self rule
        """
        self.vn3000 = VN3000()
        self.vn3000.star_work()
        self.DialogMsg(self.vn3000.check_phase())

    """
    Control of substrate
    """

    def checkBoxHeatSub(self, state):
        if state == QtCore.Qt.Checked:
            self.vn3000.enable_heat_sub(self.vn3000.get_heat_sub())
        else:
            self.vn3000.disable_heat_sub()

    def checkBoxRotationSub(self, state):
        if state == QtCore.Qt.Checked:
            self.vn3000.enable_rotation_sub(self.vn3000.get_rotation_sub())
        else:
            self.vn3000.disable_rotation_sub()

    def changeHeatSub(self):
        self.vn3000.change_heat_sub(self.spinBox_current_heat.value())
        if self.checkBox_currnet_heat.isChecked() == True:
            self.vn3000.enable_heat_sub(self.vn3000.get_heat_sub())

    def changeRotationSub(self):
        self.vn3000.change_rotation_sub(self.spinBox_Speed.value())
        if self.checkBox_rotation_substrate.isChecked() == True:
            self.vn3000.enable_rotation_sub(self.vn3000.get_rotation_sub())

    """
    Inlet gas ZQ1/ZQ2 open/close
    """

    def checkBoxZQ1(self, state):
        if state == QtCore.Qt.Checked:
            self.vn3000.enable_inlent_ZQ1(self.vn3000.get_ZQ1())
            self.scene.SvgObjs["ZQ1"]["ON"].setVisible(True)
        else:
            self.vn3000.close_ZQ1()
            self.scene.SvgObjs["ZQ1"]["ON"].setVisible(False)

    def checkBoxZQ2(self, state):
        if state == QtCore.Qt.Checked:
            self.vn3000.enable_inlent_ZQ2(self.vn3000.get_ZQ2())
            self.scene.SvgObjs["ZQ2"]["ON"].setVisible(True)
        else:
            self.vn3000.close_ZQ2()
            self.scene.SvgObjs["ZQ2"]["ON"].setVisible(False)

    def changeZQ1(self):
        self.vn3000.change_ZQ1(self.spinBox_ZQ1.value())
        if self.checkBox_ZQ1.isChecked() == True:
            self.vn3000.enable_inlent_ZQ1(self.vn3000.get_ZQ1())

    def changeZQ2(self):
        self.vn3000.change_ZQ2(self.spinBox_ZQ2.value())
        if self.checkBox_ZQ2.isChecked() == True:
            self.vn3000.enable_inlent_ZQ2(self.vn3000.get_ZQ2())

    """
    About - I have spoken
    """

    def ButtonAbout(self):
        MsgAbout = QMessageBox.about(self, "About VN3000", self.textAbout)

    """
    Volume - only disable
    """

    def ButtonVolume(self):
        self.vn3000.disable_sound()

    """
    VE4 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE4open(self):
        self.DialogMsg(self.vn3000.open_VE4())
        self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(False)
        self.scene.SvgObjs["VE4"]["ON"].setVisible(True)

    def ButtonVE4close(self):
        self.DialogMsg(self.vn3000.close_VE4())
        self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(True)
        self.scene.SvgObjs["VE4"]["ON"].setVisible(False)

    """
    VE3 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE3Handler(self):
        if self.pushButton_VE3.isChecked():
            self.EnableVE3()
        else:
            self.DisableVE3()

    def EnableVE3(self):
        self.DialogMsg(self.vn3000.open_VE3())
        self.scene.SvgObjs["VE3"]["ON"].setVisible(True)

    def DisableVE3(self):
        self.DialogMsg(self.vn3000.close_VE3())
        self.scene.SvgObjs["VE3"]["ON"].setVisible(False)

    """
    VE2 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE2Handler(self):
        if self.pushButton_VE2.isChecked():
            self.EnableVE2()
        else:
            self.DisableVE2()

    def EnableVE2(self):
        self.DialogMsg(self.vn3000.open_VE2())
        self.scene.SvgObjs["VE2"]["ON"].setVisible(True)

    def DisableVE2(self):
        self.DialogMsg(self.vn3000.close_VE2())
        self.scene.SvgObjs["VE2"]["ON"].setVisible(False)

    """
    VE1 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE1Handler(self):
        if self.pushButton_VE1.isChecked():
            self.EnableVE1()
        else:
            self.DisableVE1()

    def EnableVE1(self):
        self.DialogMsg(self.vn3000.open_VE1())
        self.scene.SvgObjs["VE1"]["ON"].setVisible(True)

    def DisableVE1(self):
        self.DialogMsg(self.vn3000.close_VE1())
        self.scene.SvgObjs["VE1"]["ON"].setVisible(False)

    """
    NT - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonNTHandler(self):
        if self.pushButton_NT.isChecked():
            self.EnableNT()
        else:
            self.DisableNT()

    def EnableNT(self):
        self.DialogMsg(self.vn3000.enable_NT())
        self.scene.SvgObjs["NT"]["WAIT"].setVisible(True)

    def DisableNT(self):
        self.DialogMsg(self.vn3000.disable_NT())
        self.scene.SvgObjs["NT"]["WAIT"].setVisible(False)

    """
    NF - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonNFHandler(self):
        if self.pushButton_NF.isChecked():
            self.EnableNF()
        else:
            self.DisableNF()

    def EnableNF(self):
        self.DialogMsg(self.vn3000.enable_NF())
        self.scene.SvgObjs["NF"]["ON"].setVisible(True)

    def DisableNF(self):
        self.DialogMsg(self.vn3000.disable_NF())
        self.scene.SvgObjs["NF"]["ON"].setVisible(False)

    """
    PG - Handler: anable and disable. Checking conditions for reduce crash of installation
    """

    def ButtonPGHandler(self):
        if self.pushButton_PG.isChecked():
            self.EnablePG()
        else:
            self.DisablePG()

    def EnablePG(self):
        self.DialogMsg(self.vn3000.enable_PG())
        self.progressBar_PG.setVisible(True)
        self.label_isPG.setVisible(True)
        self.label_pressure_PG.setVisible(True)
        self.label_PG.setVisible(True)

    def DisablePG(self):
        self.progressBar_PG.setVisible(False)
        self.label_isPG.setVisible(False)
        self.label_pressure_PG.setVisible(False)
        self.label_PG.setVisible(False)

    def DialogMsg(self, ErrorCode: int):
        print("Error Code: ", ErrorCode)
        if ErrorCode != None:
            msg = QMessageBox.warning(self, "Message Warning", self.CodeDict[ErrorCode])

    def closeEvent(self, event):
        close = QMessageBox.question(
            self,
            "Quit",
            "Вы уверены, что хотите закрыть программу?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if close == QMessageBox.Yes:
            self.vn3000.end_work()
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
