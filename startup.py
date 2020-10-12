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
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_1_blockRasp = QtWidgets.QGridLayout()
        self.gridLayout_1_blockRasp.setContentsMargins(9, 3, 9, 3)
        self.gridLayout_1_blockRasp.setSpacing(6)
        self.gridLayout_1_blockRasp.setObjectName("gridLayout_1_blockRasp")
        self.spinBox_current_heat = QtWidgets.QSpinBox(self.tab_blockRasp)
        self.spinBox_current_heat.setMaximum(5500)
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
        self.gridLayout_2_blockRasp.setContentsMargins(9, 3, 9, 3)
        self.gridLayout_2_blockRasp.setHorizontalSpacing(9)
        self.gridLayout_2_blockRasp.setVerticalSpacing(6)
        self.gridLayout_2_blockRasp.setObjectName("gridLayout_2_blockRasp")
        self.pushButton_open_VE4 = QtWidgets.QPushButton(self.tab_blockRasp)
        self.pushButton_open_VE4.setObjectName("pushButton_open_VE4")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_open_VE4, 1, 0, 1, 1)
        self.pushButton_close_VE4 = QtWidgets.QPushButton(self.tab_blockRasp)
        self.pushButton_close_VE4.setObjectName("pushButton_close_VE4")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_close_VE4, 1, 1, 1, 1)
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
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_NT, 0, 0, 1, 1)
        self.pushButton_NF = QtWidgets.QPushButton(self.tab_blockRasp)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-pump-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_NF.setIcon(icon2)
        self.pushButton_NF.setCheckable(True)
        self.pushButton_NF.setAutoDefault(False)
        self.pushButton_NF.setDefault(False)
        self.pushButton_NF.setFlat(False)
        self.pushButton_NF.setObjectName("pushButton_NF")
        self.gridLayout_2_blockRasp.addWidget(self.pushButton_NF, 0, 1, 1, 1)
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
        self.formLayout_3_blockRasp.setContentsMargins(-1, 3, -1, 3)
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
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_1_blockUpr = QtWidgets.QGridLayout()
        self.gridLayout_1_blockUpr.setContentsMargins(9, 3, 9, 3)
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
        self.gridLayout_2_blockUpr.setContentsMargins(9, 3, 9, 3)
        self.gridLayout_2_blockUpr.setHorizontalSpacing(9)
        self.gridLayout_2_blockUpr.setVerticalSpacing(6)
        self.gridLayout_2_blockUpr.setObjectName("gridLayout_2_blockUpr")
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
        self.verticalLayout_4.addLayout(self.gridLayout_2_blockUpr)
        self.groupBox_meas_upr = QtWidgets.QGroupBox(self.tab_blockUpr)
        self.groupBox_meas_upr.setFlat(True)
        self.groupBox_meas_upr.setObjectName("groupBox_meas_upr")
        self.formLayout_3_blockUpr = QtWidgets.QFormLayout(self.groupBox_meas_upr)
        self.formLayout_3_blockUpr.setContentsMargins(-1, 3, 9, 3)
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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_blockDC)
        self.verticalLayout_5.setContentsMargins(9, 6, 9, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(9, 6, 9, 6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_enableDcBlock = QtWidgets.QPushButton(self.tab_blockDC)
        self.pushButton_enableDcBlock.setObjectName("pushButton_enableDcBlock")
        self.horizontalLayout_13.addWidget(self.pushButton_enableDcBlock)
        self.pushButton_openDamperDc = QtWidgets.QPushButton(self.tab_blockDC)
        self.pushButton_openDamperDc.setObjectName("pushButton_openDamperDc")
        self.horizontalLayout_13.addWidget(self.pushButton_openDamperDc)
        self.pushButton_posDamperDc = QtWidgets.QPushButton(self.tab_blockDC)
        self.pushButton_posDamperDc.setObjectName("pushButton_posDamperDc")
        self.horizontalLayout_13.addWidget(self.pushButton_posDamperDc)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(9, 6, 9, 6)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_CurrentDcMagnetron = QtWidgets.QSpinBox(self.tab_blockDC)
        self.spinBox_CurrentDcMagnetron.setMaximum(255)
        self.spinBox_CurrentDcMagnetron.setObjectName("spinBox_CurrentDcMagnetron")
        self.gridLayout.addWidget(self.spinBox_CurrentDcMagnetron, 0, 1, 1, 1)
        self.checkBox_CurrentDcMagnetron = QtWidgets.QCheckBox(self.tab_blockDC)
        self.checkBox_CurrentDcMagnetron.setObjectName("checkBox_CurrentDcMagnetron")
        self.gridLayout.addWidget(self.checkBox_CurrentDcMagnetron, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.groupBox_meas_blockDC = QtWidgets.QGroupBox(self.tab_blockDC)
        self.groupBox_meas_blockDC.setFlat(True)
        self.groupBox_meas_blockDC.setObjectName("groupBox_meas_blockDC")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_meas_blockDC)
        self.formLayout.setObjectName("formLayout")
        self.label_I_DcMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockDC)
        self.label_I_DcMagnetron.setObjectName("label_I_DcMagnetron")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_I_DcMagnetron
        )
        self.label_isI_DcMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockDC)
        self.label_isI_DcMagnetron.setObjectName("label_isI_DcMagnetron")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label_isI_DcMagnetron
        )
        self.label_U_DcMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockDC)
        self.label_U_DcMagnetron.setObjectName("label_U_DcMagnetron")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_U_DcMagnetron
        )
        self.label_isU_DcMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockDC)
        self.label_isU_DcMagnetron.setObjectName("label_isU_DcMagnetron")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.label_isU_DcMagnetron
        )
        self.verticalLayout_5.addWidget(self.groupBox_meas_blockDC)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-probability-collision-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_work_tab.addTab(self.tab_blockDC, icon8, "")
        self.tab_blockRF = QtWidgets.QWidget()
        self.tab_blockRF.setObjectName("tab_blockRF")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_blockRF)
        self.verticalLayout_8.setContentsMargins(9, 6, 9, 6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(9, 6, 9, 6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_enableRfBlock = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_enableRfBlock.setObjectName("pushButton_enableRfBlock")
        self.horizontalLayout_12.addWidget(self.pushButton_enableRfBlock)
        self.pushButton_openDamperRf = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_openDamperRf.setObjectName("pushButton_openDamperRf")
        self.horizontalLayout_12.addWidget(self.pushButton_openDamperRf)
        self.pushButton_posDamperRf = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_posDamperRf.setObjectName("pushButton_posDamperRf")
        self.horizontalLayout_12.addWidget(self.pushButton_posDamperRf)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_PowerRFMagnetron = QtWidgets.QLabel(self.tab_blockRF)
        self.label_PowerRFMagnetron.setObjectName("label_PowerRFMagnetron")
        self.horizontalLayout_11.addWidget(self.label_PowerRFMagnetron)
        self.spinBox_powerRfMagnetron = QtWidgets.QSpinBox(self.tab_blockRF)
        self.spinBox_powerRfMagnetron.setMaximum(500)
        self.spinBox_powerRfMagnetron.setObjectName("spinBox_powerRfMagnetron")
        self.horizontalLayout_11.addWidget(self.spinBox_powerRfMagnetron)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_C1Rf = QtWidgets.QLabel(self.tab_blockRF)
        self.label_C1Rf.setObjectName("label_C1Rf")
        self.gridLayout_8.addWidget(self.label_C1Rf, 0, 1, 1, 1)
        self.label_C2Rf = QtWidgets.QLabel(self.tab_blockRF)
        self.label_C2Rf.setObjectName("label_C2Rf")
        self.gridLayout_8.addWidget(self.label_C2Rf, 0, 3, 1, 1)
        self.pushButton_upC1 = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_upC1.setMaximumSize(QtCore.QSize(26, 26))
        self.pushButton_upC1.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/icons/icons/up-chevron.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_upC1.setIcon(icon9)
        self.pushButton_upC1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_upC1.setObjectName("pushButton_upC1")
        self.gridLayout_8.addWidget(self.pushButton_upC1, 0, 0, 1, 1)
        self.pushButton_upC2 = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_upC2.setMaximumSize(QtCore.QSize(26, 26))
        self.pushButton_upC2.setText("")
        self.pushButton_upC2.setIcon(icon9)
        self.pushButton_upC2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_upC2.setObjectName("pushButton_upC2")
        self.gridLayout_8.addWidget(self.pushButton_upC2, 0, 2, 1, 1)
        self.pushButton_downC2 = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_downC2.setMaximumSize(QtCore.QSize(26, 26))
        self.pushButton_downC2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/icons/icons/down-chevron.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_downC2.setIcon(icon10)
        self.pushButton_downC2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_downC2.setObjectName("pushButton_downC2")
        self.gridLayout_8.addWidget(self.pushButton_downC2, 1, 2, 1, 1)
        self.pushButton_downC1 = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_downC1.setMaximumSize(QtCore.QSize(26, 26))
        self.pushButton_downC1.setText("")
        self.pushButton_downC1.setIcon(icon10)
        self.pushButton_downC1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_downC1.setObjectName("pushButton_downC1")
        self.gridLayout_8.addWidget(self.pushButton_downC1, 1, 0, 1, 1)
        self.pushButton_sputteringRf = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_sputteringRf.setObjectName("pushButton_sputteringRf")
        self.gridLayout_8.addWidget(self.pushButton_sputteringRf, 0, 4, 1, 1)
        self.pushButton_sputteringDc = QtWidgets.QPushButton(self.tab_blockRF)
        self.pushButton_sputteringDc.setObjectName("pushButton_sputteringDc")
        self.gridLayout_8.addWidget(self.pushButton_sputteringDc, 1, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_8.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout_8.addItem(spacerItem6, 1, 3, 1, 1)
        self.horizontalLayout_11.addLayout(self.gridLayout_8)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.groupBox_meas_blockRf = QtWidgets.QGroupBox(self.tab_blockRF)
        self.groupBox_meas_blockRf.setFlat(True)
        self.groupBox_meas_blockRf.setObjectName("groupBox_meas_blockRf")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_meas_blockRf)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_KBV = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_KBV.setObjectName("label_KBV")
        self.gridLayout_5.addWidget(self.label_KBV, 2, 2, 1, 1)
        self.label_I_RfAnode = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_I_RfAnode.setObjectName("label_I_RfAnode")
        self.gridLayout_5.addWidget(self.label_I_RfAnode, 3, 0, 1, 1)
        self.label_PowerRf = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_PowerRf.setObjectName("label_PowerRf")
        self.gridLayout_5.addWidget(self.label_PowerRf, 2, 0, 1, 1)
        self.label_I_RfDriver = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_I_RfDriver.setObjectName("label_I_RfDriver")
        self.gridLayout_5.addWidget(self.label_I_RfDriver, 4, 0, 1, 1)
        self.label_isPowerRf = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_isPowerRf.setObjectName("label_isPowerRf")
        self.gridLayout_5.addWidget(self.label_isPowerRf, 2, 1, 1, 1)
        self.label_I_RfMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_I_RfMagnetron.setObjectName("label_I_RfMagnetron")
        self.gridLayout_5.addWidget(self.label_I_RfMagnetron, 4, 2, 1, 1)
        self.label_URfMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_URfMagnetron.setObjectName("label_URfMagnetron")
        self.gridLayout_5.addWidget(self.label_URfMagnetron, 3, 2, 1, 1)
        self.label_isKBV = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_isKBV.setObjectName("label_isKBV")
        self.gridLayout_5.addWidget(self.label_isKBV, 2, 3, 1, 1)
        self.label_isI_RfAnode = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_isI_RfAnode.setObjectName("label_isI_RfAnode")
        self.gridLayout_5.addWidget(self.label_isI_RfAnode, 3, 1, 1, 1)
        self.label_IsI_RfDriver = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_IsI_RfDriver.setObjectName("label_IsI_RfDriver")
        self.gridLayout_5.addWidget(self.label_IsI_RfDriver, 4, 1, 1, 1)
        self.label_isU_RfMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_isU_RfMagnetron.setObjectName("label_isU_RfMagnetron")
        self.gridLayout_5.addWidget(self.label_isU_RfMagnetron, 3, 3, 1, 1)
        self.label_IsI_RfMagnetron = QtWidgets.QLabel(self.groupBox_meas_blockRf)
        self.label_IsI_RfMagnetron.setObjectName("label_IsI_RfMagnetron")
        self.gridLayout_5.addWidget(self.label_IsI_RfMagnetron, 4, 3, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_meas_blockRf)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-sine-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.tabWidget_work_tab.addTab(self.tab_blockRF, icon11, "")
        self.verticalLayout.addWidget(self.tabWidget_work_tab)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(9, 9, 18, 9)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(360, 360))
        self.graphicsView.setMaximumSize(QtCore.QSize(360, 360))
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)
        self.graphicsView.setViewportUpdateMode(
            QtWidgets.QGraphicsView.SmartViewportUpdate
        )
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        spacerItem7 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem7)
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
            QtGui.QPixmap(":/icons/icons/icons8-sensor-100.png")
        )
        self.WaterSensor3.setScaledContents(True)
        self.WaterSensor3.setObjectName("WaterSensor3")
        self.horizontalLayout_6.addWidget(self.WaterSensor3)
        self.WaterLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.WaterLabel3.setObjectName("WaterLabel3")
        self.horizontalLayout_6.addWidget(self.WaterLabel3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_pressure_P1 = QtWidgets.QLabel(self.centralwidget)
        self.label_pressure_P1.setMaximumSize(QtCore.QSize(24, 24))
        self.label_pressure_P1.setText("")
        self.label_pressure_P1.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-vacuum-bell-jar-100.png")
        )
        self.label_pressure_P1.setScaledContents(True)
        self.label_pressure_P1.setObjectName("label_pressure_P1")
        self.horizontalLayout_4.addWidget(self.label_pressure_P1)
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
        self.label_pressure_P2 = QtWidgets.QLabel(self.centralwidget)
        self.label_pressure_P2.setMaximumSize(QtCore.QSize(24, 24))
        self.label_pressure_P2.setText("")
        self.label_pressure_P2.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-pressure-100.png")
        )
        self.label_pressure_P2.setScaledContents(True)
        self.label_pressure_P2.setObjectName("label_pressure_P2")
        self.horizontalLayout_3.addWidget(self.label_pressure_P2)
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
        self.label_pressure_PG = QtWidgets.QLabel(self.centralwidget)
        self.label_pressure_PG.setEnabled(True)
        self.label_pressure_PG.setMaximumSize(QtCore.QSize(24, 24))
        self.label_pressure_PG.setText("")
        self.label_pressure_PG.setPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-vacuum-bell-jar-100.png")
        )
        self.label_pressure_PG.setScaledContents(True)
        self.label_pressure_PG.setObjectName("label_pressure_PG")
        self.horizontalLayout_2.addWidget(self.label_pressure_PG)
        self.label_PG = QtWidgets.QLabel(self.centralwidget)
        self.label_PG.setEnabled(True)
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
        self.label_isPG.setEnabled(True)
        self.label_isPG.setObjectName("label_isPG")
        self.horizontalLayout_2.addWidget(self.label_isPG)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_settings = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_settings.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-automatic-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_settings.setIcon(icon12)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout_5.addWidget(self.pushButton_settings)
        self.pushButton_About = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_About.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-book-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_About.setIcon(icon13)
        self.pushButton_About.setObjectName("pushButton_About")
        self.horizontalLayout_5.addWidget(self.pushButton_About)
        self.pushButton_disVolume = QtWidgets.QPushButton(self.centralwidget)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(
            QtGui.QPixmap(":/icons/icons/icons8-no-audio-100.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.pushButton_disVolume.setIcon(icon14)
        self.pushButton_disVolume.setObjectName("pushButton_disVolume")
        self.horizontalLayout_5.addWidget(self.pushButton_disVolume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout_2.addItem(spacerItem9)
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
            _translate("MainWindow", "╨Т╤А╨░╤Й╨╡╨╜╨╕╨╡ ╨┐╨╛╨┤╨╗╨╛╨╢╨║╨╕")
        )
        self.checkBox_currnet_heat.setText(
            _translate("MainWindow", "╨Э╨░╨│╤А╨╡╨▓ ╨┐╨╛╨┤╨╗╨╛╨╢╨║╨╕")
        )
        self.pushButton_open_VE4.setText(_translate("MainWindow", "╨Ю╤В╨║╤А╤Л╤В╤М VE4"))
        self.pushButton_close_VE4.setText(
            _translate("MainWindow", "╨Ч╨░╨║╤А╤Л╤В╤М VE4")
        )
        self.pushButton_NT.setText(_translate("MainWindow", "NT"))
        self.pushButton_NF.setText(_translate("MainWindow", "NF"))
        self.groupBox_meas_rasp.setTitle(_translate("MainWindow", "╨Ш╨╖╨╝╨╡╤А╨╡╨╜╨╕╤П"))
        self.label_temperature.setText(
            _translate("MainWindow", "╨в╨╡╨╝╨┐╨╡╤А╨░╤В╤Г╤А╨░")
        )
        self.label_istemperature.setText(_translate("MainWindow", "TextLabel"))
        self.label_current_heat.setText(
            _translate("MainWindow", "╨в╨╛╨║ ╨╜╨░╨│╤А╨╡╨▓╨░")
        )
        self.label_iscurrent_heat.setText(_translate("MainWindow", "TextLabel"))
        self.label_speed.setText(_translate("MainWindow", "╨Ю╨▒╨╛╤А╨╛╤В╤Л"))
        self.label_isspeed.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_blockRasp_blockUpr.setTabText(
            self.tabWidget_blockRasp_blockUpr.indexOf(self.tab_blockRasp),
            _translate("MainWindow", "╨С╨╗╨╛╨║ ╤А╨░╤Б╨┐╤А╨╡╨┤╨╡╨╗╨╕╤В╨╡╨╗╤М╨╜╤Л╨╣"),
        )
        self.checkBox_ZQ2.setText(_translate("MainWindow", "ZQ2"))
        self.checkBox_ZQ1.setText(_translate("MainWindow", "ZQ1"))
        self.pushButton_VE3.setText(_translate("MainWindow", "╨Ъ╨╗╨░╨┐╨░╨╜ VE3"))
        self.pushButton_VE1.setText(_translate("MainWindow", "╨Ъ╨╗╨░╨┐╨░╨╜ VE1"))
        self.pushButton_VE2.setText(_translate("MainWindow", "╨Ъ╨╗╨░╨┐╨░╨╜ VE2"))
        self.pushButton_PG.setText(_translate("MainWindow", "╨Ф╨░╤В╤З╨╕╨║ PG"))
        self.groupBox_meas_upr.setTitle(_translate("MainWindow", "╨Ш╨╖╨╝╨╡╤А╨╡╨╜╨╕╤П"))
        self.label_P1_U.setText(_translate("MainWindow", "╨Э╨░╨┐╤А╤П╨╢╨╡╨╜╨╕╨╡ P1"))
        self.label_isP1_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_P2_U.setText(_translate("MainWindow", "╨Э╨░╨┐╤А╤П╨╢╨╡╨╜╨╕╨╡ P2"))
        self.label_isP2_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_ZQ1_U.setText(_translate("MainWindow", "╨Э╨░╨┐╤А╤П╨╢╨╡╨╜╨╕╨╡ ZQ1"))
        self.label_isZQ1_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_ZQ2_U.setText(_translate("MainWindow", "╨Э╨░╨┐╤А╤П╨╢╨╡╨╜╨╕╨╡ ZQ2"))
        self.label_isZQ2_U.setText(_translate("MainWindow", "TextLabel"))
        self.label_PG_I.setText(_translate("MainWindow", "╨в╨╛╨║ ╤Н╨╝╨╕╤Б╤Б╨╕ PG"))
        self.label_isPG_I.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_blockRasp_blockUpr.setTabText(
            self.tabWidget_blockRasp_blockUpr.indexOf(self.tab_blockUpr),
            _translate("MainWindow", "╨С╨╗╨╛╨║ ╤Г╨┐╤А╨░╨▓╨╗╨╡╨╜╨╕╤П"),
        )
        self.pushButton_enableDcBlock.setText(
            _translate("MainWindow", "╨Т╨║╨╗. ╨▒╨╗╨╛╨║")
        )
        self.pushButton_openDamperDc.setText(
            _translate("MainWindow", "╨Ю╤В╨║╤А. ╨╖╨░╤Б╨╗╨╛╨╜╨║╤Г")
        )
        self.pushButton_posDamperDc.setText(
            _translate("MainWindow", "╨Я╨╛╨╖. ╨╖╨░╤Б╨╗╨╛╨╜╨║╤Г")
        )
        self.checkBox_CurrentDcMagnetron.setText(
            _translate("MainWindow", "╨в╨╛╨║ ╨╝╨░╨│╨╜╨╡╤В╤А╨╛╨╜╨░")
        )
        self.groupBox_meas_blockDC.setTitle(
            _translate("MainWindow", "╨Ш╨╖╨╝╨╡╤А╨╡╨╜╨╕╤П")
        )
        self.label_I_DcMagnetron.setText(
            _translate("MainWindow", "I, ╨╝╨░╨│╨╜╨╡╤В╤А╨╛╨╜╨░")
        )
        self.label_isI_DcMagnetron.setText(_translate("MainWindow", "TextLabel"))
        self.label_U_DcMagnetron.setText(
            _translate("MainWindow", "U, ╨╝╨░╨│╨╜╨╡╤В╤А╨╛╨╜╨░")
        )
        self.label_isU_DcMagnetron.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_work_tab.setTabText(
            self.tabWidget_work_tab.indexOf(self.tab_blockDC),
            _translate("MainWindow", "DC"),
        )
        self.pushButton_enableRfBlock.setText(
            _translate("MainWindow", "╨Т╨║╨╗. ╨▒╨╗╨╛╨║")
        )
        self.pushButton_openDamperRf.setText(
            _translate("MainWindow", "╨Ю╤В╨║╤А. ╨╖╨░╤Б╨╗╨╛╨╜╨║╤Г")
        )
        self.pushButton_posDamperRf.setText(
            _translate("MainWindow", "╨Я╨╛╨╖. ╨╖╨░╤Б╨╗╨╛╨╜╨║╤Г")
        )
        self.label_PowerRFMagnetron.setText(
            _translate("MainWindow", "╨Ь╨╛╤Й╨╜╨╛╤Б╤В╤М (╨Т╤В)")
        )
        self.label_C1Rf.setText(_translate("MainWindow", "╨б1"))
        self.label_C2Rf.setText(_translate("MainWindow", "╨б2"))
        self.pushButton_sputteringRf.setText(
            _translate("MainWindow", "╨Э╨░╨┐╤Л╨╗╨╡╨╜╨╕╨╡")
        )
        self.pushButton_sputteringDc.setText(
            _translate("MainWindow", "╨г╤Б╤В╨░╨╜╨╛╨▓╨╕╤В╤М")
        )
        self.groupBox_meas_blockRf.setTitle(
            _translate("MainWindow", "╨Ш╨╖╨╝╨╡╤А╨╡╨╜╨╕╤П")
        )
        self.label_KBV.setText(_translate("MainWindow", "╨Ъ╨С╨Т"))
        self.label_I_RfAnode.setText(_translate("MainWindow", "I, ╨░╨╜╨╛╨┤╨░"))
        self.label_PowerRf.setText(_translate("MainWindow", "╨Ь╨╛╤Й╨╜╨╛╤Б╤В╤М"))
        self.label_I_RfDriver.setText(_translate("MainWindow", "I, ╨┤╤А╨░╨╣╨▓╨╡╤А╨░"))
        self.label_isPowerRf.setText(_translate("MainWindow", "TextLabel"))
        self.label_I_RfMagnetron.setText(
            _translate("MainWindow", "I, ╨╝╨░╨│╨╜╨╡╤В╤А╨╛╨╜╨░")
        )
        self.label_URfMagnetron.setText(
            _translate("MainWindow", "U, ╨╝╨░╨│╨╜╨╡╤В╤А╨╛╨╜╨░")
        )
        self.label_isKBV.setText(_translate("MainWindow", "TextLabel"))
        self.label_isI_RfAnode.setText(_translate("MainWindow", "TextLabel"))
        self.label_IsI_RfDriver.setText(_translate("MainWindow", "TextLabel"))
        self.label_isU_RfMagnetron.setText(_translate("MainWindow", "TextLabel"))
        self.label_IsI_RfMagnetron.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget_work_tab.setTabText(
            self.tabWidget_work_tab.indexOf(self.tab_blockRF),
            _translate("MainWindow", "RF"),
        )
        self.WaterLabel1.setText(_translate("MainWindow", "╨Т╨╛╨┤╨░ 1"))
        self.WaterLabel2.setText(_translate("MainWindow", "╨Т╨╛╨┤╨░ 2"))
        self.WaterLabel3.setText(_translate("MainWindow", "╨Т╨╛╨┤╨░ 3"))
        self.label_P1.setText(_translate("MainWindow", "P1"))
        self.progressBar_P1.setFormat(_translate("MainWindow", "%p%"))
        self.label_isP1.setText(_translate("MainWindow", "TextLabel"))
        self.label_P2.setText(_translate("MainWindow", "P2"))
        self.label_isP2.setText(_translate("MainWindow", "TextLabel"))
        self.label_PG.setText(_translate("MainWindow", "PG"))
        self.label_isPG.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_disVolume.setText(
            _translate("MainWindow", "╨Т╤Л╨║╨╗. ╨╖╨▓╤Г╨║")
        )


import resources
