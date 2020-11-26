import sys
import math
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
            "state": {"ON": "g282"},
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
        self.CodeDict[-13] = "Остановка насоса длится в течении 50 мин!"
        self.CodeDict[-14] = "Нет охлаждения магнетрона!"
        self.CodeDict[-15] = "Блок DC магнетрона не включён!"
        self.CodeDict[-16] = "Нет связи с блоком DC магнетрона!"
        self.CodeDict[-17] = "Нет связи с блоком RF магнетрона!"
        self.CodeDict[-18] = "Блок RF магнетрона не включён!"
        self.CodeDict[-19] = "Блок RF магнетрона еще не готов к работе!"
        """
        Text aboout
        """
        self.textAbout = "Программа для управления установкой VN3000.\n"
        self.textAbout += "Данное приложение разработано в 2020, лицензия MIT.\n"
        self.textAbout += "Подробнее на https://github.com/Oerdna/VN3000"

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
        Method to control DC block
        """
        self.pushButton_enableDcBlock.clicked.connect(self.ButtonDCHandler)
        self.pushButton_CurrentDcMagnetron.clicked.connect(self.ButtonSputteringHandler)
        self.spinBox_CurrentDcMagnetron.valueChanged.connect(self.changeDCcurrent)

        """
        Method to control RF block
        """
        self.pushButton_enableRfBlock.clicked.connect(self.ButtonRFHandler)
        self.pushButton_sputteringRFcheck.clicked.connect(self.ButtonRFcheckHandler)
        self.pushButton_sputteringRF.clicked.connect(self.ButtonRFsputteringHandler)
        self.spinBox_powerRfMagnetron.valueChanged.connect(self.changeRFcurrent)
        self.pushButton_upC1.pressed.connect(self.ButtonCap1upPressed)
        self.pushButton_upC2.pressed.connect(self.ButtonCap2upPressed)
        self.pushButton_downC1.pressed.connect(self.ButtonCap1downPressed)
        self.pushButton_downC2.pressed.connect(self.ButtonCap2downPressed)
        self.pushButton_upC1.released.connect(self.ButtonCap1upReleased)
        self.pushButton_upC2.released.connect(self.ButtonCap2upReleased)
        self.pushButton_downC1.released.connect(self.ButtonCap1downReleased)
        self.pushButton_downC2.released.connect(self.ButtonCap2downReleased)

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
        self.updateStatus()
        """
        Hide the PG pressure bar and label with data in init method
        """
        self.DisablePG()

        """
        Run the updater screen
        """
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.updateMeasurement)
        self.timer.start()

    """
    Control Rf block
    """

    def ButtonRFHandler(self):
        if self.pushButton_enableRfBlock.isChecked():
            self.DialogMsg(self.vn3000.enable_rf_block(), self.pushButton_enableRfBlock)
        else:
            self.DialogMsg(
                self.vn3000.disable_rf_block(), self.pushButton_enableRfBlock
            )

    def ButtonRFcheckHandler(self):
        if self.pushButton_sputteringRFcheck.isChecked():
            self.DialogMsg(
                self.vn3000.cheking_rf_sputtering(), self.pushButton_sputteringRFcheck
            )
        else:
            self.DialogMsg(
                self.vn3000.disable_cheking_rf_sputtering(),
                self.pushButton_sputteringRFcheck,
            )

    def ButtonRFsputteringHandler(self):
        if self.pushButton_sputteringRF.isChecked():
            self.DialogMsg(
                self.vn3000.enable_rf_sputtering(self.vn3000.get_rf_sputtering()),
                self.pushButton_sputteringRF,
            )
        else:
            self.DialogMsg(
                self.vn3000.disable_rf_sputtering(), self.pushButton_sputteringRF
            )

    def changeRFcurrent(self):
        self.vn3000.change_rf_sputtering(self.spinBox_powerRfMagnetron.value())
        if self.pushButton_sputteringRF.isChecked() == True:
            self.vn3000.enable_rf_sputtering(self.vn3000.get_rf_sputtering())

    def ButtonCap1upPressed(self):
        self.vn3000.Cap1upStart()

    def ButtonCap2upPressed(self):
        self.vn3000.Cap2upStart()

    def ButtonCap1downPressed(self):
        self.vn3000.Cap1downStart()

    def ButtonCap2downPressed(self):
        self.vn3000.Cap2downStart()

    def ButtonCap1upReleased(self):
        self.vn3000.Cap1upStop()

    def ButtonCap2upReleased(self):
        self.vn3000.Cap2upStop()

    def ButtonCap1downReleased(self):
        self.vn3000.Cap1downStop()

    def ButtonCap2downReleased(self):
        self.vn3000.Cap2downStop()

    """
    Control Dc block
    """

    def ButtonDCHandler(self):
        if self.pushButton_enableDcBlock.isChecked():
            self.DialogMsg(self.vn3000.enable_dc_block(), self.pushButton_enableDcBlock)
        else:
            self.DialogMsg(
                self.vn3000.disable_dc_block(), self.pushButton_enableDcBlock
            )

    def ButtonSputteringHandler(self):
        if self.pushButton_CurrentDcMagnetron.isChecked():
            self.DialogMsg(
                self.vn3000.enable_dc_sputtering(self.vn3000.get_dc_sputtering()),
                self.pushButton_CurrentDcMagnetron,
            )
        else:
            self.DialogMsg(
                self.vn3000.disable_dc_sputtering(), self.pushButton_CurrentDcMagnetron
            )

    def changeDCcurrent(self):
        self.vn3000.change_dc_sputtering(self.spinBox_CurrentDcMagnetron.value())
        if self.pushButton_CurrentDcMagnetron.isChecked() == True:
            self.vn3000.enable_dc_sputtering(self.vn3000.get_dc_sputtering())

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
        else:
            self.vn3000.close_ZQ1()

    def checkBoxZQ2(self, state):
        if state == QtCore.Qt.Checked:
            self.vn3000.enable_inlent_ZQ2(self.vn3000.get_ZQ2())
        else:
            self.vn3000.close_ZQ2()

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

    def ButtonVE4close(self):
        self.DialogMsg(self.vn3000.close_VE4())

    """
    VE3 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE3Handler(self):
        if self.pushButton_VE3.isChecked():
            self.DialogMsg(self.vn3000.open_VE3(), self.pushButton_VE3)
        else:
            self.DialogMsg(self.vn3000.close_VE3(), self.pushButton_VE3)

    """
    VE2 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE2Handler(self):
        if self.pushButton_VE2.isChecked():
            self.DialogMsg(self.vn3000.open_VE2(), self.pushButton_VE2)
        else:
            self.DialogMsg(self.vn3000.close_VE2(), self.pushButton_VE2)

    """
    VE1 - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonVE1Handler(self):
        if self.pushButton_VE1.isChecked():
            self.DialogMsg(self.vn3000.open_VE1(), self.pushButton_VE1)
        else:
            self.DialogMsg(self.vn3000.close_VE1(), self.pushButton_VE1)

    """
    NT - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonNTHandler(self):
        if self.pushButton_NT.isChecked():
            self.DialogMsg(self.vn3000.enable_NT(), self.pushButton_NT)
        else:
            self.DialogMsg(self.vn3000.disable_NT(), self.pushButton_NT)

    """
    NF - Handler: aneble and disable. Checking conditions for reduce crash of installation
    """

    def ButtonNFHandler(self):
        if self.pushButton_NF.isChecked():
            self.DialogMsg(self.vn3000.enable_NF(), self.pushButton_NF)
        else:
            self.DialogMsg(self.vn3000.disable_NF(), self.pushButton_NF)

    """
    PG - Handler: anable and disable. Checking conditions for reduce crash of installation
    """

    def ButtonPGHandler(self):
        if self.pushButton_PG.isChecked():
            self.EnablePG()
        else:
            self.DisablePG()

    def EnablePG(self):
        self.DialogMsg(self.vn3000.enable_PG(), self.pushButton_PG)
        if self.pushButton_PG.isChecked():
            self.progressBar_PG.setVisible(True)
            self.label_isPG.setVisible(True)
            self.label_pressure_PG.setVisible(True)
            self.label_PG.setVisible(True)

    def DisablePG(self):
        self.vn3000.disable_PG()
        self.progressBar_PG.setVisible(False)
        self.label_isPG.setVisible(False)
        self.label_pressure_PG.setVisible(False)
        self.label_PG.setVisible(False)

    """
    Cheking return Error
    """

    def DialogMsg(self, ErrorCode: int, Button: object = None):
        print("Error Code: ", ErrorCode)
        if ErrorCode != None:
            msg = QMessageBox.warning(self, "Message Warning", self.CodeDict[ErrorCode])
            if Button != None:
                Button.toggle()

    """
    Cheking close Window
    """

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

    def updateMeasurement(self):
        """
        Update the labels every 0.5 seconds using a QTimer
        """
        self.vn3000.get_measurements()
        """
        Get kwargs from VN3000
        """
        kwargsMeas = self.vn3000.get_values_for_update()
        """
        Set text labels by .formats
        """
        self.label_isP1.setText("{pressure_ch:.2E}, мм. рт. ст.".format(**kwargsMeas))
        self.label_isP2.setText("{pressure_pmp:.2E}, мм. рт. ст.".format(**kwargsMeas))
        self.label_isPG.setText("{pressure_pg:.2E}, мм. рт. ст.".format(**kwargsMeas))
        self.label_isP1_U.setText("{mes_pmt6_1:.2f}, В".format(**kwargsMeas))
        self.label_isP2_U.setText("{mes_pmt6_2:.2f}, В".format(**kwargsMeas))
        self.label_isZQ1_U.setText("{mes_ZQ1_voltage}, ед.".format(**kwargsMeas))
        self.label_isZQ2_U.setText("{mes_ZQ2_voltage}, ед.".format(**kwargsMeas))
        self.label_isPG_I.setText("{mes_pg_current:.2f}, мА".format(**kwargsMeas))
        self.label_istemperature.setText("{mes_temperature}, ℃".format(**kwargsMeas))
        self.label_iscurrent_heat.setText("{mes_current}, А".format(**kwargsMeas))
        self.label_isspeed.setText("{mes_speed}, об/мин".format(**kwargsMeas))
        self.label_isI_DcMagnetron.setText("{mes_current_dc}, мА".format(**kwargsMeas))
        self.label_isU_DcMagnetron.setText("{mes_voltage_dc}, В".format(**kwargsMeas))
        self.label_isPowerRf.setText("{mes_rf_Power:.2f}, Вт").format(**kwargsMeas)
        self.label_isKBV.setText("{mes_rf_KBV:.3f}").format(**kwargsMeas)
        self.label_isI_RfAnode.setText("{mes_rf_Ianod:.2f}, мА").format(**kwargsMeas)
        self.label_IsI_RfDriver.setText("{mes_rf_Idriver:.2f}, мА").format(**kwargsMeas)
        self.label_isU_RfMagnetron.setText("{mes_rf_Umagn:.2f}, В").format(**kwargsMeas)
        self.label_IsI_RfMagnetron.setText("{mes_rf_Imagn:.2f}, мА").format(
            **kwargsMeas
        )
        """
        Check waters
        """
        if kwargsMeas["water_1"]:
            self.WaterSensor1.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100.png")
            )
        else:
            self.WaterSensor1.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
            )
        if kwargsMeas["water_2"]:
            self.WaterSensor2.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100.png")
            )
        else:
            self.WaterSensor2.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
            )
        if kwargsMeas["water_3"]:
            self.WaterSensor3.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100.png")
            )
        else:
            self.WaterSensor3.setPixmap(
                QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
            )
        """
        Set bar widget in log scale
        """
        kwargsMeas["pressure_ch"] = (
            2e-3 if kwargsMeas["pressure_ch"] < 2e-3 else kwargsMeas["pressure_ch"]
        )
        self.progressBar_P1.setValue(
            round(math.log10(kwargsMeas["pressure_ch"] * 133)) * 100
        )
        kwargsMeas["pressure_pmp"] = (
            2e-3 if kwargsMeas["pressure_pmp"] < 2e-3 else kwargsMeas["pressure_pmp"]
        )
        self.progressBar_P2.setValue(
            round(math.log10(kwargsMeas["pressure_pmp"] * 133)) * 100
        )
        kwargsMeas["pressure_pg"] = (
            7.5e-8 if kwargsMeas["pressure_pg"] < 7.5e-8 else kwargsMeas["pressure_pg"]
        )
        self.progressBar_PG.setValue(
            round(math.log10(kwargsMeas["pressure_pg"] * 133)) * 100
        )
        """
        Set SvgItems
        """
        self.scene.SvgObjs["VE1"]["ON"].setVisible(kwargsMeas["state_VE1"])
        self.scene.SvgObjs["VE2"]["ON"].setVisible(kwargsMeas["state_VE2"])
        self.scene.SvgObjs["VE3"]["ON"].setVisible(kwargsMeas["state_VE3"])
        self.scene.SvgObjs["ZQ1"]["ON"].setVisible(kwargsMeas["state_ZQ1"])
        self.scene.SvgObjs["ZQ2"]["ON"].setVisible(kwargsMeas["state_ZQ2"])
        self.scene.SvgObjs["NF"]["ON"].setVisible(kwargsMeas["state_NF"])
        self.scene.SvgObjs["CMB"]["ON"].setVisible(kwargsMeas["state_chmb_open"])
        """NT Logic
        """
        if kwargsMeas["turbine_active"]:
            self.scene.SvgObjs["NT"]["ON"].setVisible(True)
            self.scene.SvgObjs["NT"]["WAIT"].setVisible(False)
        else:
            self.scene.SvgObjs["NT"]["WAIT"].setVisible(kwargsMeas["state_NT"])
        """VE4 Logic
        """
        if kwargsMeas["state_VE4_close"]:
            self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(True)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)
        elif kwargsMeas["state_VE4_open"]:
            self.scene.SvgObjs["VE4"]["ON"].setVisible(True)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)
        elif (
            kwargsMeas["state_VE4_open"] == False
            and kwargsMeas["state_VE4_close"] == False
        ) and (
            kwargsMeas["state_comand_open_VE4"] == False
            and kwargsMeas["state_comand_close_VE4"] == False
        ):
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(True)
        else:
            self.scene.SvgObjs["VE4"]["ON"].setVisible(False)
            self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(False)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)

    def updateStatus(self):
        """
        Update states
        """
        kwargsStats = self.vn3000.get_values_for_states()
        """
        Change labels and widgets
        """
        self.pushButton_VE1.setChecked(kwargsStats["state_VE1"])
        self.pushButton_VE2.setChecked(kwargsStats["state_VE2"])
        self.pushButton_VE3.setChecked(kwargsStats["state_VE3"])
        self.pushButton_NF.setChecked(kwargsStats["state_NF"])
        self.pushButton_NT.setChecked(kwargsStats["state_NT"])
        self.checkBox_ZQ1.setChecked(kwargsStats["state_ZQ1"])
        self.spinBox_ZQ1.setValue(kwargsStats["set_voltage_ZQ1"])
        self.checkBox_ZQ2.setChecked(kwargsStats["state_ZQ2"])
        self.spinBox_ZQ2.setValue(kwargsStats["set_voltage_ZQ2"])
        self.checkBox_currnet_heat.setChecked(kwargsStats["state_heat"])
        self.spinBox_current_heat.setValue(kwargsStats["seted_cur_heat"])
        self.checkBox_rotation_substrate.setChecked(kwargsStats["state_rotation"])
        self.spinBox_Speed.setValue(kwargsStats["seted_rot_speed"])
        self.spinBox_CurrentDcMagnetron.setValue(kwargsStats["range_current"])
        self.pushButton_enableDcBlock.setChecked(kwargsStats["block_dc_enable"])
        self.pushButton_CurrentDcMagnetron.setChecked(kwargsStats["current_state"])
        self.spinBox_powerRfMagnetron.setValue(kwargsStats["range_power"])
        self.pushButton_enableRfBlock.setChecked(kwargsStats["block_rf_enable"])
        self.pushButton_sputteringRFcheck.setChecked(kwargsStats["block_rf_sputtering"])
        self.pushButton_sputteringRF.setChecked(kwargsStats["block_rf_set_power"])

        """PG Logic
        """
        if kwargsStats["state_PG"] == True:
            self.pushButton_PG.setChecked(kwargsStats["state_PG"])
            self.EnablePG()
        """
        Set SvgItems
        """
        self.scene.SvgObjs["VE2"]["ON"].setVisible(kwargsStats["state_VE2"])
        self.scene.SvgObjs["VE1"]["ON"].setVisible(kwargsStats["state_VE1"])
        self.scene.SvgObjs["VE3"]["ON"].setVisible(kwargsStats["state_VE3"])
        self.scene.SvgObjs["ZQ1"]["ON"].setVisible(kwargsStats["state_ZQ1"])
        self.scene.SvgObjs["ZQ2"]["ON"].setVisible(kwargsStats["state_ZQ2"])
        self.scene.SvgObjs["NF"]["ON"].setVisible(kwargsStats["state_NF"])
        self.scene.SvgObjs["NT"]["WAIT"].setVisible(kwargsStats["state_NT"])
        self.scene.SvgObjs["CMB"]["ON"].setVisible(kwargsStats["state_chmb_open"])
        """VE4 Logic
        """
        if kwargsStats["state_VE4_close"]:
            self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(True)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)
        elif kwargsStats["state_VE4_open"]:
            self.scene.SvgObjs["VE4"]["ON"].setVisible(True)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)
        elif (
            kwargsStats["state_VE4_open"] == False
            and kwargsStats["state_VE4_close"] == False
        ) and (
            kwargsStats["state_comand_open_VE4"] == False
            and kwargsStats["state_comand_close_VE4"] == False
        ):
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(True)
        else:
            self.scene.SvgObjs["VE4"]["ON"].setVisible(False)
            self.scene.SvgObjs["VE4"]["CLOSE"].setVisible(False)
            self.scene.SvgObjs["Waring_VE4"]["ON"].setVisible(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
