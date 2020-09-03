# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/main_icon.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "QMainWindow, QTabBar, QTabWidget, QPushButton, QLabel, QSpinBox, QCheckBox, QGroupBox{\n"
            '    font: 11pt "MS Shell Dlg 2";\n'
            "}"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget_blockRasp_blockUpr = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_blockRasp_blockUpr.setFont(font)
        self.tabWidget_blockRasp_blockUpr.setAutoFillBackground(True)
        self.tabWidget_blockRasp_blockUpr.setUsesScrollButtons(False)
        self.tabWidget_blockRasp_blockUpr.setDocumentMode(False)
        self.tabWidget_blockRasp_blockUpr.setTabsClosable(False)
        self.tabWidget_blockRasp_blockUpr.setMovable(False)
        self.tabWidget_blockRasp_blockUpr.setObjectName("tabWidget_blockRasp_blockUpr")
        self.tab_blockRasp = QtWidgets.QWidget()
        self.tab_blockRasp.setObjectName("tab_blockRasp")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_blockRasp)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_1_blockRasp = QtWidgets.QGridLayout()
        self.gridLayout_1_blockRasp.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_1_blockRasp.setSpacing(6)
        self.gridLayout_1_blockRasp.setObjectName("gridLayout_1_blockRasp")
        self.spinBox_current_heat = QtWidgets.QSpinBox(self.tab_blockRasp)
        self.spinBox_current_heat.setMaximum(550)
        self.spinBox_current_heat.setObjectName("spinBox_current_heat")
        self.gridLayout_1_blockRasp.addWidget(self.spinBox_current_heat, 0, 1, 1, 1)
        self.checkBox_rotation_substrate = QtWidgets.QCheckBox(self.tab_blockRasp)
        self.checkBox_rotation_substrate.setObjectName("checkBox_rotation_substrate")
        self.gridLayout_1_blockRasp.addWidget(
            self.checkBox_rotation_substrate, 1, 0, 1, 1
        )
        self.spinBox_Speed = QtWidgets.QSpinBox(self.tab_blockRasp)
        self.spinBox_Speed.setMaximum(100)
        self.spinBox_Speed.setObjectName("spinBox_Speed")
        self.gridLayout_1_blockRasp.addWidget(self.spinBox_Speed, 1, 1, 1, 1)
        self.checkBox_currnet_heat = QtWidgets.QCheckBox(self.tab_blockRasp)
        self.checkBox_currnet_heat.setObjectName("checkBox_currnet_heat")
        self.gridLayout_1_blockRasp.addWidget(self.checkBox_currnet_heat, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_1_blockRasp.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_1_blockRasp.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_1_blockRasp)
        self.gridLayout_2_blockRasp = QtWidgets.QGridLayout()
        self.gridLayout_2_blockRasp.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2_blockRasp.setSpacing(6)
        self.gridLayout_2_blockRasp.setObjectName("gridLayout_2_blockRasp")
        self.pushButton_NT = QtWidgets.QPushButton(self.tab_blockRasp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/turbine.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_NT.setIcon(icon1)
        self.pushButton_NT.setCheckable(True)
        self.pushButton_NT.setObjectName("pushButton_NT")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_NT, 0, 1, 1, 1)
        self.pushButton_NL = QtWidgets.QPushButton(self.tab_blockRasp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-pump-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_NL.setIcon(icon2)
        self.pushButton_NL.setCheckable(True)
        self.pushButton_NL.setAutoDefault(False)
        self.pushButton_NL.setDefault(False)
        self.pushButton_NL.setFlat(False)
        self.pushButton_NL.setObjectName("pushButton_NL")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_NL, 0, 0, 1, 1)
        self.pushButton_close_VE4 = QtWidgets.QPushButton(self.tab_blockRasp)
        self.pushButton_close_VE4.setObjectName("pushButton_close_VE4")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_close_VE4, 1, 1, 1, 1)
        self.pushButton_open_VE4 = QtWidgets.QPushButton(self.tab_blockRasp)
        self.pushButton_open_VE4.setObjectName("pushButton_open_VE4")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_open_VE4, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2_blockRasp)
        self.groupBox_meas_rasp = QtWidgets.QGroupBox(self.tab_blockRasp)
        self.groupBox_meas_rasp.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.groupBox_meas_rasp.setAcceptDrops(False)
        self.groupBox_meas_rasp.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.groupBox_meas_rasp.setFlat(True)
        self.groupBox_meas_rasp.setCheckable(False)
        self.groupBox_meas_rasp.setObjectName("groupBox_meas_rasp")
        self.formLayout_3_blockRasp = QtWidgets.QFormLayout(self.groupBox_meas_rasp)
        self.formLayout_3_blockRasp.setObjectName("formLayout_3_blockRasp")
        self.label_temperature = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_temperature.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_temperature.setObjectName("label_temperature")
        self.formLayout_3_blockRasp.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_temperature
        )
        self.label_istemperature = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_istemperature.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_istemperature.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_istemperature.setObjectName("label_istemperature")
        self.formLayout_3_blockRasp.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_istemperature
        )
        self.label_current_heat = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_current_heat.setObjectName("label_current_heat")
        self.formLayout_3_blockRasp.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_current_heat
        )
        self.label_iscurrent_heat = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_iscurrent_heat.setObjectName("label_iscurrent_heat")
        self.formLayout_3_blockRasp.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_iscurrent_heat
        )
        self.label_speed = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_speed.setObjectName("label_speed")
        self.formLayout_3_blockRasp.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_speed
        )
        self.label_isspeed = QtWidgets.QLabel(self.groupBox_meas_rasp)
        self.label_isspeed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_isspeed.setObjectName("label_isspeed")
        self.formLayout_3_blockRasp.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_isspeed
        )
        self.verticalLayout_3.addWidget(self.groupBox_meas_rasp)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-integrated-circuit-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_blockRasp_blockUpr.addTab(self.tab_blockRasp, icon3, "")
        self.tab_blockUpr = QtWidgets.QWidget()
        self.tab_blockUpr.setObjectName("tab_blockUpr")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_blockUpr)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_1_blockUpr = QtWidgets.QGridLayout()
        self.gridLayout_1_blockUpr.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_1_blockUpr.setSpacing(6)
        self.gridLayout_1_blockUpr.setObjectName("gridLayout_1_blockUpr")
        self.checkBox_ZQ2 = QtWidgets.QCheckBox(self.tab_blockUpr)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-shampoo-100_2.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.checkBox_ZQ2.setIcon(icon4)
        self.checkBox_ZQ2.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_ZQ2.setObjectName("checkBox_ZQ2")
        self.gridLayout_1_blockUpr.addWidget(self.checkBox_ZQ2, 1, 0, 1, 1)
        self.checkBox_ZQ1 = QtWidgets.QCheckBox(self.tab_blockUpr)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-shampoo-100_1.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.checkBox_ZQ1.setIcon(icon5)
        self.checkBox_ZQ1.setIconSize(QtCore.QSize(24, 24))
        self.checkBox_ZQ1.setTristate(False)
        self.checkBox_ZQ1.setObjectName("checkBox_ZQ1")
        self.gridLayout_1_blockUpr.addWidget(self.checkBox_ZQ1, 0, 0, 1, 1)
        self.spinBox_ZQ1 = QtWidgets.QSpinBox(self.tab_blockUpr)
        self.spinBox_ZQ1.setMaximum(255)
        self.spinBox_ZQ1.setObjectName("spinBox_ZQ1")
        self.gridLayout_1_blockUpr.addWidget(self.spinBox_ZQ1, 0, 1, 1, 1)
        self.spinBox_ZQ2 = QtWidgets.QSpinBox(self.tab_blockUpr)
        self.spinBox_ZQ2.setMaximum(255)
        self.spinBox_ZQ2.setObjectName("spinBox_ZQ2")
        self.gridLayout_1_blockUpr.addWidget(self.spinBox_ZQ2, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_1_blockUpr.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_1_blockUpr.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_1_blockUpr)
        self.gridLayout_2_blockUpr = QtWidgets.QGridLayout()
        self.gridLayout_2_blockUpr.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2_blockUpr.setSpacing(6)
        self.gridLayout_2_blockUpr.setObjectName("gridLayout_2_blockUpr")
        self.pushButton_PG = QtWidgets.QPushButton(self.tab_blockUpr)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-voltmeter-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_PG.setIcon(icon6)
        self.pushButton_PG.setCheckable(True)
        self.pushButton_PG.setObjectName("pushButton_PG")
        self.gridLayout_2_blockUpr.addWidget(self.pushButton_PG, 1, 1, 1, 1)
        self.pushButton_VE3 = QtWidgets.QPushButton(self.tab_blockUpr)
        self.pushButton_VE3.setCheckable(True)
        self.pushButton_VE3.setObjectName("pushButton_VE3")
        self.gridLayout_2_blockUpr.addWidget(self.pushButton_VE3, 1, 0, 1, 1)
        self.pushButton_VE1 = QtWidgets.QPushButton(self.tab_blockUpr)
        self.pushButton_VE1.setCheckable(True)
        self.pushButton_VE1.setObjectName("pushButton_VE1")
        self.gridLayout_2_blockUpr.addWidget(self.pushButton_VE1, 0, 0, 1, 1)
        self.pushButton_VE2 = QtWidgets.QPushButton(self.tab_blockUpr)
        self.pushButton_VE2.setCheckable(True)
        self.pushButton_VE2.setObjectName("pushButton_VE2")
        self.gridLayout_2_blockUpr.addWidget(self.pushButton_VE2, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2_blockUpr)
        self.groupBox_meas_upr = QtWidgets.QGroupBox(self.tab_blockUpr)
        self.groupBox_meas_upr.setFlat(True)
        self.groupBox_meas_upr.setObjectName("groupBox_meas_upr")
        self.formLayout_3_blockUpr = QtWidgets.QFormLayout(self.groupBox_meas_upr)
        self.formLayout_3_blockUpr.setObjectName("formLayout_3_blockUpr")
        self.label_P1_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_P1_U.setObjectName("label_P1_U")
        self.formLayout_3_blockUpr.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_P1_U
        )
        self.label_isP1_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_isP1_U.setObjectName("label_isP1_U")
        self.formLayout_3_blockUpr.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_isP1_U
        )
        self.label_P2_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_P2_U.setObjectName("label_P2_U")
        self.formLayout_3_blockUpr.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_P2_U
        )
        self.label_isP2_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_isP2_U.setObjectName("label_isP2_U")
        self.formLayout_3_blockUpr.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_isP2_U
        )
        self.label_ZQ1_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_ZQ1_U.setObjectName("label_ZQ1_U")
        self.formLayout_3_blockUpr.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_ZQ1_U
        )
        self.label_isZQ1_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_isZQ1_U.setObjectName("label_isZQ1_U")
        self.formLayout_3_blockUpr.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.label_isZQ1_U
        )
        self.label_ZQ2_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_ZQ2_U.setObjectName("label_ZQ2_U")
        self.formLayout_3_blockUpr.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_ZQ2_U
        )
        self.label_isZQ2_U = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_isZQ2_U.setObjectName("label_isZQ2_U")
        self.formLayout_3_blockUpr.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.label_isZQ2_U
        )
        self.label_PG_I = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_PG_I.setObjectName("label_PG_I")
        self.formLayout_3_blockUpr.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_PG_I
        )
        self.label_isPG_I = QtWidgets.QLabel(self.groupBox_meas_upr)
        self.label_isPG_I.setObjectName("label_isPG_I")
        self.formLayout_3_blockUpr.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.label_isPG_I
        )
        self.verticalLayout_4.addWidget(self.groupBox_meas_upr)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-processor-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_blockRasp_blockUpr.addTab(self.tab_blockUpr, icon7, "")
        self.verticalLayout.addWidget(self.tabWidget_blockRasp_blockUpr)
        self.tabWidget_work_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_work_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_work_tab.setObjectName("tabWidget_work_tab")
        self.tab_blockDC = QtWidgets.QWidget()
        self.tab_blockDC.setObjectName("tab_blockDC")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-probability-collision-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_work_tab.addTab(self.tab_blockDC, icon8, "")
        self.tab_blockRF = QtWidgets.QWidget()
        self.tab_blockRF.setObjectName("tab_blockRF")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-sine-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_work_tab.addTab(self.tab_blockRF, icon9, "")
        self.verticalLayout.addWidget(self.tabWidget_work_tab)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(9, 9, 18, 9)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMinimumSize(QtCore.QSize(360, 360))
        self.graphicsView.setMaximumSize(QtCore.QSize(360, 400))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.WaterSensor1 = QtWidgets.QLabel(self.centralwidget)
        self.WaterSensor1.setMaximumSize(QtCore.QSize(24, 24))
        self.WaterSensor1.setText("")
        self.WaterSensor1.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
        )
        self.WaterSensor1.setScaledContents(True)
        self.WaterSensor1.setObjectName("WaterSensor1")
        self.horizontalLayout_6.addWidget(self.WaterSensor1)
        self.WaterLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.WaterLabel1.setObjectName("WaterLabel1")
        self.horizontalLayout_6.addWidget(self.WaterLabel1)
        self.WaterSensor2 = QtWidgets.QLabel(self.centralwidget)
        self.WaterSensor2.setMaximumSize(QtCore.QSize(24, 24))
        self.WaterSensor2.setText("")
        self.WaterSensor2.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
        )
        self.WaterSensor2.setScaledContents(True)
        self.WaterSensor2.setObjectName("WaterSensor2")
        self.horizontalLayout_6.addWidget(self.WaterSensor2)
        self.WaterLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.WaterLabel2.setObjectName("WaterLabel2")
        self.horizontalLayout_6.addWidget(self.WaterLabel2)
        self.WaterSensor3 = QtWidgets.QLabel(self.centralwidget)
        self.WaterSensor3.setMaximumSize(QtCore.QSize(24, 24))
        self.WaterSensor3.setText("")
        self.WaterSensor3.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-sensor-100 (r).png")
        )
        self.WaterSensor3.setScaledContents(True)
        self.WaterSensor3.setObjectName("WaterSensor3")
        self.horizontalLayout_6.addWidget(self.WaterSensor3)
        self.WaterLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.WaterLabel3.setObjectName("WaterLabel3")
        self.horizontalLayout_6.addWidget(self.WaterLabel3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_preasure_P1 = QtWidgets.QLabel(self.centralwidget)
        self.label_preasure_P1.setMaximumSize(QtCore.QSize(24, 24))
        self.label_preasure_P1.setText("")
        self.label_preasure_P1.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-vacuum-bell-jar-100.png")
        )
        self.label_preasure_P1.setScaledContents(True)
        self.label_preasure_P1.setObjectName("label_preasure_P1")
        self.horizontalLayout_4.addWidget(self.label_preasure_P1)
        self.label_P1 = QtWidgets.QLabel(self.centralwidget)
        self.label_P1.setObjectName("label_P1")
        self.horizontalLayout_4.addWidget(self.label_P1)
        self.progressBar_P1 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_P1.setStyleSheet(
            "QProgressBar {\n"
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.46, x2:1, y2:0.44, stop:0.1 rgba(34, 180, 246, 255), stop:0.55 rgba(239, 203, 99, 255),stop:0.71 rgba(239, 203, 99, 255), stop:1 rgba(255, 14, 0, 255));\n"
            "border: solid grey;\n"
            "border-radius: 7px;\n"
            "text-align: center;\n"
            "color: black;\n"
            " }\n"
            "QProgressBar::chunk {\n"
            "background-color: rgba(51, 54, 82, 170);\n"
            "border-radius :7px;\n"
            " }"
        )
        self.progressBar_P1.setMinimum(-200)
        self.progressBar_P1.setMaximum(500)
        self.progressBar_P1.setProperty("value", 130)
        self.progressBar_P1.setTextVisible(False)
        self.progressBar_P1.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar_P1.setInvertedAppearance(False)
        self.progressBar_P1.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_P1.setObjectName("progressBar_P1")
        self.horizontalLayout_4.addWidget(self.progressBar_P1)
        self.label_isP1 = QtWidgets.QLabel(self.centralwidget)
        self.label_isP1.setObjectName("label_isP1")
        self.horizontalLayout_4.addWidget(self.label_isP1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_preasure_P2 = QtWidgets.QLabel(self.centralwidget)
        self.label_preasure_P2.setMaximumSize(QtCore.QSize(24, 24))
        self.label_preasure_P2.setText("")
        self.label_preasure_P2.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-pressure-100.png")
        )
        self.label_preasure_P2.setScaledContents(True)
        self.label_preasure_P2.setObjectName("label_preasure_P2")
        self.horizontalLayout_3.addWidget(self.label_preasure_P2)
        self.label_P2 = QtWidgets.QLabel(self.centralwidget)
        self.label_P2.setObjectName("label_P2")
        self.horizontalLayout_3.addWidget(self.label_P2)
        self.progressBar_P2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_P2.setStyleSheet(
            "QProgressBar {\n"
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.46, x2:1, y2:0.44, stop:0.1 rgba(34, 180, 246, 255), stop:0.55 rgba(239, 203, 99, 255),stop:0.71 rgba(239, 203, 99, 255), stop:1 rgba(255, 14, 0, 255));\n"
            "border: solid grey;\n"
            "border-radius: 7px;\n"
            "text-align: center;\n"
            "color: black;\n"
            " }\n"
            "QProgressBar::chunk {\n"
            "background-color: rgba(51, 54, 82, 170);\n"
            "border-radius :7px;\n"
            " }"
        )
        self.progressBar_P2.setMinimum(-200)
        self.progressBar_P2.setMaximum(500)
        self.progressBar_P2.setProperty("value", 1)
        self.progressBar_P2.setTextVisible(False)
        self.progressBar_P2.setFormat("")
        self.progressBar_P2.setObjectName("progressBar_P2")
        self.horizontalLayout_3.addWidget(self.progressBar_P2)
        self.label_isP2 = QtWidgets.QLabel(self.centralwidget)
        self.label_isP2.setObjectName("label_isP2")
        self.horizontalLayout_3.addWidget(self.label_isP2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_preasure_PG = QtWidgets.QLabel(self.centralwidget)
        self.label_preasure_PG.setMaximumSize(QtCore.QSize(24, 24))
        self.label_preasure_PG.setText("")
        self.label_preasure_PG.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-vacuum-bell-jar-100.png")
        )
        self.label_preasure_PG.setScaledContents(True)
        self.label_preasure_PG.setObjectName("label_preasure_PG")
        self.horizontalLayout_2.addWidget(self.label_preasure_PG)
        self.label_PG = QtWidgets.QLabel(self.centralwidget)
        self.label_PG.setObjectName("label_PG")
        self.horizontalLayout_2.addWidget(self.label_PG)
        self.progressBar_PG = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_PG.setEnabled(True)
        self.progressBar_PG.setStyleSheet(
            "QProgressBar {\n"
            "background-color:qlineargradient(spread:pad, x1:0, y1:0.46, x2:1, y2:0.44, stop:0.1 rgba(34, 180, 246, 255), stop:0.55 rgba(239, 203, 99, 255),stop:0.71 rgba(239, 203, 99, 255), stop:1 rgba(255, 14, 0, 255));\n"
            "border: solid grey;\n"
            "border-radius: 7px;\n"
            "text-align: center;\n"
            "color: black;\n"
            " }\n"
            "QProgressBar::chunk {\n"
            "background-color: rgba(51, 54, 82, 170);\n"
            "border-radius :7px;\n"
            " }"
        )
        self.progressBar_PG.setMinimum(-500)
        self.progressBar_PG.setMaximum(100)
        self.progressBar_PG.setProperty("value", 10)
        self.progressBar_PG.setTextVisible(False)
        self.progressBar_PG.setFormat("")
        self.progressBar_PG.setObjectName("progressBar_PG")
        self.horizontalLayout_2.addWidget(self.progressBar_PG)
        self.label_isPG = QtWidgets.QLabel(self.centralwidget)
        self.label_isPG.setObjectName("label_isPG")
        self.horizontalLayout_2.addWidget(self.label_isPG)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_settings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_settings.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-automatic-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_settings.setIcon(icon10)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout_5.addWidget(self.pushButton_settings)
        self.pushButton_About = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_About.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-book-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_About.setIcon(icon11)
        self.pushButton_About.setObjectName("pushButton_About")
        self.horizontalLayout_5.addWidget(self.pushButton_About)
        self.pushButton_disVolume = QtWidgets.QPushButton(self.centralwidget)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-no-audio-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_disVolume.setIcon(icon12)
        self.pushButton_disVolume.setObjectName("pushButton_disVolume")
        self.horizontalLayout_5.addWidget(self.pushButton_disVolume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_blockRasp_blockUpr.setCurrentIndex(0)
        self.tabWidget_work_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VN3000"))
        self.checkBox_rotation_substrate.setText(
            _translate("MainWindow", "Вращение подложки")
        )
        self.checkBox_currnet_heat.setText(_translate("MainWindow", "Нагрев подложки"))
        self.pushButton_NT.setText(_translate("MainWindow", "NT"))
        self.pushButton_NL.setText(_translate("MainWindow", "NF"))
        self.pushButton_close_VE4.setText(_translate("MainWindow", "Закрыть VE4"))
        self.pushButton_open_VE4.setText(_translate("MainWindow", "Открыть VE4"))
        self.groupBox_meas_rasp.setTitle(_translate("MainWindow", "Измерения"))
        self.label_temperature.setText(_translate("MainWindow", "Температура, ℃"))
        self.label_istemperature.setText(_translate("MainWindow", "TextLabel"))
        self.label_current_heat.setText(_translate("MainWindow", "Ток нагрева, А"))
        self.label_iscurrent_heat.setText(_translate("MainWindow", "TextLabel"))
        self.label_speed.setText(_translate("MainWindow", "Обороты, об/мин"))
        self.label_isspeed.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_blockRasp_blockUpr.setTabText(
            self.tabWidget_blockRasp_blockUpr.indexOf(self.tab_blockRasp),
            _translate("MainWindow", "Блок распределительный"),
        )
        self.checkBox_ZQ2.setText(_translate("MainWindow", "ZQ2"))
        self.checkBox_ZQ1.setText(_translate("MainWindow", "ZQ1"))
        self.pushButton_PG.setText(_translate("MainWindow", "Датчик PG"))
        self.pushButton_VE3.setText(_translate("MainWindow", "Клапан VE3"))
        self.pushButton_VE1.setText(_translate("MainWindow", "Клапан VE1"))
        self.pushButton_VE2.setText(_translate("MainWindow", "Клапан VE2"))
        self.groupBox_meas_upr.setTitle(_translate("MainWindow", "Измерения"))
        self.label_P1_U.setText(_translate("MainWindow", "Напряжение P1, В"))
        self.label_isP1_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_P2_U.setText(_translate("MainWindow", "Напряжение P2, В"))
        self.label_isP2_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_ZQ1_U.setText(_translate("MainWindow", "Напряжение ZQ1, В"))
        self.label_isZQ1_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_ZQ2_U.setText(_translate("MainWindow", "Напряжение ZQ2, В"))
        self.label_isZQ2_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_PG_I.setText(_translate("MainWindow", "Ток эмисси PG, мА"))
        self.label_isPG_I.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_blockRasp_blockUpr.setTabText(
            self.tabWidget_blockRasp_blockUpr.indexOf(self.tab_blockUpr),
            _translate("MainWindow", "Блок управления"),
        )
        self.tabWidget_work_tab.setTabText(
            self.tabWidget_work_tab.indexOf(self.tab_blockDC),
            _translate("MainWindow", "DC"),
        )
        self.tabWidget_work_tab.setTabText(
            self.tabWidget_work_tab.indexOf(self.tab_blockRF),
            _translate("MainWindow", "RF"),
        )
        self.WaterLabel1.setText(_translate("MainWindow", "Вода 1"))
        self.WaterLabel2.setText(_translate("MainWindow", "Вода 2"))
        self.WaterLabel3.setText(_translate("MainWindow", "Вода 3"))
        self.label_P1.setText(_translate("MainWindow", "P1"))
        self.progressBar_P1.setFormat(_translate("MainWindow", "%p%"))
        self.label_isP1.setText(_translate("MainWindow", "TextLabel"))
        self.label_P2.setText(_translate("MainWindow", "P2"))
        self.label_isP2.setText(_translate("MainWindow", "TextLabel"))
        self.label_PG.setText(_translate("MainWindow", "PG"))
        self.label_isPG.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_disVolume.setText(_translate("MainWindow", "Выкл. звук"))


import resources


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
