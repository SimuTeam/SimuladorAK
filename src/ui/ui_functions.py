################################################################################
##
## SIGMA BY: LUCAS DEPETRIS
## BASED ON WANDERSON M. PIMENTA'S PROJECT AND COMSYS-TRAINER BY SOUMADIP DEY
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUNT INITIAL MENU
count = 1

class UIFunctions(MainWindow):

    ## ==> GLOBALS
    GLOBAL_STATE = 0
    GLOBAL_TITLE_BAR = True
    icons = []
    theme = "default"

    # custom_font = QFont('Satoshi Black')
    # custom_font.setWeight(18);
    # QApplication.setFont(custom_font, "QPushButton")

    ########################################################################
    ## START - GUI FUNCTIONS
    ########################################################################

    ## ==> MAXIMIZE/RESTORE
    ########################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_maximize_restore.setToolTip("Restore")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            if UIFunctions.theme == "default":
                self.ui.frame_top_btns.setStyleSheet("background-color: rgb(27, 29, 35)")
            elif UIFunctions.theme == "ak":
                self.ui.frame_top_btns.setStyleSheet("background-color: rgb(43, 112, 74)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            if UIFunctions.theme == "default":
                self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            elif UIFunctions.theme == "ak":
                self.ui.frame_top_btns.setStyleSheet("background-color: rgba(43, 112, 74, 200)")
            self.ui.frame_size_grip.show()


    ## ==> RETURN STATUS
    def returnStatus():
        return GLOBAL_STATE

    ## ==> SET STATUS
    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    ## ==> ENABLE MAXIMUM SIZE
    ########################################################################
    def enableMaximumSize(self, width, height):
        if width != '' and height != '':
            self.setMaximumSize(QSize(width, height))
            self.ui.frame_size_grip.hide()
            self.ui.btn_maximize_restore.hide()


    ## ==> TOGGLE MENU
    ########################################################################
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    ## ==> SET TITLE BAR
    ########################################################################
    def removeTitleBar(status):
        global GLOBAL_TITLE_BAR
        GLOBAL_TITLE_BAR = status

    ## ==> HEADER TEXTS
    ########################################################################
    # LABEL TITLE
    def labelTitle(self, text):
        self.ui.label_title_bar_top.setText(text)

    # LABEL DESCRIPTION
    def labelDescription(self, text):
        self.ui.label_top_info_1.setText(text)

    ## ==> DYNAMIC MENUS
    ########################################################################
    def addNewMenu(self, name, objName, icon, isTopMenu):
        font = QFont()
        font.setFamily(u"Satoshi Black")
        font.setBold(True)
        font.setPixelSize(18)
        button = QPushButton(str(count),self)
        button.setObjectName(objName)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy3)
        button.setMinimumSize(QSize(0, 70))
        button.setLayoutDirection(Qt.LeftToRight)
        button.setFont(font)
        button.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', icon))
        UIFunctions.icons.append(icon)
        button.setText(name)
        button.setToolTip(name)
        button.clicked.connect(self.Button)

        if isTopMenu:
            self.ui.layout_menus.addWidget(button)
        else:
            self.ui.layout_menu_bottom.addWidget(button)

    ## ==> SELECT/DESELECT MENU
    ########################################################################
    ## ==> SELECT
    def selectMenu(getStyle):
        color = "rgb(238, 238, 238);"
        if UIFunctions.theme == "default":
            color = "rgb(44, 49, 60);"
        elif UIFunctions.theme == "ak":
            color = "rgb(255, 255, 255);"

        select = getStyle + ("QPushButton { border-right: 7px solid " + color + " }")
        return select

    ## ==> DESELECT
    def deselectMenu(getStyle):
        color = "rgb(44, 49, 60);"
        if UIFunctions.theme == "default":
            color = "rgb(44, 49, 60);"
        elif UIFunctions.theme == "ak":
            color = "rgb(255, 255, 255);"
            
        deselect = getStyle.replace("QPushButton { border-right: 7px solid " + color + " }", "")
        return deselect

    ## ==> START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    ## ==> RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.frame_left_menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

    ## ==> CHANGE PAGE LABEL TEXT
    def labelPage(self, text):
        newText = '| ' + text.upper()
        self.ui.label_top_info_2.setText(newText)

    ## ==> CHANGE LABEL CREDITS TEXT
    def labelCredits(self, text):
        self.ui.label_credits.setText(text)

    ## ==> CHANGE LABEL VERSION TEXT
    def labelVersion(self, text):
        self.ui.label_version.setText(text)

    ## ==> USER ICON
    ########################################################################
    def userIcon(self, initialsTooltip, icon, showHide):
        if showHide:
            # SET TEXT
            self.ui.label_user_icon.setText(initialsTooltip)

            # SET ICON
            if icon:
                style = self.ui.label_user_icon.styleSheet()
                setIcon = "QLabel { background-image: " + icon + "; }"
                self.ui.label_user_icon.setStyleSheet(style + setIcon)
                self.ui.label_user_icon.setText('')
                self.ui.label_user_icon.setToolTip(initialsTooltip)
        else:
            self.ui.label_user_icon.hide()

    def themeSwitcher(self, btnWidget, theme = "default"):
        UIFunctions.theme = theme
        if theme == "default":
            # self.ui.frame_top_btns.setStyleSheet(self.ui.frame_top_btns.styleSheet().replace("background-color: rgb(63, 137, 75);", "background-color: rgba(27, 29, 35, 200);"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200);")
            self.ui.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
            self.ui.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
            
            self.ui.label_top_info_1.setStyleSheet("color: rgb(159, 165, 177);")
            self.ui.label_top_info_2.setStyleSheet("color: rgb(159, 165, 177);")
            self.ui.label_credits.setStyleSheet("color: rgb(159, 165, 177);")
            self.ui.label_version.setStyleSheet("color: rgb(159, 165, 177);")

            for i, w in enumerate(self.ui.frame_left_menu.findChildren(QPushButton)):
                w.setStyleSheet(Style.style_bt_standard.replace('ICON_REPLACE', UIFunctions.icons[i]))
            btnWidget.setStyleSheet(btnWidget.styleSheet().replace("url(:/16x16/icons/16x16/cil-moon.png)", "url(:/16x16/icons/16x16/cil-lightbulb.png)"))
            self.ui.btn_toggle_menu.setStyleSheet(self.ui.btn_toggle_menu.styleSheet().replace("background-color: #195B47;", "background-color: rgb(27, 29, 35);"))
            
            self.ui.label_user_icon.setStyleSheet(self.ui.label_user_icon.styleSheet().replace("background-color: rgb(44, 60, 47);", "background-color: rgb(44, 49, 60);"))
            self.ui.label_user_icon.setStyleSheet(self.ui.label_user_icon.styleSheet().replace("border: 5px solid rgb(25, 91, 42);", "border: 5px solid rgb(39, 44, 54);"))
        elif theme == "ak":
            self.ui.frame_top_btns.setStyleSheet("background-color: rgb(43, 112, 74);")
            self.ui.frame_left_menu.setStyleSheet("background-color: rgb(63, 137, 75);")
            self.ui.frame_top_info.setStyleSheet("background-color: rgb(63, 137, 75);")
            self.ui.frame_grip.setStyleSheet("background-color: rgb(63, 137, 75);")

            self.ui.label_top_info_1.setStyleSheet("color: rgb(230, 230, 230);")
            self.ui.label_top_info_2.setStyleSheet("color: rgb(230, 230, 230);")
            self.ui.label_credits.setStyleSheet("color: rgb(230, 230, 230);")
            self.ui.label_version.setStyleSheet("color: rgb(230, 230, 230);")

            for i, w in enumerate(self.ui.frame_left_menu.findChildren(QPushButton)):
                w.setStyleSheet(Style.style_bt_ak.replace('ICON_REPLACE', UIFunctions.icons[i]))
            btnWidget.setStyleSheet(btnWidget.styleSheet().replace("url(:/16x16/icons/16x16/cil-lightbulb.png)", "url(:/16x16/icons/16x16/cil-moon.png)"))
            self.ui.btn_toggle_menu.setStyleSheet(self.ui.btn_toggle_menu.styleSheet().replace("background-color: rgb(27, 29, 35);", "background-color: #195B47;"))

            self.ui.label_user_icon.setStyleSheet(self.ui.label_user_icon.styleSheet().replace("background-color: rgb(44, 49, 60);", "background-color: rgb(38, 107, 51);"))
            self.ui.label_user_icon.setStyleSheet(self.ui.label_user_icon.styleSheet().replace("border: 5px solid rgb(39, 44, 54);", "border: 5px solid rgb(25, 91, 42);"))

    # rgb(43, 112, 74)
    # rgb(63, 137, 75)
    # rgb(25, 91, 71)
    # rgb(85, 170, 255)

    ########################################################################
    ## END - GUI FUNCTIONS
    ########################################################################


    ########################################################################
    ## START - GUI DEFINITIONS
    ########################################################################

    ## ==> UI DEFINITIONS
    ########################################################################
    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: UIFunctions.maximize_restore(self))

        ## REMOVE ==> STANDARD TITLE BAR
        if GLOBAL_TITLE_BAR:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_label_top_btns.mouseDoubleClickEvent = dobleClickMaximizeRestore
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.frame_label_top_btns.setContentsMargins(8, 0, 0, 5)
            self.ui.frame_label_top_btns.setMinimumHeight(42)
            self.ui.frame_icon_top_bar.hide()
            self.ui.frame_btns_right.hide()
            self.ui.frame_size_grip.hide()

        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.frame_main.setGraphicsEffect(self.shadow)

        ## ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        ### ==> MINIMIZE
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        ## ==> MAXIMIZE/RESTORE
        self.ui.btn_maximize_restore.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        ## SHOW ==> CLOSE APPLICATION
        self.ui.btn_close.clicked.connect(lambda: QApplication.closeAllWindows())    

    ########################################################################
    ## END - GUI DEFINITIONS
    ########################################################################

def fontManager(self, status):
    if status == 0:
        self.ui.messageInputASK.setFont(QFont('Satoshi Black', 12))
        self.ui.carrierFreqInputASK.setFont(QFont('Satoshi Black', 12))
        self.ui.modulateBtnASK.setFont(QFont('Satoshi Black', 20))
        self.ui.clearBtnASK.setFont(QFont('Satoshi Black', 20))
        self.ui.messageInputFSK.setFont(QFont('Satoshi Black', 12))
        self.ui.carrierFreq1InputFSK.setFont(QFont('Satoshi Black', 12))
        self.ui.carrierFreq2InputFSK.setFont(QFont('Satoshi Black', 12))
        self.ui.modulateBtnFSK.setFont(QFont('Satoshi Black', 20))
        self.ui.Btn_pauseASK.setFont(QFont('Satoshi Black', 20))
        self.ui.Btn_helpASK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_pauseFSK.setFont(QFont('Satoshi Black', 20))
        self.ui.Btn_helpFSK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_pausePSK.setFont(QFont('Satoshi Black', 20))
        self.ui.Btn_helpPSK.setFont(QFont('Satoshi Black', 14))
        self.ui.clearBtnFSK.setFont(QFont('Satoshi Black', 20))
        self.ui.messageInputPSK.setFont(QFont('Satoshi Black', 12))
        self.ui.carrierFreqInputPSK.setFont(QFont('Satoshi Black', 12))
        self.ui.modulateBtnPSK.setFont(QFont('Satoshi Black', 20))
        self.ui.clearBtnPSK.setFont(QFont('Satoshi Black', 20))
    else: 
        self.ui.messageInputASK.setFont(QFont('Satoshi Black', 10))
        self.ui.carrierFreqInputASK.setFont(QFont('Satoshi Black', 10))
        self.ui.modulateBtnASK.setFont(QFont('Satoshi Black', 14))
        self.ui.clearBtnASK.setFont(QFont('Satoshi Black', 14))
        self.ui.messageInputFSK.setFont(QFont('Satoshi Black', 10))
        self.ui.carrierFreq1InputFSK.setFont(QFont('Satoshi Black', 10))
        self.ui.carrierFreq2InputFSK.setFont(QFont('Satoshi Black', 10))
        self.ui.modulateBtnFSK.setFont(QFont('Satoshi Black', 14))
        self.ui.clearBtnFSK.setFont(QFont('Satoshi Black', 14))
        self.ui.messageInputPSK.setFont(QFont('Satoshi Black', 10))
        self.ui.carrierFreqInputPSK.setFont(QFont('Satoshi Black', 10))
        self.ui.modulateBtnPSK.setFont(QFont('Satoshi Black', 14))
        self.ui.clearBtnPSK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_pauseASK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_helpASK.setFont(QFont('Satoshi Black', 12))
        self.ui.Btn_pauseFSK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_helpFSK.setFont(QFont('Satoshi Black', 12))
        self.ui.Btn_pausePSK.setFont(QFont('Satoshi Black', 14))
        self.ui.Btn_helpPSK.setFont(QFont('Satoshi Black', 12))